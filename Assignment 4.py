def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        
        with open(filename, "r") as file:
            content = file.read()

        
        modified_content = content.upper()

        
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"The modified content has been written to {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read or written.")

if __name__ == "__main__":
    read_and_modify_file()
