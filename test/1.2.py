def head_tail(lst):
    return [x for x in lst if x[0] == x[len(x)-1]]
print(head_tail( [ 'apple', 'edge', 'idea', 'mm' , "TuyenT", "aA"] ))
print(head_tail( [ 'orange', 'kiwi', 'banana', "TUYENNUYENT"] ))