print("Welcome!")
print()
shape = input("Please enter a shape: ")
print()
calculations = input("Are you calculating Perimeter or Area")
print()
dimensions = int(input("What are the dimensions of your shape?"))
sides = []
sides.append(dimensions)
if calculations == 'Perimeter':
    if len(sides) != 2:
        print("2")
    elif len(sides) != 3:
        print("3")
    elif len(sides) != 4:
        print("4")
    elif len(sides) != 5:
        print("5")
    elif len(sides) != 6:
        print("6")
    elif len(sides) != 7:
        print("7")
    elif len(sides) != 8:
        print("8")
    elif len(sides) != 9:
        print("9")
    elif len(sides) != 10:
        print("10")
    else:
        print("error")
elif calculations == 'Area':
    if len(sides) != 2:
        print("2")
    elif len(sides) != 3:
        print("3")
    elif len(sides) != 4:
        print("4")
    elif len(sides) != 5:
        print("5")
    elif len(sides) != 6:
        print("6")
    elif len(sides) != 7:
        print("7")
    elif len(sides) != 8:
        print("8")
    elif len(sides) != 9:
        print("9")
    elif len(sides) != 10:
        print("10")
    else:
        print("error")
else:
    print("error")

