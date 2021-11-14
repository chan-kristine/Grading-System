# Clarification of system program
print("\nThe program will identify what digit is the lowest between the three user's inputted digits.")

first_num = float(input("Enter your first number: "))
second_num = float(input("Enter your second number: "))
third_num = float(input("Enter your third number: "))

def number_display(Amount1, Amount2, Amount3):
    if Amount1 < Amount2 and Amount1 < Amount3:
        return Amount1;
    elif Amount2 < Amount1 and Amount2 < Amount3:
        return Amount2;
    elif Amount3 < Amount1 and Amount3 < Amount2:
        return Amount3;


smallest_num = number_display(Amount1 = first_num, Amount2 = second_num, Amount3 = third_num)

print(f"The Lowest input number in the program is {smallest_num} .")