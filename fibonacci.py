
first_number = 0
second_number = 1

for i in range(10):
    print (first_number)
    temp = first_number
    first_number = second_number
    second_number = temp+second_number
