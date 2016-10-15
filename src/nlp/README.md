## Notes 
### term_frequency.py
[machine-learning-text-feature-extraction-tf-idf-part-i](http://blog.christianperone.com/2011/09/machine-learning-text-feature-extraction-tf-idf-part-i/)
这个文件是上边链接的一个实现, 主要使计算term frequency的 

### tf_idf.py 
[machine-learning-text-feature-extraction-tf-idf-part-ii/](http://blog.christianperone.com/2011/10/machine-learning-text-feature-extraction-tf-idf-part-ii/)
这个文件是上边链接的一个实现

LP-space wikipedia上有解释, P代表了向量的维度。而向量是在此链接中则是每个文档中各个term的frequency, eg. `[0 1 1 1]`
L2-norm, L1-norm 分别是公式中P等于2和1的情况下的不同情况。

还需要注意的是当前的sklearn计算idf的公式已经和上边的链接不一样了, 所以程序的结果也会不同










