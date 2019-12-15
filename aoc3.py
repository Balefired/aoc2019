#!/usr/bin/python3 -tt
from scipy.spatial.distance import cdist
counter=0

def movement(coords, move):
    #print(move)
    if move[0] == 'U':
        x = [coords[-1][0]] * (int(move[1:]))
        y = list(range( (coords[-1][1]+1), (coords[-1][1]+1) + (int(move[1:])) ))
        coords.extend(zip(x,y))
    if move[0] == 'R':
        y = [coords[-1][1]] * (int(move[1:]))
        x = list(range(coords[-1][0]+1,(coords[-1][0]+1) + (int(move[1:]))))
        coords.extend(zip(x,y))
    if move[0] == 'D':
        x = [coords[-1][0]] * (int(move[1:]))
        y = list(range( (coords[-1][1]-1), (coords[-1][1]-1) - (int(move[1:])) ,-1))
        coords.extend(zip(x,y))
    if move[0] == 'L':
        y = [coords[-1][1]] * (int(move[1:]))
        x = list(range( (coords[-1][0]-1), (coords[-1][0]-1) - (int(move[1:])) ,-1))
        coords.extend(zip(x,y))
    return coords

def city(c, coords2):
    global counter
    counter+=1
    print(counter)
    if c in coords2[1:]:
        return cdist([(0,0)],[c],'cityblock')[0]
    else: 
        return 0



def main():
    f=open('aoc3.txt','r')
    text = f.read()
    f.close()
    text = text.rstrip()
    wires = text.split('\n')
    wires = [wire.split(',') for wire in wires]
    
    coords1 = [[0,0]]

    for w in wires[0]:
        coords1 = movement(coords1, w)

    #print(coords1)

    coords2 = [[0,0]]

    for w in wires[1]:
        coords2 = movement(coords2, w)

    #print(coords2)


    

    #print(len(coords1))
    #input('press enter')

    #crossv = [city(c,coords2) for c in coords1[1:]]

    '''for c in coords1[1:]:
        print('still goin '+str(counter) )
        counter+=1'''

    #print(crossv)
    #print(min(list(filter((0).__ne__,crossv))))

    cross = set(coords1[1:]) & set(coords2[1:])

    crossv = [cdist([(0,0)],[c],'cityblock')[0][0] for c in cross]
    #crossv = [i[0] for i in crossv]
    print('answer part 1')
    print(min(crossv))

    crossv2 = []
    for i in list(cross):
        crossv2.append((coords1.index(i))+(coords2.index(i)))
    print('answer part 2')
    
    print(min(crossv2))
    

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('main()', setup='from __main__ import main', number=1))