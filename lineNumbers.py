
fileName = input("What's the name of the file: ").strip()

try:
    with open(fileName, 'r') as infile:
        for i, line in enumerate(infile, start=0):
                print(f"{line.strip()} {i}:")

except FileNotFoundError:
    print("The file was not found")

except Exception as e:
    print(f"An unexptected error occurred: {e}")