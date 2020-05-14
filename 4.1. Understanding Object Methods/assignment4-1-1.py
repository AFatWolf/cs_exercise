def list_upper(xs):
  result = []
  for x in xs:
    result.append(x.upper())
  return result
xs = ['a','b','c']
print(list_upper(xs))