# coding:utf-8
# Author:  mmoosstt -- github
# Purpose: data types used within XmlXdiff
# Created: 01.01.2019
# Copyright (C) 2019, diponaut@gmx.de
# License: TBD


from inspect import isclass
from svgwrite import rgb


class XElement(object):

    def __init__(self):
        self.hash = None
        self.xpath = None
        self.type = None
        self.node = None
        self.svg_node = None
        self.xelements = []

    def addSvgNode(self, inp):
        self.svg_node = inp

    def addXelement(self, xelement):
        self.xelements.append(xelement)

    def setNode(self, inp):
        self.node = inp

    def setType(self, inp):
        if isclass(inp):
            self.type = inp()
        else:
            self.type = inp

    def setXpath(self, inp):
        self.xpath = inp

    def setHash(self, inp):
        self.hash = inp


class XType(object):

    opacity = 0.3

    @classmethod
    def name(cls):
        return cls.__name__.replace("Element", "")


class ElementUnknown(XType):
    fill = rgb(0xd0, 0xd0, 0xd0)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementUnchanged(XType):
    fill = rgb(0x7e, 0x62, 0xa1)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementChanged(XType):
    fill = rgb(0xff, 0x00, 0x80)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementDeleted(XType):
    fill = rgb(0xff, 0x00, 0xff)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementAdded(XType):
    fill = rgb(0x0f, 0xff, 0x00)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementVerified(XType):
    fill = rgb(0xff, 0xff, 0x00)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementMoved(XType):
    fill = rgb(0x1e, 0x2d, 0xd2)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementTagConsitency(XType):
    fill = rgb(0x00, 0xa0, 0x70)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementTextAttributeValueConsitency(XType):
    fill = rgb(0x00, 0x70, 0xa0)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementTagAttributeNameConsitency(XType):
    fill = rgb(0x00, 0xd0, 0xe0)

    def __init__(self):
        super(self.__class__, self).__init__()


class ElementTagAttributeNameValueConsitency(XType):
    fill = rgb(0x00, 0xa0, 0xf0)

    def __init__(self):
        super(self.__class__, self).__init__()


def LOOP_GRAVITY(elements, gravity_index=0, *element_types):

    for _element in elements[gravity_index:]:
        if isinstance(_element.type, element_types):
            yield _element

    for _element in elements[:gravity_index]:
        if isinstance(_element.type, element_types):
            yield _element


def LOOP(elements, *element_types):

    # try to match shortest paths first - identification of biggest blocks
    # /root
    # /node1
    # /node1/node2
    # ...

    _append = []
    for _element in elements:
        if isinstance(_element.type, element_types):
            _append.append((len(_element.xpath), _element.xpath, _element))

    for _, _, _element in sorted(_append):
        if isinstance(_element.type, element_types):
            yield _element


def LOOP_XTYPES():
    for _xtype in XType.__subclasses__():
        yield _xtype
