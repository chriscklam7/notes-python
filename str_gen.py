"""
String generator

Author: Chris
Email: chris.cklam7@gmail.com
"""

# Imports
# Python:
import sys
import argparse
import string
import secrets

# 3rd party:
# Internal:

# Variables
APP_TITLE = "String generator"

"""
functions:
set_argv_rule()
validate_pos_int(number)
generate_string(gen_str_each_length, gen_str_type, gen_str_number)
main(args)
"""

def set_argv_rule() -> argparse.Namespace:
    """
    Set argument rules
    1. Optional
    2. Required

    Returns
    -------
    args: Namespace
        Key-value of arguments
    """
    optional_argument = argparse.ArgumentParser(
        description="", formatter_class=argparse.RawTextHelpFormatter
    )
    # 1. Optional
    optional_argument.add_argument(
        "-l",
        "--each_length",
        type=validate_pos_int,
        help="length of each generated string",
        nargs="?",
        const=1,
        default=15,
    )
    optional_argument.add_argument(
        "-t",
        "--type",
        type=int,
        choices=[1, 2, 3],
        help="type of generated string\n\
1) ASCII letters and digits, e.g.: ABC..XYZ + abc...xyz + 123...890\n\
2) HEX, e.g.: ABCDEF + 123...890\n\
3) URL-safe, e.g.: ABC..XYZ + abc...xyz + 123...890 + - + _",
        nargs="?",
        const=1,
        default=1,
    )
    optional_argument.add_argument(
        "-n",
        "--number",
        type=validate_pos_int,
        help="number of generated strings",
        nargs="?",
        const=1,
        default=1,
    )
    # 2. Required
    args = optional_argument.parse_args()
    return args


def validate_pos_int(value: str) -> int:
    """
    Validate positive integer

    Returns
    -------
    int
    """
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("{} is not a valid integer".format(value))
    if number <= 0:
        raise argparse.ArgumentTypeError(
            "{} is an invalid positive integer".format(number)
        )
    return number


def generate_string(gen_str_each_length, gen_str_type, gen_str_number) -> str:
    """
    Generate string
    Type of generated string
    1) ASCII letters and digits, e.g.: ABC..XYZ + abc...xyz + 123...890
    2) HEX, e.g.: ABCDEF + 123...890
    3) URL-safe, e.g.: ABC..XYZ + abc...xyz + 123...890 + - + _

    Returns
    -------
    str:Generated string(s)
    """
    type = {}
    type[1] = string.ascii_letters + string.digits
    type[2] = string.hexdigits
    type[3] = secrets.token_urlsafe(gen_str_each_length)
    generated_strings_list = []
    for _ in range(gen_str_number):
        found = False
        while not found:
            if gen_str_type in [1, 2]:
                generated_string = "".join(secrets.choice(type[gen_str_type]) for _ in range(gen_str_each_length))
            elif gen_str_type == 3:
                generated_string = type[3]
            if generated_string not in generated_strings_list:
                found = True
                generated_strings_list.append(generated_string)
    generated_strings = "\n".join(generated_strings_list)
    return generated_strings


def main(args) -> None:
    print(f"{APP_TITLE}\n")
    print(f"args:\n{args}\n")
    generated_string = generate_string(args.each_length, args.type, args.number)
    print(f"generated_string:\n\n{generated_string}\n")

    print("end")


if __name__ == "__main__":
    args = set_argv_rule()
    main(args)
    sys.exit()
