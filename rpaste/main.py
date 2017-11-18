import argparse
import pyperclip
import os.path
from .rpaste import rpaste


def main():
    parser = argparse.ArgumentParser(prog='rpaste')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('--push', nargs="*",
                       help='Push paste to rpaste.com')
    group.add_argument('--pull', nargs=1,
                       help='Pull paste from rpaste.com')

    parser.add_argument('--clip', action='store_true',
                        help='Use clipboard to push and pull paste')
    args = parser.parse_args()

    if args.push is not None:
        files = args.push
        if not files:
            # Get input from the console
            paste = rpaste()
            if args.clip:
                paste.set_content(pyperclip.paste())
            else:
                paste = paste.set_content(input())
            paste.upload()
        else:
            if len(files) > 10:
                print("Can only process 10 files at a time")
                exit(2)

            for filename in files:
                if not os.path.isfile(filename):
                    print("File {} not found.".format(filename))
                else:
                    paste = rpaste()
                    paste.set_content(open(filename,"r").read())
                    paste.upload()

    elif args.pull:
        pass

    return 0
