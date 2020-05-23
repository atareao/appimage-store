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

class Application(object):

    def __init__(self, layout=None, name=None, description=None, icon=None,
                 screenshot=None, link=None, author=None, author_link=None,
                 download_link=None):
        """

        :layout: TODO
        :name: TODO
        :description: TODO
        :icon: TODO
        :screenshot: TODO
        :link: TODO
        :author: TODO
        :author_link: TODO
        :download_link: TODO
        :returns: TODO

        """
        self._layout = layout
        self._name = name
        self._description = description
        self._icon = icon
        self._screenshot = screenshot
        self._link = link
        self._author = author
        self._author_link = author_link
        self._download_link = download_link

    def get_layout(self):
        """TODO: Docstring for get_layout.
        :returns: layoout

        """
        return self._layout

    def set_layout(self, layout):
        """TODO: Docstring for set_layout.

        :layout: TODO

        """
        self._layout = layout

    def get_description(self):
        """TODO: Docstring for get_description.
        :returns: description

        """
        return self._description

    def set_description(self, description):
        """TODO: Docstring for set_description.

        :description: TODO

        """
        self._description = description

    def get_icon(self):
        """TODO: Docstring for get_icon.
        :returns: TODO

        """
        return self._icon

    def set_icon(self, icon):
        """TODO: Docstring for set_icon.

        :icon: TODO

        """
        self._icon = icon

    def get_screenshot(self):
        """TODO: Docstring for get_screenshot.
        :returns: TODO

        """
        return self._screenshot

    def set_screenshot(self, screenshot):
        """TODO: Docstring for set_screenshot.

        :screenshot: TODO

        """
        self._screenshot = screenshot

    def get_link(self):
        """TODO: Docstring for get_link.
        :returns: TODO

        """
        return self._link

    def set_link(self, link):
        """TODO: Docstring for set_link.

        :link: TODO
        :returns: TODO

        """
        self._link = link

    def get_author(self):
        """TODO: Docstring for get_author.
        :returns: TODO

        """
        return self._author

    def set_author(self, author):
        """TODO: Docstring for set_author.

        :author: TODO
        :returns: TODO

        """
        self._author = author

    def get_author(self):
        """TODO: Docstring for get_author.
        :returns: TODO

        """
        return self._author

    def set_author_link(self, author_link):
        """TODO: Docstring for set_author_link.

        :author_link: TODO
        :returns: TODO

        """
        self._author_link = author_link

    def get_download_link(self):
        """TODO: Docstring for get_download_link.
        :returns: TODO

        """
        return self._download_link

    def set_download_link(self, download_link):
        """TODO: Docstring for set_download_link.

        :download_link: TODO
        :returns: TODO

        """
        self._download_link = download_link
