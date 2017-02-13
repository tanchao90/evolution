#!/usr/bin/python
# -*- coding: utf-8 -*-


__author__ = "Tan Chao"
__email__ = "tanchao_bupt@163.com"
__version__ = "1.0.0"


import time
import numpy as np
import matplotlib.pyplot as plt


'''BezierCurve
   1. 实现贝塞尔曲线
   2. 支持随意阶数
   3. 点支持多维
   4. 相机跟随示例
   5. 测试用例，并画图对比结果
'''


class BezierCurve(object):
    """docstring for BezierCurve
    """
    def __init__(self, points):
        super(BezierCurve, self).__init__()

        self.resetPoints(points)

    def resetPoints(self, points):
        """重置原始曲线上的关键点
        Note:
            degree 阶数: len(points)
            dimension 维数: len(points[0])
        """
        self.points = points or []

    def getPointAt(self, t=0.5):
        """获取t时刻的值

        Args:
            t (float): 时刻

        Returns:
            返回t时刻的点
        """
        return self.computePointAt(0, len(self.points)-1, t)

    def computePointAt(self, start, end, t):
        """递归计算t时刻的点

        Note:
            t本质上反应了起点和终点所占的权重
            t==0: 起点全部权重
            t==1: 终点全部权重

        Args:
            start (int): 起点
            end (int): 终点
            t (float): 时刻

        Returns:
            返回t时刻的点
        """
        if start == end:
            return self.points[start]

        b1 = self.computePointAt(start, end-1, t)
        b2 = self.computePointAt(start+1, end, t)

        point = []
        for i in xrange(0, len(b1)):
            point.append((1-t)*b1[i] + t*b2[i])

        return point


class BezierCurveImprove(BezierCurve):
    """docstring for BezierCurveImprove
    缓存中间计算结果，用空间换时间，提升效率
    self.cache (map): 缓存中间结果
    """
    def __init__(self, points):
        super(BezierCurveImprove, self).__init__(points)

    def resetPoints(self, points):
        super(BezierCurveImprove, self).resetPoints(points)
        self.cache = {} # {"start:end:t": point}

    def computePointAt(self, start, end, t):
        key = '%s:%s:%s' % (start, end, t)
        point = self.cache.get(key, None)
        if point:
            return point

        point = super(BezierCurveImprove, self).computePointAt(start, end, t)
        self.cache[key] = point

        return point


class CameraFollow(object):
    """docstring for CameraFollow"""
    def __init__(self, delayFrame=5):
        super(CameraFollow, self).__init__()
        self.targetPath = [] # 相机需要跟随的路径
        self.delayFrame = delayFrame # 延后跟随的帧数
        self.bezierCurve = BezierCurve([])

    def updateTarget(self, point):
        """根据玩家的坐标更新来不断更新相机目标
        也可以玩家坐标更新与相机目标更新按不同的节奏
        """
        self.targetPath.append(point)
        if len(self.targetPath) > self.delayFrame:
            self.targetPath.pop(0)

        self.bezierCurve.resetPoints(self.targetPath)
        return self.bezierCurve.getPointAt(0.5)


class Plotting(object):
    """docstring for Plotting"""
    def __init__(self, title):
        super(Plotting, self).__init__()
        self.reset(title)

    def reset(self, title):
        plt.title(title)
        plt.xlabel('x-coordinate')
        plt.ylabel('y-coordinate')

    def draw(self, points, style='.-', label=''):
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        plt.plot(x, y, style, label=label)
        if label:
            plt.legend(loc='upper left')
        plt.tight_layout() # 自动调整布局

    def show(self):
        plt.show()


class PlottingSubplot(Plotting):
    def __init__(self, title, row, col):
        super(PlottingSubplot, self).__init__(title)
        self.row = row
        self.col = col

    def draw(self, points, plotNumber, title='', style='.-'):
        ax = plt.subplot(self.row, self.col, plotNumber)
        ax.set_title(title)
        super(PlottingSubplot, self).draw(points, style)


# ----------------------------------------------------------------
# --------------------------Test----------------------------------
def testDegreeImpl(points, count, ps, plotNumber):
    bc = BezierCurve(points)
    curvePoints = []
    for t in xrange(0, count+1):
        curvePoints.append(bc.getPointAt(1.0*t/count))

    title = 'Bezier Curve: Degree %s' % (len(points, ))
    ps.draw(points, plotNumber, title=title, style='.-')
    ps.draw(curvePoints, plotNumber, title=title, style='.-r')

def testDegreeN():
    ps = PlottingSubplot('Bezier Curve', 2, 2)

    points3 = [(1, 1), (2, 3), (3, 1)]
    points4 = [(1, 1), (0.5, 3), (3, 4), (4, 1)]
    points5 = [(1, 1), (0.5, 3), (3, 4), (4, 1), (5, 5)]
    points10 = [(1, 1), (0.5, 3), (3, 4), (4, 1), (5, 10), (6, 5), (6, 8), (7, 4), (8, 2), (9, 6)]

    testDegreeImpl(points3, 10, ps, 1)
    testDegreeImpl(points4, 10, ps, 2)
    testDegreeImpl(points5, 10, ps, 3)
    testDegreeImpl(points10, 20, ps, 4)

    ps.show()


def testCamera():
    """
    测试结果显示延迟的帧数越多，跟随越平滑
    但是实际中不能延迟太多帧，否则会出现镜头跟随不及时，并且计算会非常耗时
    """
    avatarPos = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (1, 4), (2, 4), (3, 4), (4, 4), (4, 5), (5, 1)]
    avatarPos += [(6, 2)] * 10 # 表示avatar停在某个位置了，镜头最终还是会跟随到玩家位置

    followPos3 = []
    cf3 = CameraFollow(3)
    for target in avatarPos:
        followPos3.append(cf3.updateTarget(target))

    followPos5 = []
    cf5 = CameraFollow(5)
    for target in avatarPos:
        followPos5.append(cf5.updateTarget(target))

    followPos10 = []
    cf10 = CameraFollow(10)
    for target in avatarPos:
        followPos10.append(cf10.updateTarget(target))

    p = Plotting('Bezier Curve: Camera Follow')
    p.draw(avatarPos, '.-', label='avatar')
    p.draw(followPos3, '.-r', label='delay 3')
    p.draw(followPos5, '.-g', label='delay 5')
    p.draw(followPos10, '.-y', label='delay 10')
    p.show()


def countTimeCost(points, cls):
    start = time.time()
    bc = cls(points)
    curvePoints = []
    for t in xrange(0, 101):
        curvePoints.append(bc.getPointAt(t/100.0))
    # cache = getattr(bc, 'cache', {})
    # print 'cache', len(cache) # cache num is ok, ((1+n)*n)/2 * 101
    return curvePoints, time.time()-start

def compareTwoPlan(points):
    curvePoints, timeNormal = countTimeCost(points, BezierCurve)
    curvePointsImprove, timeImprove = countTimeCost(points, BezierCurveImprove)
    print 'point', len(points), timeNormal, timeImprove, timeNormal/timeImprove
    # print curvePoints, curvePointsImprove

def testPerformance():
    """测试结果：
    point 5 0.00200009346008 0.00399994850159 0.500029802706
    point 10 0.0670001506805 0.0160000324249 4.18750093132
    point 15 2.13499999046 0.0349998474121 61.0002656676
    5阶优化反而降低效率
    10阶提升4倍
    15阶提升6倍

    随着阶数的增加，提升效率越发明显
    """
    points5 = [(1, 1), (0.5, 3), (3, 4), (4, 1), (5, 10)]
    points10 = [(6, 5), (6, 8), (7, 4), (8, 2), (9, 6), (10, 1), (11, 2), (12, 3), (13, 4), (14, 10)]
    compareTwoPlan(points5)
    compareTwoPlan(points10)
    compareTwoPlan(points5 + points10)


if __name__ == '__main__':
    testDegreeN()
    # testCamera()
    # testPerformance()
    pass

