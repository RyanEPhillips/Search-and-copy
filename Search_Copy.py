import os
import shutil

def copy_mp3(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        raise FileNotFoundError(f"Source folder '{source_folder}' does not exist.")
    if not os.path.exists(destination_folder):
        raise FileNotFoundError(f"Destination folder '{destination_folder}' does not exist.")

    for dirpath, _, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith('.mp3'):
                source_file = os.path.join(dirpath, filename)
                destination_file = os.path.join(destination_folder, filename)
                if os.path.exists(destination_file):
                    print(f"Skipping: {source_file} already exists in {destination_folder}")
                    continue
                else:
                    shutil.copy2(source_file, destination_file)
                    print(f"Copied: {source_file} to {destination_file}")

source_folder = ""  # Source folder path
destination_folder = ""  # Destination folder path

copy_mp3(source_folder, destination_folder)

