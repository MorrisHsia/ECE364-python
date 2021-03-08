#! /user/local/bin/python3.7

import os


def runCheckAgainstStringFunctions():
    stringFunctions = ['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find',
                       'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
                       'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'ljust', 'lower', 'lstrip',
                       'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
                       'rstrip', 'split', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

    fileName = "regexTasks.py"

    if not os.path.exists(fileName):
        message = f"The file {fileName} was NOT found. No check has been made!"
        print(f"-------------------------------\n{message}\n-------------------------------\n")
        return

    with open(fileName, "r") as cFile:
        lines = cFile.readlines()

    printOut = ""
    functions = set()

    for index, line in enumerate(lines):
        for fn in stringFunctions:
            verb = f".{fn}("

            if verb in line:
                line = line.strip()
                printOut += f'   Fn: "{fn}()" => Line({index:03d}): "{line}"\n'
                functions.add(f"{fn}()")

    if printOut:
        message = f"The file {fileName} contains one or more string functions that cannot be used.\n"
        message += "Please remove these functions, or you might get 0.\n\n"
        message += "Functions Used: {0}\n\n".format(", ".join(functions))
        message += "Location Details:\n" + printOut
    else:
        message = "The file {0} has been checked, and it does not contain any string functions.".format(fileName)

    print("-------------------------------\n{}\n-------------------------------\n".format(message))


if __name__ == "__main__":
    # Verify that file is clean of string functions.
    runCheckAgainstStringFunctions()
