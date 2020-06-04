def below_threshold(xs, threshold):
    return [x for x in xs if len(x) < threshold]
print(below_threshold(['apple',"kiwi", "orange"], 6))
print(below_threshold(['baseball','basketball', 'swinning'], 10))
print(below_threshold(['baseball','basketball', 'swinning'], 8))

