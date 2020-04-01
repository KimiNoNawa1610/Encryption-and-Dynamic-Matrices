def image2complex(img_name):
    """
    IN: img_name - the name of the image to read
    OUT: set of complex numbers x+yi where the intensity of pixel (x,y) is greater than 120
    """
    import image
    
    # data is a list of lists such that the intensity of pixel (x,y) is given by data[h-1-y][x]
    # where h = height of the image
    data = image.color2gray(image.file2image("img01.png"))
    
    
    #FIXME: COMPLETE THIS FUNCTION

from plotting import plot
import image
#S = image2complex("img01.png")
data = image.color2gray(image.file2image("img01.png"))
print(data)
