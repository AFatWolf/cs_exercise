def stripe(w,h):
    for i in range(h):
        print("#" * w if i % 2 == 0 else '+' * w)
stripe(8,7)