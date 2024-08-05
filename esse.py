import os
import hashlib

def hash_file(file_path):
    """Generate a hash for a given file."""
    hasher = hashlib.sha256()  # You can use hashlib.md5() or hashlib.sha1() instead
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def check_duplicates(directory):
    """Check if all files in the directory are duplicates."""
    if not os.path.isdir(directory):
        raise ValueError(f"The path {directory} is not a valid directory.")

    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        raise ValueError("The directory is empty.")
    
    # Calculate hashes for all files
    hashes = [hash_file(file) for file in files]

    # Check if all hashes are the same
    all_duplicates = all(h == hashes[0] for h in hashes)

    return all_duplicates

# Example usage
directory_path = "/path/to/your/folder"
if check_duplicates(directory_path):
    print("All files in the folder are duplicates.")
else:
    print("Not all files in the folder are duplicates.")
