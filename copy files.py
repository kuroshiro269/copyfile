import os
import shutil

def copy_files(source_folder, destination_folder):
    # Get the list of files in the source folder
    source_files = os.listdir(source_folder)

    # Compare files in the source and destination folders
    for file_name in source_files:
        source_file_path = os.path.join(source_folder, file_name)
        destination_file_path = os.path.join(destination_folder, file_name)

        # Check if the file exists in the destination folder
        if not os.path.exists(destination_file_path):
            # Copy the file from the source folder to the destination folder
            shutil.copy2(source_file_path, destination_folder)
            print(f"Copied '{file_name}' from '{source_folder}' to '{destination_folder}'.")
        else:
            print(f"'{file_name}' already exists in '{destination_folder}'. Skipping...")

# Example usage
source_folder = '/path/to/source/folder'
destination_folder = '/path/to/destination/folder'

copy_files(source_folder, destination_folder)
