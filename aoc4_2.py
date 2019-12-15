#!/usr/bin/python3 -tt
from collections import Counter

def testnum(x):
    t=list(str(x))
    t=[int(i) for i in t]
    adj = False
    nevdec = True
    for i,v in enumerate(t[1:]):
        if v < t[i]:
            nevdec = False
            return nevdec
    
    for c in Counter(t).values():
        if c == 2:
            adj = True
    return adj and nevdec
    


def main():
    

    ran = list(range(278384,824796))

    ans = [testnum(i) for i in ran]
    print(ans.count(True))



if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))