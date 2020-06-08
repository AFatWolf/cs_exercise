while True:
  try:
    a = float(input('Input the value of "a", for equation ax + b = 0: '))
    b = float(input('Input the value of "b", for equation ax + b = 0: '))
    print('x = ' + str(-b/a))
  except KeyboardInterrupt:
    print('The program will terminate because CTRL+C is pressed.')
    break
  except ValueError:
    print('Input a numerical value.')
  except ZeroDivisionError:
    print('Input a value other than zero for "a".')