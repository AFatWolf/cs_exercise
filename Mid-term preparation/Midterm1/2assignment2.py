import re
s = '2019/05/01'
result = re.fullmatch(r'(\d{4})/(\d{2})/(\d{2})', s)
if result:
    print('{0}-{1}-{2}'.format(result.group(1), result.group(2), result.group(3)))