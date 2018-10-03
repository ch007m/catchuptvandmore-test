# -*- coding: utf-8 -*-
import sys
import mock


class FakeListItem(object):
    def __init__(self, label="", label2="", iconImage="", thumbnailImage="", path=""):
        self._label = label
        self._label2 = label2
        self._iconImage = iconImage
        self._thumbnailImage = thumbnailImage
        self._path = path
        self._property = {}
        self._info = {}
        self._art = {}
        self._actors = {}
        self._stream = {}
        self._context_menu = []

    def getLabel(self):
        return self._label

    def setLabel(self, label):
        self._label = label

    def getLabel2(self):
        return self._label2

    def setLabel2(self, label):
        self._label2 = label

    def getPath(self):
        return self._path

    def setPath(self, path):
        self._path = path

    def setArt(self, art):
        self._art = art

    def getArt(self, key):
        return self._art.get(key, '')

    def setInfo(self, ctype, infoLabels):
        self._info[ctype] = infoLabels

    def setCast(self, actors):
        self._actors = actors

    def addStreamInfo(self, cType, dictionary):
        self._stream[cType] = dictionary

    def setProperty(self, key, value):
        self._property[key] = value

    def getProperty(self, key):
        return self._property.get(key, '')

    def addContextMenuItems(self, items, replaceItems=False):
        self._context_menu = items




mock_xbmcgui = mock.MagicMock()
mock_xbmcgui.ListItem.side_effect = FakeListItem

# Say to Python that the xbmcgui module is mock_xbmcgui
sys.modules['xbmcgui'] = mock_xbmcgui
