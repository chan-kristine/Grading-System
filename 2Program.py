# Clarification of system program
print("\nThe program will identify what digit is the lowest between the three user's inputted digits.")

first_digit = float(input("Enter your first number: "))
second_digit = float(input("Enter your second number: "))
third_digit = float(input("Enter your third number: "))

def number_display(Quantity_1, Quantity_2, Quantity_3):
    if Quantity_1 < Quantity_2 and Quantity_1 < Quantity_3:
        return Quantity_1;
    elif Quantity_2 < Quantity_1 and Quantity_2 < Quantity_3:
        return Quantity_2;
    elif Quantity_3 < Quantity_1 and Quantity_3 < Quantity_2:
        return Quantity_3;


smallest_num = number_display(Quantity_1 = first_digit, Quantity_2 = second_digit, Quantity_3 = third_digit)

print(f"The Lowest input number in the program is {smallest_num} . ")