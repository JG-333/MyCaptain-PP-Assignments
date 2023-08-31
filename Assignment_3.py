import operator


def most_frequent(string):
    d = dict()
    for i in string:
        d[i] = d.get(i, 0) + 1
    order = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    freq = ', '.join(f'{key} = {value}' for key, value in order.items())
    return freq


s = input("Please enter a string.\n")
print("Frequency of letters :",most_frequent(s))
