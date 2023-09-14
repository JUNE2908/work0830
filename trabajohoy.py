import numpy as np

def adicv(a,b):
    v1 = np.array(a)
    v2 = np.array(b)
    solu = v1 + v2
    return (solu)

def inveravc(a):
    vect = np.array(a)
    solu = vect * (-1)
    return (solu)

def multvc(a,b):
    vect = np.array(b)
    solu = a * vect
    return (solu)

def adicmc(a,b):
    matri1 = np.array(a)
    matri2 = np.array(b)
    solu = matri1 + matri2
    return (solu)

def invemc(a):
    matri = np.array(a)
    solu = matri * (-1)
    return (solu)

def multmc(a,b):
    val = np.array(b)
    solu = a * val
    return (solu)

def tranmv(a):
    x = np.array(a)
    solu = np.transpose(x)
    return (solu)

def conjmv(a):
    val = np.array(a)
    solu = x.conjugate(val)
    return (solu)

def dagamv(a):
    val = np.array(a)
    solu = transp(conjug(val))
    return (solu)

def prodmatrices(a,b):
    if len(a[0]) == len(b[1]):
        xx = np.array(a)
        yy = np.array(b)
        solu = np.matmul(xx,yy)
        return (solu)
    else:
        return ("No son del mismo tamaño")
    
def accionmv(a,b):
    if len(a[0]) == len(b):
        matri = np.array(a)
        vec = np.array(b)
        solu = np.array(np.dot(matri,vec))
        return (solu)
    else:
        return ("No son del mismo tamaño")
    
def prodint(a,b):
    if len(a) == len(b):
        val1 = dagamv(np.array(a))
        val2 = np.array(b)
        solu = np.array(np.dot(val1,val2))
        return (solu)
    else:
        return ("No cumple requerimientos")
    
def normv(a):
    val = np.array(a)
    prod = prodint(val,val)
    solu = np.sqrt(prod)
    return (result.real)

def distvec(a,b):
    v1 = np.array(a)
    v2 = np.array(b)
    disr = v1 - v2
    solu = norma(disr)
    return (solu.real)

def valyvect(a):
    if len(a) == len(a[0]):
        mat = np.array(a)
        valores,vectores = np.linalg.eig(mat)
        return "valores propios {} vectores propios {}".format(valores, vectores)
    else:
        return ("No cumple requerimientos")

def unita(a):
    matri = np.array(a)
    adj = dagamv(matri)
    iden = np.identity(len(matri))
    prod = prodmatrices(matri,adj)
    if prod.all() == iden.all():
        return ("Es matriz unitaria")
    else:
        return ("No es matriz unitaria")
    
def hermi(x):
    mat = np.array(x)
    adj = dagamv(mat)
    if mat.all() == adj.all():
        return ("Es matriz hermitiana")
    else:
        return ("No es matriz hermitiana")
    

def prodten(a,b):
    val1 = np.array(a)
    val2 = np.array(b)
    resultado=[]
    for i in range (len(val1)):
        for j in range(len(val2)):
            r=val1[i]*vval2[j]
            resultado.append(r)
    return resultado

def prod_tensor_m(a,b):
    m1 = np.array(a)
    m2 = np.array(b)
    n=len(m2)
    n2=len(m2[0])
    m=len(m1)
    m2=len(m1[0])
    x=n*m
    x2=n2*m2
    solu=[[0 for i in range (x)]for j in range (x2)]
    for i in range(x2):
        for j in range(x):
            solu[i][j]= a[j//n][j//n2]*b[j%n][j%n2]
    return (solu)

