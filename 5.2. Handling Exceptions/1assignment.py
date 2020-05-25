while True:
  try:
    h = float(input('Width: '))
    v = float(input('Height: '))
    print('The area of rectangle is', v*h)
  except:
    print('Please input numbers correctly')