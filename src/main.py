import argparse
import re
from pathlib import Path

from constants import INVALID_FORMAT, NO_SOLUTION
from models import Curry, Customer, Proposals

SPLIT_REGEX = r"(?<=.) (?=\d)"


def main(file_path):
    with open(file_path, "r") as file:
        try:
            num_types = int(file.readline())
        except ValueError:
            return INVALID_FORMAT
        customers = []
        for line in file.readlines():
            preferences = []
            for preference in re.split(SPLIT_REGEX, line.rstrip()):
                try:
                    preferences.append(Curry(int(preference[0]), preference[2]))
                except (IndexError, ValueError):
                    return INVALID_FORMAT
            customers.append(Customer(preferences))
    result = Proposals(num_types, customers).resolve()
    if result != NO_SOLUTION:
        return " ".join(result.values())
    else:
        return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, type=Path)
    args = parser.parse_args()
    print(main(args.file))
