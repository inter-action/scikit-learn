* [A super simple introduction to neural networks](http://www.mattzeunert.com/2016/12/09/neural-networks-super-simple-introduction.html)
这篇文章介绍了神经网络学习的一个基础介绍，简单的介绍了神经元和Layer的概念。和JS实现的一个简单的
对数字是否是偶数的一个判断的一个神经网络程序。

首先需要注意的是，输入的向量是16个长度的二进制数，总共有2^16-1次可能，在此实例中代表[0, 2^16 - 1]
范围的数字。

虽然代码中是以数组计算的，但是实际中，用向量理解更容易。而且实际中也是向量在处理。
代码中 exampleIsPredictedCorrectly 方法正确性的公式还是不能理解。文中对这一部分的解释似乎很随意，
貌似是说为了解释最终的神经网络结果，随便定义了一个如果大于0.5就认为是偶数。然后根据这个假设去训练神经网络。

文中, 各个layer的权重完全没有目的的随机出来的。实际中应该是有数学公式，或者是梯度下降来做这一部分的计算应该。
梯度下降具体看Andrew NG的教学视频吧

https://www.youtube.com/watch?v=fdxgFsBaHWU&list=PLJ1-ciQ35nuiyL1PX6O4NdF5CjjaDdnVC&index=18


扩展阅读:
* [Book: Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/index.html)