import statistics as st
def my_mean_deviations(s):
    return st.mean(s), st.stdev(s)
s = [80, 75, 60, 90, 100, 55, 75, 95]
print(my_mean_deviations(s))