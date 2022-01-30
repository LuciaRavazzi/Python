# Store multiple things on the clipboar -> every paste has its own key.

import json
import sys

import clipboard


def save_data(filepath, data):
    """
    Save data to json file.
    """
    with open(filepath, "w") as f:
        json.dump(data, f)


# save_items("test.json", {"key": "value"})


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


SAVED_DATA = "clipboard.json"

# --- Press the button in the upper left part.
# --- Command to execute the program: python multiclipboard.py

# Paste the data from the clipboard (the same as ctrl+V) to data.
# data = clipboard.paste()
# print(data)

# overwrite.
# clipboard.copy("abc")

# Catch the element of cmd.
if len(sys.argv) == 2:
    # take the command.
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        # Add a {key: clipboard.value} to a file.
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved. ")

    elif command == "load":
        # Check if the key exists and if so, put it into clipboard.copy
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
        else:
            print("Key does not exits.")
    elif command == "list":
        print(data)
    else:
        print("Unkown command.")
else:
    print("Please pass exactly one command.")
