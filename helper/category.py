#!/usr/bin/env python3
#
# This file is part of appimage-store
# Copyright © 2020 yourname
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import re


class Category(object):

    def __init__(self, layout=None, xdg=None, title=None, subtitle=None,
                 image=None):
        """TODO: Docstring for __init__.

        :layout: TODO
        :xdg: TODO
        :title: TODO
        :subtitle: TODO
        :image: TODO
        :returns: TODO

        """
        self._layout = layout
        self._xdg = xdg
        self._title = title
        self._subtitle = subtitle
        self._image = image

    def get_layout(self):
        """TODO: Docstring for get_layout.
        :returns: TODO

        """
        return self._layout

    def set_layout(self, layout):
        """TODO: Docstring for set_layout.

        :layout: TODO
        :returns: TODO

        """
        self._layout = layout

    def get_xdg(self):
        """TODO: Docstring for get_xdg.
        :returns: TODO

        """
        return self._xdg

    def set_xdg(self, xdg):
        """TODO: Docstring for set_xdg.

        :xdg: TODO
        :returns: TODO

        """
        self._xdg = xdg

    def get_title(self):
        """TODO: Docstring for get_title.
        :returns: TODO

        """
        return self._title

    def set_title(self, title):
        """TODO: Docstring for set_title.

        :title: TODO
        :returns: TODO

        """
        self._title = title

    def get_subtitle(self):
        """TODO: Docstring for get_subtitle.
        :returns: TODO

        """
        return self._subtitle

    def set_subtitle(self, subtitle):
        """TODO: Docstring for set_subtitle.

        :subtitle: TODO
        :returns: TODO

        """
        self._subtitle = subtitle

    def get_image(self):
        """TODO: Docstring for get_image.
        :returns: TODO

        """
        return self._image

    def set_image(self, image):
        """TODO: Docstring for set_image.

        :image: TODO
        :returns: TODO

        """
        self._image = image

    @staticmethod
    def parse_string(string):
        """TODO: Docstring for parse_string.

        :string: TODO
        :returns: TODO

        """
        is_info = False
        category = Category()
        for line in string.split('\n'):
            if line.startswith('---'):
                is_info = not is_info
                continue
            if is_info:
                layout = re.match(r'layout:\s+([^\#]*)', line)
                if layout:
                    category.set_layout(layout.groups()[0].strip())
                xdg = re.match(r'xdg:\s+([^\#]*)', line)
                if xdg:
                    category.set_xdg(xdg.groups()[0].strip())
                title = re.match(r'title:\s+([^\#]*)', line)
                if title:
                    category.set_title(title.groups()[0].strip())
                subtitle = re.match(r'subtitle:\s+([^\#]*)', line)
                if subtitle:
                    category.set_subtitle(subtitle.groups()[0].strip())
                image = re.match(r'image:\s+([^\#]*)', line)
                if image:
                    category.set_image(image.groups()[0].strip())
        return category

    def __str__(self):
        """TODO: Docstring for __string__.
        :returns: TODO

        """
        string = 'layout: {}\n'.format(self._layout)
        string += 'xdg: {}\n'.format(self._xdg)
        string += 'title: {}\n'.format(self._title)
        string += 'subtitle: {}\n'.format(self._subtitle)
        string += 'image: {}'.format(self._image)
        return string


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    test_file = os.path.normpath(os.path.join(
        dir_path, '../appimage.github.io/_categories/Audio.md'))
    with open(test_file, 'r') as fr:
        content = fr.read()
        print(content)
        category = Category.parse_string(content)
        print(category)
