# -*- coding: utf-8 -*-

def recorrer (m): 
    if m == [['16']]:
        return '16'
    else:       
        return  leer(m)+" "+recorrer(eliminar(m))
def voltear (m):
    return [[m[i][j] for i in range(0, len(m), 1)] for j in range(len(m[0])-1,-1 , -1)]
def eliminar (m):
    m.remove(m[0])
    return  voltear(m)
def leer(m):
    return ' '.join(m[0])
print(recorrer([x.split()for x in open ("C:\\Users\\david\\Desktop\\matriz.txt").readlines()]))
