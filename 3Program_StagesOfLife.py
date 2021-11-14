# steps:
# 1. Ask for the age,convert and store
age = int(input("Age: "))

# 2. Test if kid
if age > -1 and age <= 12:
    print("Kid")
# 3. Test if teen
elif age >= 13 and age <=17:
    print("Teen")
# 4. Test if debut
elif age == 18:
    print("Debut")
# 5. sure adult
else:
    print("Adult")

print("Done!")