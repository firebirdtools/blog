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
