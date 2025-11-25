#!/usr/bin/python

import sys
from pathlib import Path

def grep(pattern: str, path_to_file: Path, case_match: bool, line_numbers: bool):
    with open(path_to_file, "r") as infile:
        line_number = 0
        for line in infile:
            line_number += 1
            if case_match:
                if line_numbers:
                    if pattern in line:
                        if line_number / 10 < 1:
                            print(f"{line_number}      {line}")
                        elif line_number / 100 < 1:
                            print(f"{line_number}     {line}")
                        else:
                            print(f"{line_number}    {line}")
                else:
                    if pattern in line:
                        print(f"    {line}")

            else:
                if line_numbers:
                    if pattern in line.lower():
                        if line_number / 10 < 1:
                            print(f"{line_number}      {line}")
                        elif line_number / 100 < 1:
                            print(f"{line_number}     {line}")
                        else:
                            print(f"{line_number}    {line}")
                else:
                    if pattern in line.lower():
                        print(f"    {line}")

    infile.close()

def main(args):
    if len(args) < 3:
        print("Error: Too few arguments")
        print("Usage: `./grep.py <string to search> <path to file> <case match: y/[n]> <line numbers: [y]/n`")
    else:
        pattern = args[1]
        path_to_file = Path(args[2])
        case_match = False
        line_numbers = True
        if len(args) == 4:
            match args[3]:
                case 'y':
                    case_match = True
                case _:
                    pass
        if len(args) == 5:
            match args[4]:
                case 'n':
                    line_numbers = False
                case _:
                    pass


        grep(pattern, path_to_file, case_match, line_numbers)

if __name__ == '__main__':
    main(sys.argv)
