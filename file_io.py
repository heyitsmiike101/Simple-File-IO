import json
import os
import csv
import re

############################################################
############################################################
# File_io
Version = "1.12"
#   FileIO
############################################################
############################################################


############################################################
#   JSON I/O
############################################################
def export_json(data: dict, filename: str):
    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=2)
    outfile.close()


def import_json(filename: str) -> dict:
    data = {}
    try:
        with open(filename) as json_file:
            data = json.load(json_file)
        json_file.close()
    except FileNotFoundError:
        print("File not found for", filename)
    return data


############################################################
#   CSV I/O
############################################################
def get_csv_headers(data: list[list]):
    return {k: v for v, k in enumerate(data[0])}


def import_csv(filename: str):
    """Returns 2 variables: data, col_names. Does not check if the file exists."""
    if not os.path.splitext(filename.lower())[-1] == ".csv":
        print("File type error")
        exit()
    data = []

    try:
        with open(filename, "r", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            data = list(list(rec) for rec in csv.reader(f, delimiter=","))
        f.close()
    except:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            data = list(list(rec) for rec in csv.reader(f, delimiter=","))
        f.close()

    col_names = get_csv_headers(data)
    return data, col_names


def export_csv(data: list, filename: str):
    while True:

        try:
            outFile = open(filename, "w", newline="")
            with outFile:
                writer = csv.writer(outFile)
                for i in data:
                    try:
                        writer.writerow(i)
                    except:
                        print("Cell overfilled. Printing in command prompt.")

            outFile.close()
            return True
        except:
            x = input(
                "FileWriteError: "
                + filename
                + " File with this name may already be open. Press enter once the file is closed or press 'q' then enter to quit."
            )
            if x == "q":
                exit()


############################################################
#   Text I/O
############################################################
def export_text_file(data: str, filename: str):
    try:
        with open(filename, "w", encoding="utf-8-sig") as f:
            f.write(data)
        f.close()
    except IOError:
        print(
            "IOError: "
            + filename
            + " File with this name may already be open. Press enter once the file is closed or press 'q' then enter to quit."
        )


def import_text_file(filename: str):
    data = ""
    try:
        with open(filename, "r") as f:
            data = f.read()
        f.close()
    except IOError:
        print(
            "IOError: "
            + filename
            + " File with this name may already be open or the file cannot be found."
        )
    return data


############################################################
#   General
############################################################


def create_directories(directories: str):
    """Builds out one or more directories deep if they don't exist."""
    directories = os.path.normpath(directories)
    directory_list = directories.split(os.sep)

    dir_string = ""
    # Builds the directory one level at a time to prevent errors.
    for i in directory_list:
        if i == "C:":
            dir_string = os.path.abspath(os.sep)
        else:
            dir_string = os.path.join(dir_string, i)

        if not os.path.isdir(dir_string):
            os.mkdir(dir_string)


def check_file_exists(path: str):
    """Check if file exsits. If it does append (#)."""
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        filename = re.sub(r"(\([0-9]+\))$", "", filename)
        path = filename + "(" + str(counter) + ")" + extension
        counter += 1

    return path
