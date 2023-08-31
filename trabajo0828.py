def sumavc(a,b):
    
    d1 = a[0]
    d2 = a[1]
    d3 = b[0]
    d4 = b[1]

    dat1 = d1 + d3
    dat2 = d2 + d4

    return (dat1,dat2)

def invervc(a):

    p1 = a[0]
    p2 = a[1]

    try1 = (p1 * -1)
    

    try2 = (p2 * -1)
    
    
    solu = try1,try2
 
    return solu

def multivc(a,b):

    b = list(b)
    for i in range(len(b)):
        b[i] = a*b[i]

    return b

def sumacvc(a,b):

    if len(a) != len(b):
        
        print("matrices tienen que tener el mismo tamaño")
    else:

        mat = []
        for i in range(len(a)):
            for j in range(len(a)):
                val = a[i][j] + b[i][j]
                mat.append(val)

        return mat


    
def main():

    print(sumavc((6,7),(3,5)))
    print(invervc((6,8)))
    print(multivc ((3),(6,7)))
    print(sumacvc(([3,5],[2,4]),([1,1],[1,1])))
    
main()
