import re
def count_digit(line):
    ans = [x for x in re.sub('\d', '0', line) if x == '0']
    return len(ans)
print(count_digit("3 x 4 = 12 and 4 * 3 = 12 too."))
