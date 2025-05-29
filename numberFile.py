def main():
    with open('numbersFileTest.py','r') as outfile:
        line = outfile.readline()
        while line !='':
            print(line.rstrip('\n'))
            line = outfile.readline()


if __name__ == '__main__':
    main()