def exam_any(xs, p):
    for x in xs: 
        if (x >= p):
            return "PASS"
    return "FAIL"
print(exam_any([50,60,70], 70))
print(exam_any([50,60], 70))
