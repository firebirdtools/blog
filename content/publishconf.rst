publishconf
################################

:date: 2019-01-15
:category: mcss
:tags: Pelican, mcss, re­Struc­tured­Text, git
:summary: publishconf

.. role:: py(code)
    :language: py
.. role:: rst(code)
    :language: rst


`mcss网站 <https://mcss.mosra.cz/>`_

--------------------------------------------------------------------------------

`SITEURL`_
===========

对外发布，则设置url

.. code:: py

    SITEURL = 'https://firebirdtools.github.io/blog'

本地发布，设置为空

https://mcss.mosra.cz/plugins/htmlsanity/#siteurl-formatting

--------------------------------------------------------------------------------

`STATIC_PATHS`_
================

https://docs.getpelican.com/en/3.4.0/settings.html?highlight=static_paths

默认情况下，为 ``STATIC_PATHS = ['images']`` ，但rst文档中采用的是 ``{static}``

故，设置如下：

.. code:: py

    STATIC_PATHS = ['static']

--------------------------------------------------------------------------------

`images`_
================

https://mcss.mosra.cz/plugins/images/#how-to-use

.. code:: py

    PLUGIN_PATHS = ['m.css/pelican-plugins']
    PLUGINS = ['m.htmlsanity', 'm.images']

`:alt:`_
================

https://mcss.mosra.cz/plugins/images/#images-figures

.. code:: py

    M_IMAGES_REQUIRE_ALT_TEXT = True

`math`_
================

https://mcss.mosra.cz/plugins/math-and-code/#math

.. code:: py

    PLUGINS += ['m.htmlsanity', 'm.math']
    M_MATH_RENDER_AS_CODE = False
    M_MATH_CACHE_FILE = 'm.math.cache'

`components`_
================

https://mcss.mosra.cz/plugins/components/#how-to-use

.. code:: py

    PLUGINS += ['m.htmlsanity', 'm.components']


`metadata`_
================

元数据可以进行一些搜索引擎的优化，包含博文的一些基础信息。

https://docs.getpelican.com/en/stable/content.html#file-metadata

https://mcss.mosra.cz/plugins/metadata/#how-to-use

.. code:: rst

    My super title
    ##############

    :date: 2010-10-03 10:20
    :modified: 2010-10-04 18:40
    :tags: thats, awesome
    :category: yeah
    :slug: my-super-post
    :authors: Alexis Metaireau, Conan Doyle
    :summary: Short version for index and feeds

add the new fields to FORMATTED_FIELDS

.. code:: py

    PLUGINS += ['m.metadata']
    FORMATTED_FIELDS += ['description', 'badge']

默认情况下如下所示：

.. code:: py

    M_METADATA_AUTHOR_PATH = 'authors'
    M_METADATA_CATEGORY_PATH = 'categories'
    M_METADATA_TAG_PATH = 'tags'

`blocks-notes-frame`_
======================

    https://mcss.mosra.cz/plugins/components/#blocks-notes-frame

.. code:: py

    PLUGINS += ['m.htmlsanity', 'm.components']

.. code:: rst

    .. block-danger:: Danger block

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ultrices a
        erat eu suscipit. `Link. <#>`_

    .. note-success:: Success note

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ultrices a
        erat eu suscipit. `Link. <#>`_

    .. frame:: Frame

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ultrices a
        erat eu suscipit. `Link. <#>`_


`Col­ors`_
======================

https://mcss.mosra.cz/css/components/#colors

 `col­or a block of text <https://mcss.mosra.cz/css/components/#text>`_

`Code`_
======================

https://mcss.mosra.cz/plugins/math-and-code/#code

http://docutils.sourceforge.net/docs/ref/rst/roles.html#code

https://mcss.mosra.cz/plugins/math-and-code/#code

.. code:: py

    PLUGINS += ['m-htmlsanity', 'm.code']

.. code:: c++
    :hl_lines: 1 2 3 4 5 6
    :class: m-inverted

    #include <iostream>

    int main() {
        std::cout << "Hello world!" << std::endl;
        return 0;
    }
