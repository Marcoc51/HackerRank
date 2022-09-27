def person_lister(f):
    def inner(people):
        age = lambda person : int(person[2])
        people.sort(key=age)
        for person in people:
            yield f(person)
    return inner
