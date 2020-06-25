def convert(s):
    ans = [ord(x) for x in s]
    return ans
hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def convert_num(x):
    return str(hexa[x//16]) + str(hexa[x % 16])  
def convert_list(xs):
    ans = []
    for x in xs:
        ans += [convert_num(x)]
    return " ".join(ans)
l1 = convert("Toyo university")
print(l1)
print(convert_list(l1))
l2 = convert("This is a pen.")
print(l2)
print(convert_list(l2))
