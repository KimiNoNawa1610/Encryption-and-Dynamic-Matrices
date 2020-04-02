def image2complex(img_name):
    """
    IN: img_name - the name of the image to read
    OUT: set of complex numbers x+yi where the intensity of pixel (x,y) is greater than 120
    """
    import image
    NormalPart=0
    ComplexPart=0
    # data is a list of lists such that the intensity of pixel (x,y) is given by data[h-1-y][x]
    # where h = height of the image
    data = image.color2gray(image.file2image("img01.png"))
    output=set()
    for i in reversed(data):
            
        for ii in i:
            NormalPart+=1
            if ii<120:
                output.add(complex(NormalPart,ComplexPart))
        NormalPart=0
        ComplexPart+=1
    return output
            
            
            



