import re
def toyo2iniad(s):
    print(re.sub("@toyo.jp", "@iniad.org", s))
toyo2iniad("taro.yamato@toyo.jp")