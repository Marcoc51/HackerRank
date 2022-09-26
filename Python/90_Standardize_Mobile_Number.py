def wrapper(f):
    def fun(l):
        new_l = []
        for item in l:
            while len(item) > 10:
                item = item[1:]
            new_l.append(item)
        res_l = []
        for item in new_l:
            res_l.append(f'+91 {item[:5]} {item[5:]}')
        return f(res_l)    
    return fun
