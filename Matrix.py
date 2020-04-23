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
        mul=[]
        if type(other) == float:
            #print("FIXME: Insert implementation of MATRIX-SCALAR multiplication")  #REPLACE
            for subself in self.elements:
                for selfitems in subself:
                    mul.append(selfitems*other)
                for i in range(0,len(mul),len(subself)):
                    templist=mul[i:i+len(subself)]
                outputmul.elements.append(templist)
            
        elif type(other) == Matrix:
            #print("FIXME: Insert implementation of MATRIX-MATRIX multiplication") #REPLACE
            if(len(self.elements)!=len(other.elements[0])):
                raise ValueError
            else:
                for subother in other.elements:
                    for subitems in subother:
                        print(subitems)
            
        elif type(other) == Vec:
            print("FIXME: Insert implementation for MATRIX-VECTOR multiplication")  #REPLACE
            
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
    
    def __str__(self):
        """prints the column """
        return str(self.elements)

A = Matrix([[2, 0], [0, 2], [0, 0], [0, 0]])
B = Matrix([[2, 0,0,0], [0,1, 2,0], [2,1, 0,0], [0,0, 1,0]])
print(A+B)
print(3.0*A)
print(A*B)
