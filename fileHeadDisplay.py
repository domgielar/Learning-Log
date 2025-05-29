
fileName = input("What's the name of the file: ").strip()numb

try:
    with open(fileName,'r') as infile:
        count = 0
        while count < 5:
            line = infile.readline()
            if line != '' and count <5:
                print(line.rstrip('\n'))
                count+=1
            els
                break
except FileNotFoundError:
    print("The file was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")