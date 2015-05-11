#Overview

**The Tutorial ** which guild how to develop a Blog by Django, It will update with learing.

#Requirements

- Mac OS X 10.10.1  #非必要
- Python3.4.2
- Django1.7.1 
- Bootstrap3.3.0 or Pure  #非必要
- Sublime Text 3  #非必要
- virtualenv  1.11.6


#Install 

```
$ git clone https://github.com/Andrew-liu/my_blog_tutorial

or

$ git clone git@github.com:Andrew-liu/my_blog_tutorial.git
```

#Usage

You can use the example of blog simply, just to do below:

```
$ cd my_blog_tutorial
$ pip install -r requirements.txt  #安装所有依赖
$ python manage.py migrate
$ python manage.py runserver

open the website(chrome best) and input
http://127.0.0.1:8000/

关于在windows环境下依赖项的安装注意项：
1.windows环境下，psycopg2需要安装对应的windows版本
    http://pythonhosted.org//psycopg2/install.html#install-from-a-package
2.django-toolbelt依赖于psycopg和其它的几个包，注意安装顺序
    https://pypi.python.org/pypi/django-toolbelt/0.0.1
```



#More Detail

整个博客开发过程, 已经整理成书, 欢迎阅读

链接为[Django搭建简易博客教程](http://andrew-liu.gitbooks.io/django-blog/content/)

#Done

1. Django-bootstrap-admin优化后台管理, Pure只做前端
2. markdown和代码高亮
3. 多说评论
4. aboutme功能建设完成
5. 标签分类
6. 归档
7. 搜索
8. read more功能
9. RSS功能
10. 分页功能

#TO DO



#License

Copyright (c) 2014 [Andrew Liu](http://andrewliu.tk)

Licensed under the MIT License

