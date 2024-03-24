import tkinter as tk
from tkinter import filedialog
import os


def sanitize_filename(filename):
    # Replace invalid characters with underscores
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    return filename


def flip_hit_objects(filename):
    # Read the file
    with open(filename, "r") as file:
        lines = file.readlines()

    # Find the start and end index of [HitObjects] section
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if line.strip() == "[HitObjects]":
            start_index = i + 1
            break

    if start_index is None:
        print("Error: [HitObjects] section not found")
        return

    # Extract the [HitObjects] section
    hit_objects = lines[start_index:]

    # Flip the values in the fifth column
    flipped_hit_objects = []
    for line in hit_objects:
        parts = line.strip().split(",")
        if len(parts) >= 5:
            parts[4] = "0" if parts[4].strip() == "8" else "8"
        flipped_hit_objects.append(",".join(parts) + "\n")

    # Write the modified content to a new file with a modified name

    # Get the base filename without extension
    base_filename = os.path.splitext(os.path.basename(filename))[0]

    # Sanitize the base filename
    sanitized_base_filename = sanitize_filename(base_filename)

    # Write the modified content to a new file with a modified name
    flipped_filename = f"flippedVer_{sanitized_base_filename}.osu"
    with open(flipped_filename, "w") as file:
        file.writelines(lines[:start_index])
        file.writelines(flipped_hit_objects)


def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    filename = filedialog.askopenfilename(filetypes=[("OSU files", "*.osu")])
    if filename:
        flip_hit_objects(filename)


# Call select_file function to start the process
select_file()
