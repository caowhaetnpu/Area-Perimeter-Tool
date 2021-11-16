sides = []
question1 = int(input("what are the sides of your square?"))
question2 = int(input("what are the sides of your square?"))
sides.append(question1)
sides.append(question2)
[first_item, second_item] = sides[:2]
print(first_item * second_item)