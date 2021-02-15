##!/usr/bin/env python

"""
Command line interface for python-package
"""

import argprase 
from python-package import day_of_the_week, info 

def parse_command_line():
    "Parses arguments for python-package functions."

    # Init parser and add arguments.
    parser = argparse.ArgumentParser()

    # Add long arguments.
    parser.add_argument(
        "--day",
        help = "Prints current day.",
        action = "store_true"
        )

# Parse arguments.
    args = parser.parse_args()

def main():
    """
    Run main function on parsed arguments.
    """

    # Get arguments from command line as a dict-like object.
    args = parse_command_line()

    # Pass argument to call day_of_the_week function.
    if args.today:
        day_of_the_week("day")

        info()

if __name__ == "__main__":
    day_of_the_week("day")
    info()
