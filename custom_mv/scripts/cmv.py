#!/usr/bin/env python3

"""Script CustomMoVe."""

import argparse
import asyncio
from custom_mv.file_mover import process


def parse_args() -> (str, str):
    """Parse input params."""

    parser = argparse.ArgumentParser(description='move files from dir to dir')
    parser.add_argument(dest='src')
    parser.add_argument(dest='dest')
    args = parser.parse_args()
    return args.src, args.dest


def main() -> None:
    """Main."""

    src, dest = parse_args()
    asyncio.run(process(src, dest))


if __name__ == '__main__':
    main()
