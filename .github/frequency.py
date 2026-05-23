import sys
from collections import Counter

def count_vowels(file_path):
    try:
        with open(file_path, "r") as f:
            text = f.read().lower()

        vowels = "aeiou"
        counter = Counter(char for char in text if char in vowels)

        result = "\n".join([f"{v}: {counter[v]}" for v in vowels])
        print(result)
        return result

    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python frequency.py <file>")
        sys.exit(1)

    count_vowels(sys.argv[1])
