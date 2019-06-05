import time
import unittest
import inspect
from xmldiff import main, formatting

from xml_xdiff import getPath

import lxml.etree

XSLT = '''
<xsl:stylesheet version="1.0" xmlns:diff="http://namespaces.shoobx.com/diff" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="@diff:insert-formatting">
        <xsl:attribute name="class">
            <xsl:value-of select="'insert-formatting'"/>
        </xsl:attribute>
    </xsl:template>
    
    <xsl:template match="diff:delete">
        <del><xsl:apply-templates /></del>
    </xsl:template>
    
    <xsl:template match="diff:insert">
        <ins><xsl:apply-templates /></ins>
    </xsl:template>
    
    <xsl:template match="@*| node()">
        <xsl:copy>
        <xsl:apply-templates select="@*| node()"/>
        </xsl:copy>
    </xsl:template>
</xsl:stylesheet>
'''


XSLT_TEMPLATE = lxml.etree.fromstring(XSLT)


class HTMLFormatter(formatting.XMLFormatter):
    def render(self, result):
        transform = lxml.etree.XSLT(XSLT_TEMPLATE)
        result = transform(result)
        return super(HTMLFormatter, self).render(result)


class UnSorted(unittest.TestCase):

    path1 = "{}\\..\\..\\tests\\test9\\a.xml".format(
        getPath())
    path2 = "{}\\..\\..\\tests\\test9\\b.xml".format(
        getPath())
    path = "{}\\..\\..\\tests".format(getPath())

    def testStdOutput(self):

        _t = time.time()

        result = main.diff_files(self.path1, self.path2)

        for x in result:
            print(x)

    def testHtmlOutput(self):

        _t = time.time()

        formatter = HTMLFormatter(
            text_tags=('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'),
            formatting_tags=('b', 'u', 'i', 'strike', 'em', 'super',
                             'sup', 'sub', 'link', 'a', 'span'))

        result = main.diff_files(self.path1, self.path2, formatter=formatter)

        print(time.time() - _t)

        with open('{}\\output.html'.format(self.path), "w") as f:
            f.write(result)
