#!/usr/bin/env python3
# Utils for Samuel Davenport

NAME = 'Utils'
__version__ = '0.0.1'

def intl(*args):
    data = []
    for i in args:
        data.append(int(i))
    return tuple(data)

def floatl(*args):
    data = []
    for i in args:
        data.append(float(i))
    return tuple(data)

def strl(*args):
    data = []
    for i in args:
        data.append(str(i))
    return tuple(data)

def roundl(*args):
    data = []
    for i in args:
        data.append(round(i))
    return tuple(data)

def amol(lst, **kwargs):
    # Math Operator acting appon All values of a List
    data = list(lst)
    rng = range(len(data))
    operators = kwargs.keys()
    if 'a' in operators:#add
        for i in rng:
            data[i] += kwargs['a']
    if 's' in operators:#subtract
        for i in rng:
            data[i] -= kwargs['s']
    if 'm' in operators:#multiply
        for i in rng:
            data[i] *= kwargs['m']
    if 'd' in operators:#divide
        for i in rng:
            data[i] /= kwargs['d']
    if 'p' in operators:#power
        for i in rng:
            data[i] **= kwargs['p']
    return tuple(data)

def rev(text):
    # Reverse text
    v = list(text)
    v.reverse()
    return ''.join(v)

def revlistitems(_list):
    # Reverse the items of a list
    data = []
    for i in _list:
        data.append(rev(str(i)))
    return data
