#!/usr/bin/python3 -tt

def intcode(x, noun, verb):
    t = x[:]
    t[1]=noun
    t[2]=verb
    pos=0
    while t[pos] != 99:
        if t[pos] == 1:
            t[t[pos+3]]=t[t[pos+1]]+t[t[pos+2]]
        elif t[pos] == 2:
            t[t[pos+3]]=t[t[pos+1]]*t[t[pos+2]]
        pos+=4
    return t[0]

def main():
    print('Readin data')
    f=open('aoc2.txt','r')

    print('Cleanin data')
    text = f.read()
    f.close()
    x=text.rstrip().split(',')
    x=[int(i) for i in x]

    print('Calculatin')
    n_answer = 0
    v_answer = 0
    for noun in list(range(0,100)):
        verbs = list(range(0,100))
        answers = [intcode(x,noun,v) for v in verbs]
        if 19690720 in answers:
            n_answer = noun
            v_answer = answers.index(19690720)
            break
    fanswer = (100*n_answer)+v_answer
    print(fanswer)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))