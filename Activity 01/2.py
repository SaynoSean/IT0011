def display_numbers_descending():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    descending_order = []

    if num1 >= num2:
        if num1 >= num3:
            descending_order.append(num1)
            if num2 >= num3:
                descending_order.append(num2)
                descending_order.append(num3)
            else:
                descending_order.append(num3)
                descending_order.append(num2)
        else:
            descending_order.append(num3)
            descending_order.append(num1)
            descending_order.append(num2)
    else:
        if num2 >= num3:
            descending_order.append(num2)
            if num1 >= num3:
                descending_order.append(num1)
                descending_order.append(num3)
            else:
                descending_order.append(num3)
                descending_order.append(num1)
        else:
            descending_order.append(num3)
            descending_order.append(num2)
            descending_order.append(num1)

    print("The numbers in descending order are:", descending_order)

display_numbers_descending()