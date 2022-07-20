def average(array):
    distinct = set(array)
    result = sum(distinct) / len(distinct)
    return("%.3f" % result)
