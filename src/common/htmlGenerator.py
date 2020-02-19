""" A generator which takes error objects and places them in an html file for
    easy viewing"""

import dominate
from dominate.tags import *
from datetime import date
from typing import List
from common.error import Error

STYLE = """
h1 {text-align: center; color: orange;}

hr {color: orange;}

p {text-align: center; font-weight: bold; color: orange;}

summary {text-indent: 15px; color: lightblue; font-size: larger;
          padding-bottom: 3px; border-bottom: 1px solid lightblue;}

body {background-color: rgb(50, 65, 65); color: white;}

li {padding-bottom: 2px;}
"""


class HtmlGenerator():

    title = "Static Code Output"
    tools = ""
    generatedOn = ""

    def __init__(self, tools: List[str], title=None):
        self.generatedOn = str(date.today())
        if title:
            self.title = title
        self.tools = tools

    def generateHtml(self, errors: List[Error]) -> str:
        doc = dominate.document(self.title)
        errors = self._rollupErrors(errors)
        with doc.head:
            style(STYLE)
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

    def _rollupErrors(self, errorList: List[Error]):
        """
        Takes a list of errors and groups them by file
        """
        ret = {}
        for err in errorList:
            if err.fileName not in ret:
                ret[err.fileName] = [(err.lineNumber, err.errText, err.source)]
            else:
                ret[err.fileName].append((err.lineNumber, err.errText, err.source))
        return ret
