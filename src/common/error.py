"""A standard defintion for error return by a static parser"""


class Error:
    lineNumber = 0
    fileName = ""
    errText = ""

    def __init__(self, lineNumber: int, fileName: str, errText: str):
        self.lineNumber = lineNumber
        self.fileName = fileName
        self.errText = errText
