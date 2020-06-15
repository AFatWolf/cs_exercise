def ssort(xs):
  for i in range(0, len(xs) - 1):
    maxval = xs[i]
    maxpos = i
    for j in range(i + 1, len(xs)):
      if xs[j] > maxval:
        maxval = xs[j]
        maxpos = j
    if i != maxpos:
      tmp = xs[i]
      xs[i] = maxval
      xs[maxpos] = tmp


b = [5,2,3,1,4]
print("Before sort:", b)
ssort(b)
print("After sort:", b)
