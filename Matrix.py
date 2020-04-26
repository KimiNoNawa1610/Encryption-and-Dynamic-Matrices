from Vector import Vec
class Matrix:
    
    def __init__(self, Rowsp=[]):  #FIXME: Replace with your code
        self.Rowsp=Rowsp
        self.Colsp=[]
        for i in range(len(self.Rowsp[0])):
            tempcol=[]
            for j in self.Rowsp:
                tempcol.append(j[i])
            self.Colsp.append(tempcol[:])
        pass
    
    def __add__(self, other):
        #FIXME: REPLACE WITH IMPLEMENTATION
        outputadd= Matrix([])
        add=[]
        if len(self.Rowsp)!=len(other.Rowsp):
            raise ValueError
        else:
            for subself, subother in zip(self.Rowsp,other.Rowsp):
                for selfitems, otheritems in zip(subself,subother):
                    add.append(selfitems+otheritems)
                for i in range(0,len(add),len(subself)):
                    templist=add[i:i+len(subself)]
                outputadd.Rowsp.append(templist)
        return outputadd
        pass 
    
    def __sub__(self, other):
        #FIXME: REPLACE WITH IMPLEMENTATION
        outputsub= Matrix([])
        sub=[]
        if len(self.Rowsp)!=len(other.Rowsp):
            raise ValueError
        else:
            for subself, subother in zip(self.Rowsp,other.Rowsp):
                for selfitems, otheritems in zip(subself,subother):
                    sub.append(selfitems-otheritems)
                for i in range(0,len(sub),len(subself)):
                    templist=sub[i:i+len(subself)]
                outputsub.Rowsp.append(templist)
        return outputsub
        pass
        
    def __mul__(self, other):
        outputmul=Matrix([])
        if type(other) == float:
            #print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")  #REPLACE
            mul=[]
            for subself in self.Rowsp:
                for selfitems in subself:
                    mul.append(selfitems*other)
                for i in range(0,len(mul),len(subself)):
                    templist=mul[i:i+len(subself)]
                outputmul.Rowsp.append(templist)
            
        elif type(other) == Matrix:
            #print("FIXME: Insert implementation of MATRIX-MATRIX multiplication") #REPLACE
            mul=[[0 for row in range(len(other.Rowsp[0]))]for column in range(len(self.Rowsp))]  
            if(len(self.Rowsp)!=len(other.Rowsp[0])):
                raise ValueError
            else:
                for i in range(len(self.Rowsp)):
                    for j in range(len(other.Rowsp[0])):
                        for k in range(len(other.Rowsp)):
                            mul[i][j]+=self.Rowsp[i][k]*other.Rowsp[k][j]
                outputmul.Rowsp=mul                  
        elif type(other) == Vec:
            #print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  #REPLACE
            if len(self.Rowsp[0])!=len(other.Rowsp):
                raise ValueError
            else:
                mul=[0 for column in range(len(self.Rowsp))]
                i=0
                x=0
                for j in range(len(self.Rowsp)):
                    i=0
                    row=0
                    for k in range(len(other.Rowsp)):
                        row=row+self.Rowsp[j][i]*other.Rowsp[i]
                        i+=1
                    mul[x]=row
                    x+=1
                    
                outputmul.elements=mul
        else:
            print("ERROR: Unsupported Type.")
        return outputmul
    
    def __rmul__(self, other):  
        if type(other) == float:
        #print("FIXME: Insert implementation of SCALAR-MATRIX multiplication")  #REPLACE
            outputmul=Matrix([])
            mul=[]
            for subself in self.Rowsp:
                for selfitems in subself:
                    mul.append(selfitems*other)
                for i in range(0,len(mul),len(subself)):
                    templist=mul[i:i+len(subself)]
                outputmul.Rowsp.append(templist)
        else:
            print("ERROR: Unsupported Type.")
        return outputmul

    def setCol(self,j,u):
        if len(u)!=len(self.Rowsp):
            raise ValueError("Incompatable column length")
        else:
            x=0
            for i in self.Rowsp:
                i[j-1]=u[x]
                x+=1

    def setRow(self,i,v):
        if len(v)!=len(self.Rowsp[i-1]):
            raise ValueError("Incompatable row length")
        else:
            self.elements[i-1]=v

    def setEntry(self,i,j,a):
        self.Rowsp[i-1][j-1]=a
        
    def getCol(self, j):
        output=[]
        for i in self.Rowsp:
            output.append(i[j-1])
        return output
    
    def getRow(self, i):
        return self.Rowsp[i-1]

    def getEntry(self,i,j):
        return self.Rowsp[i-1][j-1]

    def get_diagonal(m, i0, j0, d):
        return [m[(i0 + i - 1)%len(m)][(j0 + d*i - 1)%len(m[0])]
                for i in range(len(m))]
    
    def getColSpace(self):
        return self.Colsp

    def getRowSpace(self):
        return self.Rowsp
        
    def __str__(self):
        """prints the column """
        return "\n".join(" ".join(map(str,row))for row in self.Rowsp)
    
        


A = Matrix([[2, 0], [0, 2], [0, 0], [0, 0]])
print(A.getdiag(1,1,1))


