import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        file = open(f"files/{info[0]}", "w")
        file.close()
    elif command == "Add":
        with open(f"files/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")
    elif command == "Replace":
        try:
            with open(f"files/{info[0]}", "r") as file:
                text = file.readlines()

            for i in range(len(text)):
                text[i] = text[i].replace(info[2], info[3])

            with open(f"files/{info[0]}", "w") as file:
                file.write("".join(text))
        except FileNotFoundError:
            print(f"An error occurred!")

    elif command == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error occurred!")
    elif command == "End":
        break