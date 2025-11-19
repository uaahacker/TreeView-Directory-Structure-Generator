# 🌳 TreeView - Directory Structure Generator

**TreeView** is a lightweight, cross-platform Python script that generates clean, visual directory tree structures and saves them to a text file. Perfect for documentation, backup organization, or just understanding what's inside your folders!

## ✨ Features

- 🖥️ **Cross-Platform** - Works on Windows, Linux, and macOS
- 📁 **Flexible Display** - Show only directories or include files
- 👁️ **Hidden Files Control** - Choose whether to display hidden items
- 📊 **File Size Information** - Displays human-readable file sizes (KB, MB, GB)
- 🎨 **Clean Tree Structure** - Beautiful ASCII tree visualization
- 💾 **Text Export** - Saves output to a timestamped text file
- 🔒 **Permission Handling** - Gracefully handles permission errors
- 🚀 **Easy to Use** - Interactive prompts or command-line arguments

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## 🚀 Quick Start

### Installation

1. Download the script:
```bash
wget https://raw.githubusercontent.com/yourusername/treeview/main/treeview.py
# Or simply copy the script to your local machine
```

2. Make it executable (Linux/macOS):
```bash
chmod +x treeview.py
```

### Usage

#### Interactive Mode
```bash
# Run the script
python3 treeview.py

# Follow the prompts:
# 1. Enter directory path (or press Enter for current directory)
# 2. Choose: only directories (1) or directories + files (2)
# 3. Show hidden files? (y/n)
```

#### Command-Line Mode
```bash
# Specify directory as argument
python3 treeview.py /path/to/directory

# Or use current directory
python3 treeview.py .

# Using tilde expansion (Linux/macOS)
python3 treeview.py ~/Downloads/backup
```

#### Windows
```cmd
# Using Command Prompt
python treeview.py C:\Users\YourName\Downloads\backup

# Using PowerShell
python treeview.py $HOME\Downloads\backup
```

## 📖 Examples

### Example 1: Show All Files and Folders
```
$ python3 treeview.py ~/Documents

What would you like to show?
1. Only directories
2. Both directories and files (default)
Enter your choice (1/2, default=2): 2
Show hidden files/folders? (y/n, default=n): n
```

**Output:**
```
└── Documents/
    ├── Projects/
    │   ├── python-app/
    │   │   ├── main.py (2.45 KB)
    │   │   └── utils.py (1.87 KB)
    │   └── website/
    │       ├── index.html (3.21 KB)
    │       └── style.css (1.09 KB)
    ├── Photos/
    │   ├── vacation.jpg (2.34 MB)
    │   └── family.jpg (1.87 MB)
    └── notes.txt (456 B)
```

### Example 2: Show Only Directories
```
$ python3 treeview.py ~/Downloads

What would you like to show?
1. Only directories
2. Both directories and files (default)
Enter your choice (1/2, default=2): 1
Show hidden files/folders? (y/n, default=n): n
```

**Output:**
```
└── Downloads/
    ├── backup/
    │   ├── documents/
    │   ├── images/
    │   └── videos/
    ├── software/
    └── temp/
```

### Example 3: Include Hidden Files
```
What would you like to show?
1. Only directories
2. Both directories and files (default)
Enter your choice (1/2, default=2): 2
Show hidden files/folders? (y/n, default=n): y
```

**Output:**
```
└── project/
    ├── .git/
    │   ├── hooks/
    │   └── objects/
    ├── .gitignore (234 B)
    ├── README.md (1.23 KB)
    └── main.py (3.45 KB)
```

## 📄 Output File

The script generates a file named `directory_structure.txt` with the following format:

```
Directory Structure
Generated: 2025-11-19 17:55:18
Path: /home/uaahacker/Downloads/backup
User: uaahacker
Mode: Directories and Files
Hidden items: Hidden
======================================================================

└── backup/
    ├── documents/
    │   ├── report.pdf (2.34 MB)
    │   └── notes.txt (1.23 KB)
    ...
```

## 🎯 Use Cases

- 📚 **Documentation** - Include directory structure in project READMEs
- 🗂️ **Backup Planning** - Visualize what needs to be backed up
- 🔍 **Code Reviews** - Share project structure with team members
- 📊 **Disk Analysis** - Understand folder organization and file sizes
- 🎓 **Learning** - Teach others about project layout
- 💼 **Professional Reports** - Include in technical documentation

## 🛠️ Advanced Usage

### Create an Alias (Linux/macOS)

Add to your `~/.bashrc` or `~/.zshrc`:
```bash
alias treeview='python3 /path/to/treeview.py'
```

Then use it anywhere:
```bash
treeview ~/Documents
```

### Add to PATH (Linux/macOS)

```bash
# Move to a bin directory
sudo cp treeview.py /usr/local/bin/treeview
sudo chmod +x /usr/local/bin/treeview

# Now run from anywhere
treeview ~/any/folder
```

### Windows Batch Wrapper

Create `treeview.bat`:
```batch
@echo off
python "C:\path\to\treeview.py" %*
```

Add the directory to your PATH, then use:
```cmd
treeview C:\Users\YourName\Documents
```

## 🔧 Customization

You can modify the script to:

- Change output filename (line 104: `output_file = "directory_structure.txt"`)
- Modify tree symbols (lines 9-10: `connector` variables)
- Adjust file size units (lines 63-68: `format_size` function)
- Add file type filtering
- Include file modification dates
- Add depth limiting

## 🐛 Troubleshooting

### Permission Denied Errors
If you see `[Permission Denied]` in the output, the script doesn't have access to those folders. Run with elevated privileges if needed:

```bash
# Linux/macOS
sudo python3 treeview.py /protected/folder

# Windows (run as Administrator)
python treeview.py C:\System\Folder
```

### Python Not Found
Make sure Python 3 is installed:
```bash
# Check Python version
python3 --version

# Install Python (Ubuntu/Debian)
sudo apt install python3

# Install Python (Fedora)
sudo dnf install python3
```

### UTF-8 Encoding Issues
If you see strange characters, ensure your terminal supports UTF-8:
```bash
# Linux/macOS
export LANG=en_US.UTF-8
```

## 📝 License

This project is released under the **MIT License**.

```
MIT License

Copyright (c) 2025 uaahacker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions
- Add JSON/XML output format
- Implement max depth limiting
- Add file type filtering (e.g., only .py files)
- Include file modification dates
- Add colorful terminal output
- Create a GUI version

## 📧 Contact

**Author:** uaahacker  
**Created:** November 19, 2025

For issues, suggestions, or questions, please open an issue on GitHub.

## 🌟 Star This Project

If you find TreeView useful, please give it a star! ⭐

---

**Happy Tree Viewing! 🌳**
