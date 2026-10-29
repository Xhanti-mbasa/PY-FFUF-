def file_reader(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except IsADirectoryError:
        print(f"Expected a file but found a directory: {file_path}")
        return []
    
if __name__ == "__main__":
    words = file_reader("wordlist.txt")
    for word in words:
        print(word)  