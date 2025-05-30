
def main():
    try:
        with open("name.txt.py", 'r') as infile:
            counter = 0
            for i, line in enumerate(infile, start=0):
                if line != '':
                    counter+=1
                else:
                    break
            print(counter)
    except FileNotFoundError:
        print("The file was not located")
    except Exception as e: 
        print(f'There was an error with the program: {e}') 

if __name__ == "__main__":
    main()

