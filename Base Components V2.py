Unit = 0
Sidelist = []
shapeSquare = 0
ShapeCal = 0
infomation = 0
print("Welcome!")
print()
print("""What Shape will you like to calculate?
        Square, Rectangle, Circle,Trapezoid
        """)
Shape = input("Pick:")
print()
Unit = input("What unit are you using? :")
print()
while infomation == 0:
    if Shape == "Square":
        ShapeCal = input("Area or perimeter?")
        if ShapeCal == "Area":
            print()
            question1 = int(input("what are the sides of your square?"))
            Sidelist = question1 * question1
            print("The Area of the Square is: {} {}".format(Sidelist, Unit))
            infomation = 1
        elif ShapeCal == "Perimeter":
            print()
            question1 = int(input("what are the sides of your square?"))
            Sidelist = question1 + question1 + question1 + question1
            print()
            print("The Perimeter of the Square is: {} {}".format(Sidelist, Unit))
            infomation = 1
        else:
            print("error")
            print()
            infomation = 0

    elif Shape == "Rectangle":
        ShapeCal = input("Area or perimeter?")
        if ShapeCal == "Area":
            print()
            question1 = int(input("what is the width of your rectangle? :"))
            question2 = int(input("what is the length of your rectangle? :"))
            Sidelist = question1 * question2
            print("The Area of the Rectangle is: {} {}".format(Sidelist, Unit))
            infomation = 1
        elif ShapeCal == "Perimeter":
            print()
            question1 = int(input("what is the width of your rectangle? :"))
            question2 = int(input("what is the length of your rectangle? :"))
            Sidelist = question1 + question1 + question2 + question2
            print()
            print("The Perimeter of the Rectangle is: {} {}".format(Sidelist, Unit))
            infomation = 1
        else:
            print("error")
            print()
            infomation = 0
    elif Shape == "Circle":
        ShapeCal = input("Area or perimeter?")
        if ShapeCal == "Area":
            print()
            question1 = int(input("what is the radius of your circle? :"))
            Sidelist = question1 * question1 * 3.14
            print("The Area of your Circle is: {} {}".format(Sidelist, Unit))
            infomation = 1
        elif ShapeCal == "Perimeter":
            print()
            question1 = int(input("what is the radius of your circle? :"))
            Sidelist = 2 * 3.14 * question1
            print()
            print("The Perimeter of the Circle is: {} {}".format(Sidelist, Unit))
            infomation = 1
        else:
            print("error")
            print()
            infomation = 0
    elif Shape == "Trapezoid":
        ShapeCal = input("Area or perimeter?")
        if ShapeCal == "Area":
            print()
            question1 = int(input("What is one base of your trapezoid? :"))
            question2 = int(input("What is the other base of your trapezoid? : "))
            question3 = int(input("What is the height of your trapezoid? : "))
            Sidelist = 0.5 * (question1 + question2) * question3
            print("The Area of the Trapezoid is: {} {}".format(Sidelist, Unit))
            infomation = 1
        elif ShapeCal == "Perimeter":
            print()
            question1 = int(input("what are the sides of your trapezoid?"))
            Sidelist = question1 + question1 + question1 + question1
            print()
            print("The Perimeter of the Trapezoid is: {} {}".format(Sidelist, Unit))
            infomation = 1
        else:
            print("error")
            print()
            infomation = 0

    else:
        print()
        ("Error: Please Enter One Of The Select Shapes")
        print()
        infomation = 0

