
def main():
    try:
        sales = []
        while True:
            amt = input("Sales for today (type 'quit' to stop): ")
            if amt == "quit":
                break
            sales.append(int(amt))
        print(sum(sales))
    except:
        print("Something went wrong.")


if __name__ == "__main__":
    main()
    