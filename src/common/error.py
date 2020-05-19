"""A standard defintion for an error returned by a static parser"""


class Error:

    def __init__(self, lineNumber: int, fileName: str, errText: str,
                 source: str):
        self.lineNumber = lineNumber
        self.fileName = fileName
        self.errText = errText
        self.source = source

    def __str__(self):
        return self.fileName + ":" + str(self.lineNumber) + " " + \
            self.errText + " " + self.source
