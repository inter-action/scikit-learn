from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

"""
这个文件是 tf-idf 的实现, tf(term frequency), idf(inverse document frequency)
这个函数的功能就是如何将文档中的term normalize。将文档中大量重复的单词的权重降低的一种方式。
这里的代码是来自下面这个链接, 稍有改动, 适应python3和最新的sklearn版本，链接中有详细的解释:
http://blog.christianperone.com/2011/10/machine-learning-text-feature-extraction-tf-idf-part-ii/

最新的sklearn同样的api已经和链接返回不同结果了, 是sklearn里边idf生成的算法变了。
这个没办法了.... :(
"""
def run():
    train_set = ("The sky is blue.", "The sun is bright.")
    test_set = ("The sun in the sky is bright.",
    "We can see the shining sun, the bright sun.")
    count_vectorizer = CountVectorizer(stop_words="english")
    count_vectorizer.fit_transform(train_set)
    print("Vocabulary:", count_vectorizer.vocabulary_)
    # Vocabulary: {'blue': 0, 'sun': 1, 'bright': 2, 'sky': 3}
    freq_term_matrix = count_vectorizer.transform(test_set)
    print("freq_term_matrix.todense():\n", freq_term_matrix.todense())
    #[[0 1 1 1]
    #[0 2 1 0]]

    tfidf = TfidfTransformer(norm='l2', smooth_idf=False)
    tfidf.fit(freq_term_matrix)
    print("IDF:", tfidf.idf_)

    tf_idf_matrix = tfidf.transform(freq_term_matrix)
    print("\ntf_idf_matrix.todense():\n", tf_idf_matrix.todense())
    # [[ 0.         -0.70710678 -0.70710678  0.        ]
    # [ 0.         -0.89442719 -0.4472136   0.        ]]