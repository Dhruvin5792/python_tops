percentage = int(input("Enter your percentage :-"))
print("Your Percentage is :-",percentage)

if percentage<=100 and percentage>=90:
    print("Grade is A+")
elif percentage<=89 and percentage>=80:
    print("Grade is A")
elif percentage<=79 and percentage>=70:
    print("Grade is B")
elif percentage<=69 and percentage>=60:
    print("Grade is C")
elif percentage<=59 and percentage>=50:
    print("Grade is D")
elif percentage<=49 and percentage>=0:
    print("Grade is F")
else:
    print("invalid input")