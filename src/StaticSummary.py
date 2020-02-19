import argparse
from parsers.cppCheck import CppCheckParser
from parsers.clang import ClangParser
from parsers.flawFinder import FlawFinderParser
from common.htmlGenerator import HtmlGenerator
from common.error import Error
from typing import List
import os

SUPPORTED_TOOLS = set(['clang', 'cppcheck', 'flawfinder'])


def main():
    outFileName = "out.html"

    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str,
                        help='Specify the output file name')
    parser.add_argument('--target', type=str, required=True,
                        help="The target directory")
    parser.add_argument('--tools', nargs='+', required=True,
                        help="The static tool(s) you wish to use ex. clang")
    args = parser.parse_args()

    if not os.path.exists(args.target):
        print("%s does not exist" % (args.target))
        exit()

    if args.output:
        outFileName = args.output

    tools = set()
    for tool in args.tools:
        if tool not in SUPPORTED_TOOLS:
            print('Unsupported tool %s, use one of %s'
                  % (tool, str(SUPPORTED_TOOLS)))
            exit()
        tools.add(tool)
    results = parse(tools, args.target, outFileName)
    htmlGen = HtmlGenerator(tools)
    results = rollupErrors(results)
    html = htmlGen.generateHtml(results)
    f = open(outFileName, 'w')
    f.write(html)
    f.close()


def parse(tools, target: str, outFileName: str) -> List[Error]:
    """
    Prase the data and return the output as an error list
    """
    errors = []
    for tool in tools:
        if tool == 'cppcheck':
            parser = CppCheckParser(target)
            errors.append(parser.parse())
        elif tool == 'flawfinder':
            parser = FlawFinderParser(target)
            errors.append(parser.parse())
        elif tool == 'clang':
            parser = ClangParser(target)
            errors.append(parser.parse())
        # flatten ret before return
    return [e for err in errors for e in err]


def rollupErrors(errorList: List[Error]):
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


if __name__ == "__main__":
    main()
