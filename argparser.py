#!/usr/bin/env python3
import argparse
import logging
DEBUG_MODE = False

def main():
    global DEBUG_MODE
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")

    args = parser.parse_args()
    print (args)
    DEBUG_MODE = args.verbose
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug('Only shown in debug mode')
    print("debug inside:",DEBUG_MODE)

main()

print("debug outside:",DEBUG_MODE)

