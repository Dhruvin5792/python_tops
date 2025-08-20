choice ='y'
while choice !='n':

    mark = int(input("Enter Your Mark :-"))
    print("Your mark Is:-",mark)

    if mark<=100 and mark>=91:
        print("grade is A")
    elif mark<=90 and mark>=71:
        print("grade is B")
    elif mark<=70 and mark>=51:
        print("grade is C")
    elif mark<=50 and mark>=35:
        print("grade is  D")
    elif mark<=34 and mark>=0:
        print("grade is  E")
    else:
        print("invalid input")

    choice = input("do you want to repect?(y/n):-")




