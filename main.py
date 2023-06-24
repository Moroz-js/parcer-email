from argparse import ArgumentParser
import json
import sys

from clutch import parse_clutch
def get_arg_parser() -> ArgumentParser:
    """Get argument parser

    :rtype: ArgumentParser
    :returns: ArgumentParser object
    """

    arg_parser = ArgumentParser()
    arg_parser.add_argument(
        "-s",
        "--site",
        help="Read site to parse",
    )


    return arg_parser

def __init__() -> None:
    print('init')
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()
    pureCompanies = []
    with open('clutch.txt') as f:
        lines = f.readlines()
        parse_clutch(lines, pureCompanies)
    with open(f"companies.json", "w") as file:
        json.dump(pureCompanies, file, indent=4)
    sys.exit(0)
   
    

if __name__ == '__main__':
    __init__()