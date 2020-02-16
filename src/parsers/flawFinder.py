"""A implementation of a parser for the flowfinder utility"""

from parsers.aParser import Parser
from common.error import Error
from subprocess import run, PIPE
import re


class FlawFinderParser(Parser):

    def __init__(self, targetDir: str):
        super().__init__(targetDir)

    def parse(self):
        # execute cpp check
        result = run(['flawfinder', '--quiet', '--dataonly', '--singleline',
                     self.targetDir], stdout=PIPE, stderr=PIPE)
        errors = result.stdout.decode("utf-8")

        # get relevant information
        ret = []
        pattern = re.compile("(.*):(\d*): *(.*)$")
        for err in errors.split("\n"):
            res = pattern.match(err)
            if res:
                result = Error(int(res.group(2)), res.group(1),
                               res.group(3), 'flawfinder')
                ret.append(result)
        return ret
