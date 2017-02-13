# Bezier Curve

## 背景
接触贝塞尔曲线是因为2015年入职培训期间的一个项目，当时做一个小游戏，由于玩家技能会突进、瞬移等，为避免相机抖动，所以需要镜头平滑的跟随玩家，旁边的大哥告诉我试试贝塞尔曲线。

## 游戏中的表现
- 采用延后N帧跟随的方式
- 能有效避免相机抖动，实现平滑移动
- 贝塞尔曲线随着阶数的增大，计算时间倍数增加
- 实际测试延后5-10帧跟随玩家效果比较好，超过10帧可能会出现
    - 相机跟随迟缓
    - 计算耗时，出现卡帧
 

## BezierCurve.py 说明
1. 实现贝塞尔曲线
2. 支持随意阶数
3. 点支持多维
4. 相机跟随示例
5. 测试用例，并画图对比结果

![贝塞尔曲线各阶对比](https://github.com/tanchao90/evolution/raw/master/code-lib/BezierCurve/BezierCurve-N.png)
![镜头跟随效果](https://github.com/tanchao90/evolution/raw/master/code-lib/BezierCurve/BezierCurve-Camera.png)

## Reference
- [贝塞尔曲线 总结](http://blog.csdn.net/guo_hongjun1611/article/details/7842110)
- [Wiki Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
- [Matplotlib 教程](http://liam0205.me/2014/09/11/matplotlib-tutorial-zh-cn/)
- [Screenshots Examples](http://matplotlib.org/users/screenshots.html)


