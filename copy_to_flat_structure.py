#!/usr/bin/env python3
import os
import shutil
import re

# Define source and destination directories
source_dir = "/home/daniel/Development/Repos/Speech-To-Text-System-Prompt-Library/system-prompts"
dest_dir = "/home/daniel/Development/Repos/Speech-To-Text-System-Prompt-Library/system-prompts/flat-structure"

# Create destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Function to create a safe filename
def make_safe_filename(path, filename):
    # Extract the directory path relative to source_dir
    rel_path = os.path.dirname(path.replace(source_dir, '').lstrip('/'))
    
    # If the file is already in the root of system-prompts, just return the filename
    if not rel_path:
        return filename
    
    # Create a prefix from the relative path
    prefix = rel_path.replace('/', '-')
    
    # Return the prefixed filename
    return f"{prefix}--{filename}"

# Count for reporting
copied_files = 0

# Walk through the source directory
for root, dirs, files in os.walk(source_dir):
    # Skip the flat-structure directory itself to avoid copying files we just created
    if "flat-structure" in root:
        continue
        
    # Process each markdown file
    for file in files:
        if file.endswith(".md"):
            source_path = os.path.join(root, file)
            
            # Create a safe filename to avoid conflicts
            safe_filename = make_safe_filename(root, file)
            dest_path = os.path.join(dest_dir, safe_filename)
            
            # Copy the file
            shutil.copy2(source_path, dest_path)
            copied_files += 1
            print(f"Copied: {source_path} -> {dest_path}")

print(f"\nCompleted! {copied_files} files copied to {dest_dir}")
