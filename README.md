# EMD
经验模式分解
经验模态分解（Empirical Mode Decomposition，缩写EMD）是一种新型自适应信号时频处理方法，特别适用于非线性非平稳信号的分析处理。
内涵模态分量（Intrinsic Mode Functions, IMF）就是原始信号被EMD分解之后得到的各层信号分量。EMD的提出人黄锷认为，任何信号都可以拆分成若干个内涵模态分量之和。而内涵模态分量有两个约束条件：

1）在整个数据段内，极值点的个数和过零点的个数必须相等或相差最多不能超过一个。

2）在任意时刻，由局部极大值点形成的上包络线和由局部极小值点形成的下包络线的平均值为零，即上、下包络线相对于时间轴局部对称。

EMD的分解过程是简单直观的：

1）根据原始信号上下极值点，分别画出上、下包络线。

2）求上、下包络线的均值，画出均值包络线。

3）原始信号减均值包络线，得到中间信号。

4）判断该中间信号是否满足IMF的两个条件，如果满足，该信号就是一个IMF分量；如果不是，以该信号为基础，重新做1）~4）的分析。IMF分量的获取通常需要若干次的迭代。


EMD另一个包PyEMD安装方式，包的官方介绍：https://pypi.org/project/EMD-signal/0.2.7/
因为存在pyemd包计算词之间的距离，而这个包名字只是大小写不同，pip安装时不区分大小写，因此安装PyEMD时应该使用指令pip install EMD-signal。如果之前安装了pyemd,则需要删除pyemd，指令pip uninstall pyemd.
Example：https://pyemd.readthedocs.io/en/latest/examples.html
