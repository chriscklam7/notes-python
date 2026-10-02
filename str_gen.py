"""
How to generate string randomly


Imports
-------
Python:
"""
import sys
import argparse
import string
import secrets

"""
3rd party:
"""

"""
Internal:
"""

"""
Variable:
"""
PROGRAM_TITLE = "Generate string randomly"


def set_argv_rule():
    """
    Set argument rule
    1. Required
    2. Optional

    Returns
    -------
    args: Namespace
        Key-value of arguments
    """
    optional_argument = argparse.ArgumentParser(
        description="", formatter_class=argparse.RawTextHelpFormatter
    )
    # Optional
    optional_argument.add_argument(
        "-l",
        "--each_length",
        type=validate_length_positive_int,
        help="length of each generated string",
        nargs="?",
        const=1,
        default=15,
    )
    optional_argument.add_argument(
        "-t",
        "--type",
        type=validate_type,
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
        type=validate_positive_int,
        help="number of generated strings",
        nargs="?",
        const=1,
        default=1,
    )
    # Required
    args = optional_argument.parse_args()
    return args


def validate_length_positive_int(number):
    """
    Validate positive integer

    Returns
    -------
    int
    """
    try:
        input_int = int(number)
        if input_int <= 0:
            raise argparse.ArgumentTypeError(
                "{} is an invalid positive integer".format(number)
            )
        elif input_int < 3:
            raise argparse.ArgumentTypeError(
                "Length must be equal to or larger than 3".format(number)
            )
    except ValueError:
        raise argparse.ArgumentTypeError(
            "{} is an invalid positive integer".format(number)
        )
    return input_int


def validate_type(number):
    """
    Validate positive integer
    Range of valid type [1-2]

    Returns
    -------
    int
    """
    try:
        input_int = int(number)
        if input_int < 1 or input_int > 3:
            raise argparse.ArgumentTypeError("{} is an invalid type".format(number))
    except ValueError:
        raise argparse.ArgumentTypeError("{} is an invalid type".format(number))
    return input_int


def validate_positive_int(number):
    """
    Validate positive integer

    Returns
    -------
    int
    """
    try:
        input_int = int(number)
        if input_int <= 0:
            raise argparse.ArgumentTypeError(
                "{} is an invalid positive integer".format(number)
            )
    except ValueError:
        raise argparse.ArgumentTypeError(
            "{} is an invalid positive integer".format(number)
        )
    return input_int


def generate_string(gen_str_each_length, gen_str_type, gen_str_number):
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
    type[1] = secrets.choice(string.ascii_letters + string.digits)
    type[2] = secrets.choice(string.hexdigits)
    type[3] = secrets.token_urlsafe(gen_str_each_length)
    generated_strings_list = []
    for _ in range(gen_str_number):
        found = False
        while not found:
            if gen_str_type in [1, 2]:
                generated_string = "".join(
                    type[gen_str_type] for _ in range(gen_str_each_length)
                )
            elif gen_str_type == 3:
                generated_string = type[3]
            if generated_string not in generated_strings_list:
                found = True
                generated_strings_list.append(generated_string)
    generated_strings = "\n".join(generated_strings_list)
    return generated_strings


def main(args):
    print(f"args:\n{args}\n")

    generated_string = generate_string(args.each_length, args.type, args.number)
    print(f"generated_string:\n\n{generated_string}\n")

    print("end")


if __name__ == "__main__":
    args = set_argv_rule()
    main(args)
    sys.exit()
