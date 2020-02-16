"""A implementation of a parser for the cppcheck utility"""

from parsers.aParser import Parser
from common.error import Error
from subprocess import run, PIPE
import re


class CppCheckParser(Parser):

    def __init__(self, targetDir: str):
        super().__init__(targetDir)

    def parse(self):
        # execute cpp check
        result = run(['cppcheck', self.targetDir], stdout=PIPE, stderr=PIPE)
        errors = str(result.stderr).split('\\n')

        # get relevant information
        ret = []
        pattern = re.compile(".*\[(.*):(\d*)\]: *(.*)$")
        for err in errors:
            res = pattern.match(err)
            if res:
                result = Error(int(res.group(2)), res.group(1),
                               res.group(3), 'cppcheck')
                ret.append(result)
        return ret
