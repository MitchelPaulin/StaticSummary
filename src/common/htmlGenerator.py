""" A generator which takes error objects and places them in an html file for
    easy viewing"""

import dominate
from dominate.tags import *
from datetime import date
from typing import List
from common.error import Error


class HtmlGenerator():

    title = "Static Code Output"
    tools = ""
    generatedOn = ""

    def __init__(self, tools: List[str], title=None):
        self.generatedOn = str(date.today())
        if title:
            self.title = title
        self.tools = tools

    def generateHtml(self, errors) -> str:
        doc = dominate.document(self.title)
        with doc.head:
            link(rel='stylesheet', href='common/style.css')
            h1(self.title)
            p("Generated: " + self.generatedOn)
            p("Tools used: " + str(self.tools))
            hr()

        # sort the files by number of errors
        errors = {k: v for k, v in sorted(errors.items(),
                  key=lambda item: -1 * len(item[1]))}

        with doc.body:
            for fileName in errors:
                title = "{} ({} errors)".format(fileName,
                                                str(len(errors[fileName])))
                tempList = ul()
                for info in errors[fileName]:
                    tempList += li("{}: {} ({})".format(
                                   info[0], info[1], info[2]))
                detail = details(summary(title), tempList)
                doc += detail

        return str(doc)
