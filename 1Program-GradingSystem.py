import math

Mark = (float(input("Enter you mark:")))
your_mark= round (Mark)
if your_mark >= 97 and your_mark <= 100:
    print("Excellent!")
    print("Your mark is 1.0!")
elif your_mark >= 94 and your_mark <= 96:
    print("Excellent!")
    print("Your mark is 1.25!")
elif your_mark >= 91 and  your_mark <= 93:
    print("Very Good!")
    print("Your mark is 1.5!")
elif your_mark >= 88 and your_mark <= 90:
    print("Very Good!")
    print("Your mark is 1.75!")
elif your_mark >= 85 and your_mark <= 87:
    print("Good!")
    print("Your mark is 2.0!")
elif your_mark >= 82 and your_mark <= 84:
    print("Good!")
    print("Your mark is 2.25!")
elif your_mark >= 79 and your_mark <= 81:
    print("Satisfactory!")
    print("Your mark is 2.50!")
elif your_mark >= 76 and your_mark <= 78:
    print("Satisfactory!")
    print("Your mark is 2.75!")
elif your_mark == 75:
    print("Passing!")
    print("Your mark is 3.0!")
elif your_mark >= 65 and your_mark <= 74:
    print("Failure!")
    print("Your mark is 5.0!")
else:
    print(f"Your mark is either (Inc.) Incomplete, Your mark has been withdrawn (W) or You are Dropped (D). ")

print("Your grade is recorded!")
