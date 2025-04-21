m= input("Any medical cause for absentee? (yes/no): ")
a=int(input("Enter attendance: "))
if m=="yes":
    print("You are allowed for exam")
else:
    if a>75:
        print("You are allowed for exam")
    else:
        print("You are not allowed for exam")