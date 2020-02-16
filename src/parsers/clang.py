"""A implementation of a parser for the clang utility"""

from parsers.aParser import Parser
from common.error import Error
from subprocess import run, PIPE
import re
import os


class ClangParser(Parser):

    VALID_CPP_FILES = set(['.cpp', '.cc', '.h'])

    def __init__(self, targetDir: str):
        super().__init__(targetDir)

    def parse(self):
        # we only care about warnings, the fatals will be caught by a compiler
        pattern = re.compile("(.*):(\d*):\d*: warning: (.*)")

        # execute clang, need to execute on files individually
        ret = []
        for subdir, _, files in os.walk(self.targetDir):
            for f in files:
                for suffix in self.VALID_CPP_FILES:
                    if f.endswith(suffix):
                        result = run(['clang', '-fsyntax-only',
                                     os.path.join(subdir, f)],
                                     stdout=PIPE, stderr=PIPE)

                        error = result.stderr.decode("utf-8")
                        if(len(error) > 0):
                            err = re.findall(pattern, error)
                            for res in err:
                                result = Error(int(res[1]), res[0],
                                               res[2], 'clang')
                                ret.append(result)
        return ret
