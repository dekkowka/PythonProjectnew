import sys

def decrypt(text):
    result = []
    i = 0
    text_length = len(text)

    while i < text_length:
        char = text[i]

        if char == '.':
            i += 1
            continue

        if i + 1 < text_length and text[i + 1] == '.':
            if i + 2 < text_length and text[i + 2] == '.':
                if result:
                    result.pop()
                i += 3
            else:
                result.append(char)
                i += 2
        else:
            result.append(char)
            i += 1

    return ''.join(result)

if __name__ == '__main__':
    encrypted = sys.stdin.read().strip()
    print(decrypt(encrypted))