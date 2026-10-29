def file_reader(file_path: str) -> list[str]:
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        return [line.strip() for line in content if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
        #return {"Error": f"File not found: {file_path}"}
    except IsADirectoryError:
        print(f"Expected a file but found a directory: {file_path}")
        return []
        #return {"Error": f"Expected a file but found a directory: {file_path}"}

if __name__ == "__main__":
    print(file_reader("."))