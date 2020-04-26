import image
from Matrix import Matrix
def png2graymatrix(filename):
    """
    takes a png file and returns a Matrix object of the pixels 
    INPUT: filename - the path and filename of the png file
    OUTPUT: a Matrix object with dimensions m x n, assuming the png file has width = n and height = m, 
    """
    #FIXME: a single line of code should go here
    image_data=image.file2image(filename)
    if not image.isgray(image_data):
        image_data = image.color2gray(image_data)#FIXME: make the image grayscale
    return Matrix(image_data) #FIXME


def graymatrix2png(img_matrix, path):
    """
    returns a png file created using the Matrix object, img_matrix
    INPUT: 
        * img_matrix - a Matrix object where img_matrix[i][j] is the intensity of the (i,j) pixel
        * path - the location and name under which to save the created png file 
    OUTPUT: 
        * a png file
    """
    return image.image2file(img_matrix.Rowsp,path)
    pass
M = png2graymatrix("img11.png")  # matrix for img11.png
F = png2graymatrix("img02.png")  # matrix for img02.png
C = M * 0.5 + F * 0.5
graymatrix2png(C, "mixedfaces.png") 
