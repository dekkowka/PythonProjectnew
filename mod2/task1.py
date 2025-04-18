import sys
import os

def get_summary_rss(file_path):
    total_rss = 0
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()[1:]
            for line in lines:
                columns = line.split()
                if len(columns) > 5:
                    try:
                        total_rss += int(columns[5])
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return "0 B"
    except Exception as e:
        print(f"Error reading file: {e}")
        return "0 B"

    return format_size(total_rss * 1024)

def format_size(size_bytes):
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    index = 0
    while size_bytes >= 1024 and index < len(units) - 1:
        size_bytes /= 1024.0
        index += 1
    return f"{size_bytes:.2f} {units[index]}"

if __name__ == '__main__':
    path_to_file = 'output.txt'

    if not os.path.exists(path_to_file):
        with open(path_to_file, 'w') as f:
            f.write("Header Line\n")
            f.write("Process1  1234  5678  9101  1112  50\n")
            f.write("Process2  2345  6789  0123  2345  100\n")
    result = get_summary_rss(path_to_file)
    print(result)