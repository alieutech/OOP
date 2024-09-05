def create_an_write_file():
    try:
        # creating a new text file and writing three lines to it
        with open('my_file.txt', 'w') as file_object:
            file_object.write("Welcome to PLP Academy.\n")
            file_object.write("Where our objective is to train 1millions devs in africa.\n")
            file_object.write("For more info you can visit our website plpacademy.com.\n")
        print("File 'my_file.txt' created and written successfully.")
    except (FileNotFoundError, PermissionError) as f:
        print(f"Error while writing the file: {f}")
    finally:
        print("Write to a file completed.")


def read_file():
    try:
        # reading and displaying the contents of the file
        with open('my_file.txt', 'r') as file_object:
            print("\nReading file contents:")
            content = file_object.read()
            print(content)
    except (FileNotFoundError, PermissionError) as f:
        print(f"Error while reading the file: {f}")
    finally:
        print("Reading to a file is completed.")


def append_to_file():
    try:
        # opening the file in append mode and adding three additional lines
        with open('my_file.txt', 'a') as file_object:
            file_object.write("Welcome to PLP Academy.\n")
            file_object.write("Where our objective is to train 1millions devs in africa.\n")
            file_object.write("For more info you can visit our website plpacademy.com.\n")
        print("\nappending to lines are successfully.")
    except (FileNotFoundError, PermissionError) as f:
        print(f"Error while appending to the file: {f}")
    finally:
        print("Appending to a file  completed.")


def main():
    create_an_write_file()
    read_file()
    append_to_file()
    read_file()


if __name__ == "__main__":
    main()
