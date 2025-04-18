import sys

def get_mean_size():
    sizes = []
    try:
        lines = sys.stdin.readlines()[1:]
        for line in lines:
            parts = line.split()
            if len(parts) < 5 or parts[0].startswith('d'):
                continue
            try:
                size = int(parts[4])
                sizes.append(size)
            except ValueError:
                continue
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

    if not sizes:
        return 0

    return sum(sizes) // len(sizes)

if __name__ == '__main__':
    try:
        print(get_mean_size())
    except Exception as e:
        print(f"An error occurred in main: {e}")