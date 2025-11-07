import os

def print_tree(directory, prefix="", output_file=None):
    contents = sorted(os.listdir(directory))
    for i, item in enumerate(contents):
        if item.startswith('.') or item in ['__pycache__', '*.pyc', 'venv', 'env', '.git', 'db.sqlite3']:
            continue
        path = os.path.join(directory, item)
        is_last = i == len(contents) - 1
        current_prefix = "└── " if is_last else "├── "
        line = prefix + current_prefix + item
        print(line)
        if output_file:
            output_file.write(line + "\n")
        if os.path.isdir(path):
            extension_prefix = "    " if is_last else "│   "
            print_tree(path, prefix + extension_prefix, output_file)

# Fixed: Add encoding='utf-8' to handle Unicode characters on Windows
with open('structure.txt', 'w', encoding='utf-8') as f:
    print_tree('.', output_file=f)

print("\n✓ Project structure saved to structure.txt")
