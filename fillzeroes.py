import os
import re

    
def rename_files_in_directory(directory_path):
    # List all files in the directory
    files = sorted([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])
    
    # Rename files sequentially
    for i, filename in enumerate(files):
        # Define new name
        if len(os.path.splitext(filename)[0]) <= 3:
            new_name = f"{os.path.splitext(filename)[0].zfill(4)}{os.path.splitext(filename)[1]}"
            
            # Define full old and new file paths
            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} to {new_file_path}")
        # for formes
        elif len(os.path.splitext(filename)[0].split('-',1)[0]) <= 3:
            new_name = f"{os.path.splitext(filename)[0].split('-',1)[0].zfill(4)}-{os.path.splitext(filename)[0].split('-',1)[1]}{os.path.splitext(filename)[1]}"
            
            # Define full old and new file paths
            old_file_path = os.path.join(directory_path, filename)
            new_file_path = os.path.join(directory_path, new_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} to {new_file_path}")

# Example usage
directory_path = 'D:\\Users\\mrgal\\Documents\\pokesprite\\images'  # Replace with the path to your directory
rename_files_in_directory(directory_path)