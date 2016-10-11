from sklearn.feature_extraction.text import CountVectorizer

"""
for more infomation about this module visist:
    http://blog.christianperone.com/2011/09/machine-learning-text-feature-extraction-tf-idf-part-i/

todo:

    vectorizer 的stopwords没有, 但是博文中同样的构造函数生成出的vectorizer是包含stopwords的
"""

def test_fr():
    """ test term frequency in sklearn"""
    train_set = ("The sky is blue.", "The sun is bright.")
    test_set = ("The sun in the sky is bright.",
        "We can see the shining sun, the bright sun.")

    #The CountVectorizer already uses as default “analyzer” called WordNGramAnalyzer,
    #which is responsible to convert the text to lowercase, accents removal, 
    #token extraction, filter stop words,
    vectorizer = CountVectorizer()

    # create  `index vocabulary`
    # 这步主要是处理文本, 移除stop words.然后对剩下的每个term生个一个对应idx, Map[term: String, idx: Int]的键值对
    print("dict_index of train_set is \n ", vectorizer.fit_transform(train_set))
    dict_index = vectorizer.fit_transform(test_set)
    print("dict_index of test_set is \n ", dict_index)
    
    smatrix = vectorizer.transform(test_set)
    print("smatrix.todense of test_set is \n", smatrix.todense())
    """
    should print something like

    matrix([[0, 1, 1, 1],
        ........[0, 2, 1, 0]], dtype=int64)
    """



