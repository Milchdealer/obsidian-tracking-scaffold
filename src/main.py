#!/usr/bin/env python3
# *-* coding: utf-8 *-*
"""

"""
import argparse
from datetime import datetime


def create_scaffold(folder: str, year: int):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a scaffold for obsidian daily tracking notes."
    )
    parser.add_argument(
        "--year",
        type=int,
        default=datetime.now().year,
        help="The year to create the scaffold for",
    )
    parser.add_argument(
        "--folder",
        type=str,
        help="Where to create the scaffold",
        required=True,
    )
    args = parser.parse_args()

    create_scaffold(args.folder, args.year)
