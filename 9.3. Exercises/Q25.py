def merge(shelf, h1, h2):
    h1_pos = 0
    h2_pos = 0
    res = []
    while h1_pos < len(h1) or h2_pos < len(h2):
        if h1_pos == len(h1):
            res += [h2[h2_pos]]
            h2_pos+=1
        else:
            if h2_pos == len(h2):
                res += [h1[h1_pos]]
                h1_pos+=1
            else:
                if h1[h1_pos] < h2[h2_pos]:
                    res += [h1[h1_pos]]
                    h1_pos+=1
                else:
                    res += [h2[h2_pos]]
                    h2_pos+=1
    print("Merging   ", res)   
    return res
        
def msort(shelf, start_pos, end_pos):
    if (shelf[start_pos:end_pos+1]):
        print("Splitting   ", shelf[start_pos:end_pos+1])
    if start_pos == end_pos:
        return shelf[start_pos:end_pos+1];
    mid_pos = (start_pos + end_pos)//2
    h1 = msort(shelf, start_pos, mid_pos)
    h2 = msort(shelf, mid_pos+1,end_pos)
    return merge(shelf, h1, h2)
a = [12, 34, 47, 32]
sorted = msort(a, 0, len(a)-1)
print(a)
print(sorted)

    