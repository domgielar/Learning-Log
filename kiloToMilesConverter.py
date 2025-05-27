
kilometers = float(input("What is the distance in kilometers?: "))

def kilometers_to_miles(kilometers):
    miles = kilometers * .6214
    return miles

miles = kilometers_to_miles(kilometers)
print(f'there are {miles} miles in {kilometers} kilometers')
