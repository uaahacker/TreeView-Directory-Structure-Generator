#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from datetime import datetime

def generate_tree(directory, prefix="", is_last=True, file_handle=None, show_hidden=False, dirs_only=False):
    """Generate a visual tree structure of directories and files."""
    
    dir_name = os.path.basename(directory) if os.path.basename(directory) else directory
    connector = "└── " if is_last else "├── "
    line = f"{prefix}{connector}{dir_name}/\n"
    
    if file_handle:
        file_handle.write(line)
    print(line, end="")
    
    new_prefix = prefix + ("    " if is_last else "│   ")
    
    try:
        items = os.listdir(directory)
        
        # Filter hidden files if needed
        if not show_hidden:
            items = [item for item in items if not item.startswith('.')]
        
        items.sort()
        
        # Separate directories and files
        dirs = [item for item in items if os.path.isdir(os.path.join(directory, item))]
        files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
        
        # Choose what to display based on dirs_only flag
        if dirs_only:
            all_items = dirs
        else:
            all_items = dirs + files
        
        for index, item in enumerate(all_items):
            item_path = os.path.join(directory, item)
            is_last_item = (index == len(all_items) - 1)
            
            if os.path.isdir(item_path):
                generate_tree(item_path, new_prefix, is_last_item, file_handle, show_hidden, dirs_only)
            else:
                try:
                    file_size = os.path.getsize(item_path)
                    size_str = format_size(file_size)
                    connector = "└── " if is_last_item else "├── "
                    file_line = f"{new_prefix}{connector}{item} ({size_str})\n"
                    
                    if file_handle:
                        file_handle.write(file_line)
                    print(file_line, end="")
                except (PermissionError, OSError):
                    connector = "└── " if is_last_item else "├── "
                    file_line = f"{new_prefix}{connector}{item} [Permission Denied]\n"
                    if file_handle:
                        file_handle.write(file_line)
                    print(file_line, end="")
    
    except PermissionError:
        error_line = f"{new_prefix}[Permission Denied]\n"
        if file_handle:
            file_handle.write(error_line)
        print(error_line, end="")

def format_size(size):
    """Format file size in human-readable format."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def main():
    print("Directory Tree Generator")
    print("=" * 50)
    
    # Check for command line arguments
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = input("Enter directory path (press Enter for current directory): ").strip()
    
    if not directory:
        directory = os.getcwd()
    
    # Expand user path (works for ~ on Linux)
    directory = os.path.expanduser(directory)
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist!")
        return
    
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a directory!")
        return
    
    # Ask what to show
    print("\nWhat would you like to show?")
    print("1. Only directories")
    print("2. Both directories and files (default)")
    choice = input("Enter your choice (1/2, default=2): ").strip()
    
    dirs_only = (choice == '1')
    
    # Ask about hidden files
    show_hidden = input("Show hidden files/folders? (y/n, default=n): ").strip().lower() == 'y'
    
    output_file = "directory_structure.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\nGenerating tree structure for: {directory}")
    print(f"Output will be saved to: {output_file}\n")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        header = f"Directory Structure\n"
        header += f"Generated: {timestamp}\n"
        header += f"Path: {os.path.abspath(directory)}\n"
        header += f"User: {os.getenv('USER', os.getenv('USERNAME', 'unknown'))}\n"
        header += f"Mode: {'Directories Only' if dirs_only else 'Directories and Files'}\n"
        header += f"Hidden items: {'Shown' if show_hidden else 'Hidden'}\n"
        header += "=" * 70 + "\n\n"
        f.write(header)
        print(header)
        
        generate_tree(directory, "", True, f, show_hidden, dirs_only)
    
    print(f"\n\n✓ Tree structure saved to '{output_file}'")
    print(f"✓ Total path: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()
