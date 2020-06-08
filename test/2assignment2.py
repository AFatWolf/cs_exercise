import re

def jp_to_us(date):
  match = re.fullmatch(r'(\d+)/(\d+)/(\d+)', date)
  return '{0}/{1}/{2}'.format(match.group(2), match.group(3), match.group(1))
print(jp_to_us('2020/5/31'))
print(jp_to_us('2020/6/1'))
