import os
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]
    
    
def rename_files_in_directory(directory_path, starting_id):
    # List all files in the directory
    files = sorted([f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))])
    
    # Sort files alphabetically
    files.sort(key=natural_keys)

    # Rename files sequentially
    for i, filename in enumerate(files):
        # Define new name
        new_name = f"{i+starting_id}{os.path.splitext(filename)[1]}"
        
        # Define full old and new file paths
        old_file_path = os.path.join(directory_path, filename)
        new_file_path = os.path.join(directory_path, new_name)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {old_file_path} to {new_file_path}")

# Example usage
directory_path = 'D:\\Users\\mrgal\\Documents\\pokesprite\\images'  # Replace with the path to your directory
starting_id = 0 # Grookey's id
rename_files_in_directory(directory_path, starting_id)