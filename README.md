# About this Repo
考虑到好久没有使用过Python了, 最近一直对机器学习很有兴趣, 所以python这一关是我是要重新开始了。
这个Repo会作为我当前python状态的锚点和跳板。

这个项目是如何开始的:
我的另一个项目document-indexer, 我想加下计算文档相似度&cluster的功能。所以搜索了些链接。就是这个
[Machine Learning :: Cosine Similarity for Vector Space Models (Part III)](http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/) 
但这个博文是3部曲的,(BTW, this guy's blog has very high quality!),诺，看了第一篇,
就手痒想搞下。这个项目就诞生了。

这个项目的未来方向:
这个项目未来会存放任何和sklearn相关机器学习的代码。会当做以后的练习和参考。



# Project Settings Up

## Preliminaries:
install virtualenv, pip, ipython !


## 
* install ipython # REPL 很重要！
* setting up pyvenv, & activate it, 之所以不用virtualenv是因为和matplotlib有兼容性问题, 而且pyvenv是自带的

        pyvenv .env
        source .env/bin/activate  
        deactivate  # deactivate virtualenv
    
* install dependencies:

        # all installations goes to `./.env/lib/python3.5/site-packages`
        touch requirements.txt
        pip install NumPy
        pip install SciPy
        pip install -U scikit-learn

* working with pip:

        pip freeze > requirements.txt #freeze dependencies



* setting up Makefile
    
    http://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html
    https://gist.github.com/bsmith89/c6811893c1cbd2a72cc1d144a197bef2


## with Makefile:

    make run-main       # run this project.


## with vscode:
https://code.visualstudio.com/docs/languages/python

## with ipython
先activate virtualenv, then `>ipython`

    ctrl + l  #clear screen
    
    # --- auto reload module:
    # http://stackoverflow.com/questions/5364050/reloading-submodules-in-ipython

    %load_ext autoreload
    %autoreload 2

    # add auto reload permanently
    ipython profile create

    # appending following content to `~/.ipython/profile_default/ipython_config.py`
    c.InteractiveShellApp.extensions = ['autoreload']     
    c.InteractiveShellApp.exec_lines = ['%autoreload 2']

    


# Python3 language:
### python3 module system - https://docs.python.org/3/tutorial/modules.html

    dir()               # print out what available in this module
    import builtins     # see what inside builtins
    

Exceptions - https://docs.python.org/3/tutorial/errors.html


### import:

    from driver import chrome_driver as mydriver # absolute import

    from ..driver import chrome_driver as mydriver # relative import

        - driver
            - chrome_driver
        - crawler
            - web_crawler.py # 这个file引用chrome_driver
        main.py # 这种情况下relative import是非法的.
            http://stackoverflow.com/questions/33837717/systemerror-parent-module-not-loaded-cannot-perform-relative-import
                Note that relative imports are based on the name of the current module. 
                Since the name of the main module is always "__main__", modules intended for use as 
                the main module of a Python application must always use absolute imports.

### string format:
    https://pyformat.info/

### is vs ==
http://stackoverflow.com/questions/2988017/string-comparison-in-python-is-vs

> You use == when comparing values and is when comparing identities.


# Links

* [sklearn working with text example](http://scikit-learn.sourceforge.net/stable/auto_examples/index.html#working-with-text-documents)




## todos:

    done: 
        test using ipython with virtualenv activated

    pending:
        add a linter
        add flask, add restful webservices, 如果是练习的目的话，这个应该不需要了，再看
        add docker, then config Makefile again.
        ! learning more about ipython
        string format - http://www.python-course.eu/python3_formatted_output.php
        find a better way to handle __pycache__, generate it in non-src folder
        add python unit test

        





























