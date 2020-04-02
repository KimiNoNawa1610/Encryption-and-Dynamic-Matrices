import image
def reflectV(S, h):
    import math
    """
    reflects the complex numbers of set S about the vertical line x = h.  
    INPUT: 
        * S - set of complex numbers
        * h - float
    OUT:
        * set consisting of points in S reflected about the line x = h.
        
    """
    output=set()
    for i in S:
        d=abs(i.real-h)
        if i.real>h:
            newpoint=i-2*d
            output.add(newpoint)
        if i.real<h:
            newpoint=i+2*d
            output.add(newpoint)
    return output
    pass
data = image.color2gray(image.file2image("img01.png"))
S=image2complex(data)
h = -20
scale = 200

R1 = reflectV(S, h) #points reflected about x = -20
x_line = {h + y*1j for y in range(-scale, scale)}  #line of reflection

all_pts = R1.union(S, x_line)
plot(all_pts, 200) #second parameter affects window size
