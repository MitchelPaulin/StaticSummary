import argparse
from parsers.cppCheck import CppCheckParser
from parsers.clang import ClangParser
from parsers.flowFinder import FlowFinderParser

SUPPORTED_TOOLS = ['clang', 'cppcheck', 'flawfinder']


def main():
    outFileName = "out.html"

    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=str,
                        help='specify the output file name')
    parser.add_argument('--target', type=str, required=True,
                        help="the target directory")
    parser.add_argument('--tools', nargs='+', required=True,
                        help="The static tools you wish to use ex. clang")
    args = parser.parse_args()

    if args.output:
        outFileName = args.output

    tools = []
    for tool in args.tools:
        if tool not in SUPPORTED_TOOLS:
            print('Unsupported tool %s, use one of %s'
                  % (tool, str(SUPPORTED_TOOLS)))
            exit()
        tools.append(tool)


if __name__ == "__main__":
    main()
