# -*- coding:utf-8 -*-


import os
import fileinput


def countFileLines(path, fileTypes, ignoreDirs=[]):
    """统计指定目录下所有文件的总行数
    Args:
        path: 目录
        fileTypes: 需要统计的文件格式，如['.py', '.c', '.java']
        ignoreDirs: 需要忽略的目录名称，如['.git']
        showDetails: 是否显示详细信息，如其中每个文件的行数
    Returns:
        count: 总行数
        details: {filename: count}，每个文件的行数
    """
    count = 0
    details = {}
    for root, dirs, filenames in os.walk(path):
        # print root    # 当前目录
        # print dirs    # 该目录下的子目录
        # print filenames    # 该目录下的文件名

        ignoreFlag = False
        for eachDir in ignoreDirs:
            if root.find(eachDir) >= 0:
                ignoreFlag = True
                break
        if ignoreFlag:
            continue

        for fn in filenames:
            typeFlag = False
            for ft in fileTypes:
                if fn.endswith(ft):
                    typeFlag = True
                    break
            if not typeFlag:
                continue
            f = os.path.join(root, fn)
            for each in fileinput.input(f):
                # print each   #打印每一行内容
                pass
            details[fileinput.filename()] = fileinput.lineno()
            count += fileinput.lineno()

    return count, details



if __name__ == '__main__':
    path = "C:\Users\\username\Desktop\\tt"
    fileTypes = ['.py']
    ignoreDirs = ['.git']

    count, details = countFileLines(path, fileTypes, ignoreDirs)

    print '## line count:', count

    for filename, cnt in details.iteritems():
        print '  ', filename, cnt



