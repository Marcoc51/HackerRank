from datetime import datetime

def time_delta(t1, t2):
    T1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    T2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    if T1 > T2:
        res = T1 - T2
    else:
        res = T2 - T1
    return str(int(res.total_seconds()))
