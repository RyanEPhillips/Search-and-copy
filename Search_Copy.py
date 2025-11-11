import os
import shutil

def copy_mp3(source_folder, destination_folder):
    if not os.path.exists(source_folder): # Check for source folder
        raise FileNotFoundError(f"Source folder '{source_folder}' does not exist.")
    if not os.path.exists(destination_folder): # Check for destination folder
        raise FileNotFoundError(f"Destination folder '{destination_folder}' does not exist.")

    for dirpath, _, filenames in os.walk(source_folder):
        for filename in filenames: # Iterate through files
            if filename.endswith('.mp3'): # Check for .mp3 files
                source_file = os.path.join(dirpath, filename) # Full path of source file
                destination_file = os.path.join(destination_folder, filename) # Full path of destination file
                if os.path.exists(destination_file): # Check if file already exists in destination
                    print(f"Skipping: {source_file} already exists in {destination_folder}") 
                else: # Copy file if it doesn't exist
                    shutil.copy2(source_file, destination_file) # Copy file with metadata
                    print(f"Copied: {source_file} to {destination_file}") 

source_folder = ""  # Source folder path
destination_folder = ""  # Destination folder path

copy_mp3(source_folder, destination_folder)