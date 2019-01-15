..
    This file is part of m.css.

    Copyright © 2017, 2018, 2019 Vladimír Vondruš <mosra@centrum.cz>

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
..

Test Math
############

:date: 2019-01-15
:category: mcss
:tags: Pelican, mcss, re­Struc­tured­Text, git
:summary: Math

..
  :save_as: plugins/math-and-code/test/index.html
  :breadcrumb: {filename}/plugins.rst Pelican plugins
               {filename}/plugins/math-and-code.rst Math and code
..

Math
====

First is colored except :math:`c^2`, second is colored globally, third is
colored globally with overrides except for :math:`c^2`.

.. container:: m-row

    .. container:: m-col-m-4

        .. math::

            {\color{m-default} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-default

            a^2 + b^2 = c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-danger

            {\color{m-default} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::

            {\color{m-primary} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-primary

            a^2 + b^2 = c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-danger

            {\color{m-primary} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::

            {\color{m-success} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-success

            a^2 + b^2 = c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-danger

            {\color{m-success} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::

            {\color{m-warning} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-warning

            a^2 + b^2 = c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-danger

            {\color{m-warning} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::

            {\color{m-danger} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-danger

            a^2 + b^2 = c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-success

            {\color{m-danger} a^2 + b^2 =} ~ c^2

.. container:: m-row

    .. container:: m-col-m-4

        .. math::

            {\color{m-info} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-info

            a^2 + b^2 = c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-danger

            {\color{m-info} a^2 + b^2 =} ~ c^2

.. container:: m-row

    .. container:: m-col-m-4

        .. math::

            {\color{m-dim} a^2 + b^2 =} ~ c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-dim

            a^2 + b^2 = c^2

    .. container:: m-col-m-4

        .. math::
            :class: m-danger

            {\color{m-dim} a^2 + b^2 =} ~ c^2



.. math::
    :class: m-success

    \boldsymbol{A} = \begin{pmatrix}
        \frac{2n}{s_x} & 0 & 0 & 0 \\
        0 & \frac{2n}{s_y} & 0 & 0 \\
        0 & 0 & \frac{n + f}{n - f} & \frac{2nf}{n - f} \\
        0 & 0 & -1 & 0
    \end{pmatrix}

.. math-figure:: Infinite projection matrix

    .. math::
        :class: m-success

        \boldsymbol{A} = \begin{pmatrix}
            \frac{2n}{s_x} & 0 & 0 & 0 \\
            0 & \frac{2n}{s_y} & 0 & 0 \\
            0 & 0 & -1 & -2n \\
            0 & 0 & -1 & 0
        \end{pmatrix}

    With :math:`f = \infty`.
