from Vector import Vec
class Matrix:
    
    def __init__(self, contents=[]):  #FIXME: Replace with your code
        self.elements=contents
        pass
    
    def __add__(self, other):
        #FIXME: REPLACE WITH IMPLEMENTATION
        outputadd= Matrix([])
        add=[]
        if len(self.elements)!=len(other.elements):
            raise ValueError
        else:
            for subself, subother in zip(self.elements,other.elements):
                for selfitems, otheritems in zip(subself,subother):
                    add.append(selfitems+otheritems)
                for i in range(0,len(add),len(subself)):
                    templist=add[i:i+len(subself)]
                outputadd.elements.append(templist)
        return outputadd
        pass 
    
    def __sub__(self, other):
        #FIXME: REPLACE WITH IMPLEMENTATION
        outputsub= Matrix([])
        sub=[]
        if len(self.elements)!=len(other.elements):
            raise ValueError
        else:
            for subself, subother in zip(self.elements,other.elements):
                for selfitems, otheritems in zip(subself,subother):
                    sub.append(selfitems-otheritems)
                for i in range(0,len(sub),len(subself)):
                    templist=sub[i:i+len(subself)]
                outputsub.elements.append(templist)
        return outputsub
        pass
        
    def __mul__(self, other):
        outputmul=Matrix([])
        if type(other) == float:
            #print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")  #REPLACE
            mul=[]
            for subself in self.elements:
                for selfitems in subself:
                    mul.append(selfitems*other)
                for i in range(0,len(mul),len(subself)):
                    templist=mul[i:i+len(subself)]
                outputmul.elements.append(templist)
            
        elif type(other) == Matrix:
            #print("FIXME: Insert implementation of MATRIX-MATRIX multiplication") #REPLACE
            mul=[[0 for row in range(len(other.elements[0]))]for column in range(len(self.elements))]  
            if(len(self.elements)!=len(other.elements[0])):
                raise ValueError
            else:
                for i in range(len(self.elements)):
                    for j in range(len(other.elements[0])):
                        for k in range(len(other.elements)):
                            mul[i][j]+=self.elements[i][k]*other.elements[k][j]
                outputmul.elements=mul                  
        elif type(other) == Vec:
            #print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  #REPLACE
            if len(self.elements[0])!=len(other.elements):
                raise ValueError
            else:
                mul=[0 for column in range(len(self.elements))]
                i=0
                x=0
                for j in range(len(self.elements)):
                    i=0
                    row=0
                    for k in range(len(other.elements)):
                        row=row+self.elements[j][i]*other.elements[i]
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
            for subself in self.elements:
                for selfitems in subself:
                    mul.append(selfitems*other)
                for i in range(0,len(mul),len(subself)):
                    templist=mul[i:i+len(subself)]
                outputmul.elements.append(templist)
        else:
            print("ERROR: Unsupported Type.")
        return outputmul

    def setCol(self,j,u):
        if len(u)!=len(self.elements):
            raise ValueError("Incompatable column length")
        else:
            x=0
            for i in self.elements:
                i[j-1]=u[x]
                x+=1

    def setRow(self,i,v):
        if len(v)!=len(self.elements[i-1]):
            raise ValueError("Incompatable row length")
        else:
            self.elements[i-1]=v

    def setEntry(self,i,j,a):
        self.elements[i-1][j-1]=a
        
    def getCol(self, j):
        mul=[]
        for i in self.elements:
            mul.append(i[j-1])
        return mul
    
    def getRow(self, i):
        return self.elements[i-1]

    def getEntry(self,i,j):
        return self.elements[i-1][j-1]
        
    def __str__(self):
        """prints the column """
        return str(self.elements)
    
        


A = Matrix([[1, 2, 3], [4, 5, 6]])
print(A.getEntry(1,1))

