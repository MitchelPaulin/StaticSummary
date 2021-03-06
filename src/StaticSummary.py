import argparse
from parsers.cppCheck import CppCheckParser
from parsers.clang import ClangParser
from parsers.flawFinder import FlawFinderParser
from common.htmlGenerator import HtmlGenerator
from common.error import Error
from typing import List
from pathlib import Path
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
    html = htmlGen.generateHtml(results)

    # Create output file
    OUT_DIR = '../output'

    try:
        Path(OUT_DIR).mkdir()
    except FileExistsError:
        pass

    outFileName = os.path.join(OUT_DIR, outFileName)
    f = open(outFileName, 'w')
    f.write(html)
    f.close()


def parse(tools, target: str, outFileName: str) -> List[Error]:
    """
    Parse the files and return the output as an error list
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


if __name__ == "__main__":
    main()
