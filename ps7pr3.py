#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import compare_images
from hmcpng import load_pixels
from hmcpng import save_pixels

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

def grayscale(pixels):
    """creates a new 2-D list of pixels for a grayscale version of the pixels
    provided in the input list
    """
    new_image = green_image(len(pixels),len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            new_value = brightness(pixels[r][c])
            new_pixel = [new_value, new_value, new_value]
            new_image[r][c] = new_pixel
    return new_image


def mirror_vert(pixels):
    """returns a 2-D list where pixels has been mirrored 
    vertically
    """
    new_image = green_image(len(pixels),len(pixels[0]))
    half_vert = len(pixels)//2
    for r in range(half_vert):
        for c in range(len(pixels[0])):
            new_image[r][c] = pixels[r][c]
    for r in range(half_vert,len(pixels)):
        for c in range(len(pixels[0])):
            new_image[r][c] = pixels[len(pixels)-r-1][c]
    
    return new_image


def flip_horiz(pixels):
    """returns a 2-D list where pixels has been flipped horizontally
    """
    new_image = green_image(len(pixels),len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            new_image[r][c] = pixels[r][len(pixels[0])-1-c]
    return new_image


def extract(pixels, rmin, rmax, cmin, cmax):
    """takes the 2-D list pixels and returns a new 2-D list that
    represents the portion of the original image that is specified by the other
    four parameters: rows rmin to rmax, columns cmin to cmax, not including max's
    """
    new_image = green_image(rmax-rmin, cmax-cmin)
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            new_image[r-rmin][c-cmin] = pixels[r][c]
    return new_image
    
        
        

