#!/usr/bin/python3 -tt

def testnum(x):
    t=list(str(x))
    t=[int(i) for i in t]
    adj = False
    nevdec = True
    for i,v in enumerate(t[1:]):
        #print('v'+str(v)+'t'+str(t[i]))
        if v == t[i]:
            adj=True
        if v < t[i]:
            nevdec = False
            break
    #print(adj)
    #print(nevdec)
    return adj and nevdec
    


def main():
    

    ran = list(range(278384,824796))

    ans = [testnum(i) for i in ran]
    print(ans.count(True))



if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))