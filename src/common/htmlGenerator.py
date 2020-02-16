""" A generator which takes error objects and places them in an html file for
    easy viewing"""

import dominate
from dominate.tags import *
from datetime import date
from typing import List
from common.error import Error


class HtmlGenerator():

    title = "Static code output"
    tools = ""
    generatedOn = ""

    def __init__(self, tools: List[str], title=None):
        self.generatedOn = str(date.today())
        if title:
            self.title = title
        self.tools = tools

    def generateHtml(self, errors: List[Error]) -> str:
        doc = dominate.document(self.title)
        with doc.head:
            link(rel='stylesheet', href='common/style.css')
            h1(self.title)
            p("Generated: " + self.generatedOn)

        return str(doc)
