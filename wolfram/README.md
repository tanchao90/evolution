
### 文章背景
最近阅读 **待字闺中** 订阅号中的一个文章，看到了作者计算五角星的一段代码，然后搜索了一下发现是 **Mathematica** 

[【果壳网专访】斯蒂芬·沃尔夫勒姆：宇宙的本质是计算](http://www.guokr.com/article/439770/#rd)
> 斯蒂芬·沃尔夫勒姆这个名字，在中文世界里可能远谈不上家喻户晓；但他的英文名Stephen Wolfram恐怕反而却要熟悉得多。大名鼎鼎的数学软件Mathematica每次启动的时候都会用大红字提醒你这是Wolfram出品；而“计算知识引擎” WolframAlpha更是每一个极客必备的网站。

感觉很强大，就下载了 Wolfram Mathematica 的桌面软件体验了一下，本文的主要目的是：
- 了解 **Wolfram**
- 通过 **Mathematica** 验证一下五角星问题
- 用 **Mathematica** 尝试了一些例子

### 安装
- [Wolfram官网](http://wolfram.com/) PS：网站效果比较绚丽，但是访问速度有点不给力。
- 下载：官方下载 or [点击这里](http://pan.baidu.com/s/1i4VBCWX)
- 安装
	- [在 Windows 上安装 Wolfram 系统(官网)](http://support.wolfram.com/kb/12440)
	- [常用数学软件：如何激活Mathematica 9](http://jingyan.baidu.com/article/1876c852b44b8a890b1376ef.html)


### Wolfram的用处
[Wolfram官网](http://wolfram.com/)上列举了一大堆，包括工程研发，教育，网页和软件，金融、统计与商业分析，科学，趋势几个大的方面，通过个人的简单体验，感觉确实挺方便的，通过简单的语句就能绘制出复杂的图形，至少在辅助工作方面还挺有用的，比如下面的简单例子：
- 绘制一个交互式界面，动态调整三角函数曲线的周期
	- `Manipulate[Plot[Sin[a x], {x, 0, 10}], {a, 1, 5}]`
	- ![三角函数曲线](https://github.com/tanchao90/evolution/tree/master/wolfram/res/image_1.png)
- 绘制一个折线图
	- `ListLinePlot[{5, 6, 1, 5, 7, 8, 1, 31}]`
	- ![折线图](https://github.com/tanchao90/evolution/tree/master/wolfram/res/image_2.png)

**Wolfram官网** 提供了比较详细的资料，有兴趣的完全可以通过官网资料入门。

下面是知乎上的部分问答，大家也可以自己搜索
[Mathematica 到底有多厉害？](https://www.zhihu.com/question/27834147)
[Mathematica 这门语言怎么样？](https://www.zhihu.com/question/20324243)
[Wolfram Language 的发布有何意义？](https://www.zhihu.com/question/22860404)

### 用 **Mathematica** 验证五角星问题
关于题目可以阅读下面的连接：
[［面试题及其解答］五角星的纠缠](http://chuansong.me/n/2752733)
[五角星 github](https://github.com/tanchao90/daiziguizhong/tree/master/pentagram)

通过 **Mathematica** 图（Graph）语法可以方便的绘制出多边形，下面是绘制五角星图案的代码和对应图案（PS：图案是自己在 **Mathematica** 软件中运行代码生成的）：
```
Graph[{1 <-> 2, 2 <-> 3, 3 <-> 4, 4 <-> 5, 5 <-> 6, 6 <-> 7, 7 <-> 8, 8 <-> 2, 2 <-> 9, 9 <-> 3, 3 <-> 5, 5 <-> 10, 10 <-> 6, 6 <-> 8, 8 <-> 1}, VertexLabels -> "Name"]
```
![五角星](https://github.com/tanchao90/evolution/tree/master/wolfram/res/image_3.png)

下面的语句是用给定的序列生成所有的全排列，并且选出满足条件的序列：
```
Select[**Permutations@Range[10]**, #[[9]] + #[[3]] + #[[5]] + #[[10]] == #[[10]] + #[[6]] + #[[8]] + #[[1]] == #[[1]] + #[[2]] + #[[3]] + #[[4]] == #[[4]] + #[[5]] + #[[6]] + #[[7]] == #[[7]] + #[[8]] + #[[2]] + #[[9]] &]
```

第一部分 **Permutations@Range[10]** 用于生成1-10十个数字的全排列，也可以自定义序列生成全排列：
- Permutations[{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}]，作用同上
- Permutations[{1, 2, 3, 4, 5, 6, 8, 9, 10, 12}]
- Permutations[{1, 2, 3, 4, 5, 6, 7, 7, 7, 8}]

第二部分的等式用于指定 **SELECT** 的条件，本例中用于计算五角星五条边上四个圈的和，使其五条边的和相等；
其中的数字代表每个全排列中的十个数字，从第一个到第十个，将其对应到上面的五角星图案中，等式刚好是五条边的和。
最终的结果是[1,2,3,4,5,6,7,8,9,10]序列无解；[1,2,3,4,5,6,7,7,7,8]和[1,2,3,4,5,6,8,9,10,12] 序列各有24种不同的结果。
下图是[1,2,3,4,5,6,8,9,10,12]序列解之一，其每边和为24：
!(五角星有解序列)[https://github.com/tanchao90/evolution/tree/master/wolfram/res/image_4.png]

### 总结
通过五角星这个题目接触Wolfram，顺便了解了一下，在此小记，以后有需要的时候再深入学习。
