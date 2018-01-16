import sys

flag = True
while flag:
    number1 = input("Enter a number: ")
    print(number1)
    if number1 == 'quit':
      sys.exit(1)

    number2 = input("Enter another number: ")
    if number2 == 'quit':
      sys.exit(1)

    try:
        number1 = int(number1)
        number2 = int(number2)
    except (ValueError, AttributeError):
          print("That isn't a number. Please enter a number")
    else:
      summation = number1 + number2
      print(summation)