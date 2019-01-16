mcss-pelican-git blog full
################################

:date: 2019-01-15
:category: mcss
:tags: Pelican, mcss, re­Struc­tured­Text, git
:summary: 完整过程

.. role:: py(code)
    :language: py
.. role:: rst(code)
    :language: rst


`mcss网站 <https://mcss.mosra.cz/>`_

--------------------------------------------------------------------------------

`GitHub`_
===========

1. New repository

.. image:: {static}/static/0_new_repository.png
    :target: {static}/static/0_new_repository.png

2. blog name

.. image:: {static}/static/01_blog_name.png
    :target: {static}/static/01_blog_name.png

3. create repository

.. image:: {static}/static/02_create.png
    :target: {static}/static/02_create.png

--------------------------------------------------------------------------------

`test git`_
===========

.. code:: sh

    echo "# blog" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/firebirdtools/blog.git
    git push -u origin master

`sample code 1`_
--------------------

执行如下命令后，再刷新浏览器上的blog网页，如我的是：https://github.com/firebirdtools/blog

.. image:: {static}/static/03_test_blog.png
    :target: {static}/static/03_test_blog.png

.. code:: sh

    firebird@tools:~/github$ mkdir blog && cd blog
    firebird@tools:~/github/blog$ echo "# blog" >>README.md
    firebird@tools:~/github/blog$ git init
    已初始化空的 Git 仓库于 /home/firebird/github/blog/.git/
    firebird@tools:~/github/blog$ git add README.md
    firebird@tools:~/github/blog$ git commit -m "first commit"
    [master（根提交） 384328f] first commit
     1 file changed, 1 insertion(+)
     create mode 100644 README.md
    firebird@tools:~/github/blog$ git remote add origin https://github.com/firebirdtools/blog.git
    firebird@tools:~/github/blog$ git push -u origin master
    Username for 'https://github.com': firebirdtools
    Password for 'https://firebirdtools@github.com':
    对象计数中: 3, 完成.
    写入对象中: 100% (3/3), 219 bytes | 219.00 KiB/s, 完成.
    Total 3 (delta 0), reused 0 (delta 0)
    To https://github.com/firebirdtools/blog.git
     * [new branch]      master -> master
    分支 'master' 设置为跟踪来自 'origin' 的远程分支 'master'。
    firebird@tools:~/github/blog$

--------------------------------------------------------------------------------

`pelican-quickstart 初始化`_
============================

`sample code 2`_
--------------------

.. text-info::
    :class: m-note m-success

    + 通过 ``pelican-quickstart`` 会自动生成相关目录和文件
    + 使用 ``tree``  命令，可显示示例中的文件；若没有，则安装 ``sudo apt-get install tree``


.. code:: sh

    firebird@tools:~/github/blog$ pelican-quickstart
    Welcome to pelican-quickstart v4.0.1.

    This script will help you create a new Pelican-based website.

    Please answer the following questions so this script can generate the files
    needed by Pelican.


    > Where do you want to create your new web site? [.]
    > What will be the title of this web site? blog
    > Who will be the author of this web site? firebird
    > What will be the default language of this web site? [zh] en
    > Do you want to specify a URL prefix? e.g., https://example.com   (Y/n) n
    > Do you want to enable article pagination? (Y/n)
    > How many articles per page do you want? [10]
    > What is your time zone? [Europe/Paris]
    > Do you want to generate a tasks.py/Makefile to automate generation and publishing? (Y/n)
    > Do you want to upload your website using FTP? (y/N)
    > Do you want to upload your website using SSH? (y/N)
    > Do you want to upload your website using Dropbox? (y/N)
    > Do you want to upload your website using S3? (y/N)
    > Do you want to upload your website using Rackspace Cloud Files? (y/N)
    > Do you want to upload your website using GitHub Pages? (y/N)
    Done. Your new project is available at /home/firebird/github/blog
    firebird@tools:~/github/blog$ tree
    .
    ├── content
    ├── Makefile
    ├── output
    ├── pelicanconf.py
    ├── publishconf.py
    ├── README.md
    └── tasks.py

    2 directories, 5 files
    firebird@tools:~/github/blog$

--------------------------------------------------------------------------------

`m.css`_
======================

1. 在项目中，安装m.css，以便引用

.. code:: sh

    git submodule add git://github.com/mosra/m.css

2. 打开 ``publishconf.py`` ，添加如下代码

.. code:: py

    THEME = 'm.css/pelican-theme'
    THEME_STATIC_DIR = 'static'
    DIRECT_TEMPLATES = ['index']

    M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
                   '/static/m-dark.css']
    M_THEME_COLOR = '#22272e'

    PLUGIN_PATHS = ['m.css/pelican-plugins']
    PLUGINS = ['m.htmlsanity']

`sample code 3`_
--------------------

.. code:: sh

    firebird@tools:~/github/blog$ git submodule add git://github.com/mosra/m.css
    正克隆到 '/home/firebird/github/blog/m.css'...
    remote: Enumerating objects: 566, done.
    remote: Counting objects: 100% (566/566), done.
    remote: Compressing objects: 100% (331/331), done.
    remote: Total 8828 (delta 359), reused 357 (delta 231), pack-reused 8262
    接收对象中: 100% (8828/8828), 3.04 MiB | 49.00 KiB/s, 完成.
    处理 delta 中: 100% (6328/6328), 完成.
    firebird@tools:~/github/blog$

publishconf.py文件添加后内容

.. code:: py

    #!/usr/bin/env python
    # -*- coding: utf-8 -*- #
    from __future__ import unicode_literals

    # This file is only used if you use `make publish` or
    # explicitly specify it as your config file.

    import os
    import sys
    sys.path.append(os.curdir)
    from pelicanconf import *

    # If your site is available via HTTPS, make sure SITEURL begins with https://
    SITEURL = ''
    RELATIVE_URLS = False

    FEED_ALL_ATOM = 'feeds/all.atom.xml'
    CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

    DELETE_OUTPUT_DIRECTORY = True

    # Following items are often useful when publishing

    #DISQUS_SITENAME = ""
    #GOOGLE_ANALYTICS = ""


    # ================================================================ #
    # add m.css-theme
    THEME = 'm.css/pelican-theme'
    THEME_STATIC_DIR = 'static'
    DIRECT_TEMPLATES = ['index']

    M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
                    '/static/m-dark.css']
    M_THEME_COLOR = '#22272e'

    PLUGIN_PATHS = ['m.css/pelican-plugins']
    PLUGINS = ['m.htmlsanity']
    # ================================================================ #

--------------------------------------------------------------------------------

`本地预览`_
======================

1. 编辑好的rst文件放置于 ``content\`` 文件夹

rst示例代码

.. code:: rst

    mcss-pelican-git blog full
    ################################

    :date: 2019-01-15
    :category: mcss
    :tags: Pelican, mcss, re­Struc­tured­Text, git
    :summary: 完整过程

    `mcss网站 <https://mcss.mosra.cz/>`_

2. 本地预览，运行如下命令

.. code:: sh

    pelican content -s publishconf.py
    cd output
    python3 -m http.server

访问 http://localhost:8000 ，即可预览到带主题的网页。

输入： ``ctrl + c`` 停止服务

`sample code 4`_
--------------------

.. code:: sh

    firebird@tools:~/github/blog$ pelican content -s publishconf.py
    WARNING: Feeds generated without SITEURL set properly may not be valid
    Done: Processed 1 article, 0 drafts, 0 pages, 0 hidden pages and 0 draft pages in 0.33 seconds.
    firebird@tools:~/github/blog$ cd output
    firebird@tools:~/github/blog/output$ python3 -m http.server
    Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

--------------------------------------------------------------------------------

`发布到github`_
=============================

`修改publishconf.py`_
------------------------------

``publishconf.py`` 文件更改两处：

.. code:: py

    SITEURL = 'https://firebirdtools.github.io/blog'
    M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
                   'https://firebirdtools.github.io/blog/static/m-dark.css']

文件更改后内容：

.. code:: py

   #!/usr/bin/env python
   # -*- coding: utf-8 -*- #
   from __future__ import unicode_literals

   # This file is only used if you use `make publish` or
   # explicitly specify it as your config file.

   import os
   import sys
   sys.path.append(os.curdir)
   from pelicanconf import *

   # If your site is available via HTTPS, make sure SITEURL begins with https://
   SITEURL = 'https://firebirdtools.github.io/blog'
   RELATIVE_URLS = False

   FEED_ALL_ATOM = 'feeds/all.atom.xml'
   CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

   DELETE_OUTPUT_DIRECTORY = True

   # Following items are often useful when publishing

   #DISQUS_SITENAME = ""
   #GOOGLE_ANALYTICS = ""

   # ================================================================ #
   # add m.css-theme
   THEME = 'm.css/pelican-theme'
   THEME_STATIC_DIR = 'static'
   DIRECT_TEMPLATES = ['index']

   M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
                  'https://firebirdtools.github.io/blog/static/m-dark.css']
   M_THEME_COLOR = '#22272e'

   PLUGIN_PATHS = ['m.css/pelican-plugins']
   PLUGINS = ['m.htmlsanity']
   # ================================================================ #


`发布于gh-pages分支`_
----------------------------------------

执行 ``pip3 install ghp-import`` ，ghp-import作用是将目录复制到存储库的gh-pages分支。

.. code:: sh

    firebird@tools:~/github/blog$ pelican content -s publishconf.py
    Done: Processed 1 article, 0 drafts, 0 pages, 0 hidden pages and 0 draft pages in 0.32 seconds.
    firebird@tools:~/github/blog$ git add .
    firebird@tools:~/github/blog$ git commit -m "first blog"
    [master 8e133df] first blog
     31 files changed, 10283 insertions(+)
    ...
    firebird@tools:~/github/blog$ git push -u origin master
    Username for 'https://github.com': firebirdtools
    Password for 'https://firebirdtools@github.com':
    对象计数中: 40, 完成.
    Delta compression using up to 4 threads.
    压缩对象中: 100% (38/38), 完成.
    写入对象中: 100% (40/40), 48.59 KiB | 4.05 MiB/s, 完成.
    Total 40 (delta 12), reused 0 (delta 0)
    remote: Resolving deltas: 100% (12/12), done.
    To https://github.com/firebirdtools/blog.git
       384328f..8e133df  master -> master
    分支 'master' 设置为跟踪来自 'origin' 的远程分支 'master'。
    firebird@tools:~/github/blog$ ghp-import output -b gh-pages
    firebird@tools:~/github/blog$ git push origin gh-pages
    Username for 'https://github.com': firebirdtools
    Password for 'https://firebirdtools@github.com':
    对象计数中: 7, 完成.
    Delta compression using up to 4 threads.
    压缩对象中: 100% (7/7), 完成.
    写入对象中: 100% (7/7), 1.30 KiB | 1.30 MiB/s, 完成.
    Total 7 (delta 4), reused 0 (delta 0)
    remote: Resolving deltas: 100% (4/4), completed with 3 local objects.
    To https://github.com/firebirdtools/blog.git
       7299d46..d732a02  gh-pages -> gh-pages
    firebird@tools:~/github/blog$



打开https://firebirdtools.github.io/blog，可看到带主题的网页


`修改publishconf.py 2`_
------------------------------

实际只需设置STATIC_PATHS，就不用在其他地方添加网址了。

.. code:: py

    SITEURL = 'https://firebirdtools.github.io/blog'
    M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
                   'static/m-dark.css']
    STATIC_PATHS = ['static']


.. code:: sh

    pelican content -s publishconf.py
    git add .
    git commit -m "first blog"
    git push -u origin master
    ghp-import output -b gh-pages
    git push origin gh-pages
