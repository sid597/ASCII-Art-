from PIL import Image

MAX_PIXEL_VALUE = 255
#  Get image you want to convert to ascii art

ascii_characters_list = '"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`".'


#  Convert image size this is done to because full blown art would not make sense

def resize(image):
    original_width, original_height = image.size

    adjusted_width = 440
    adjusted_height = int(adjusted_width * (float(original_height) / original_width))
    image = image.resize((adjusted_width, adjusted_height), Image.ANTIALIAS)
    return image


#  Create a  pixel matrix


def create_matrix(image):
    pixels = list(image.getdata())
    width, height = image.size
    pixels = [pixels[i * width: (i + 1) * width] for i in xrange(height)]
    return pixels


#  To print all the individual pixel values

# def print_pixel_values(matrix, matrix_height, matrix_width):
#     for pi in xrange(matrix_height):
#         for pj in xrange(matrix_width):
#             print matrix[pi][pj]


'''
 Now we need to convert this RGB Matrix into a brightness Matrix
 Brightness can be calculated in many ways

 https://stackoverflow.com/questions/596216/formula-to-determine-brightness-of-rgb-color
 Will first try with average then others and see which looks best

'''


def luminocity(tupl):
    return 0.299 * tupl[0] + 0.587 * tupl[1] + 0.114 * tupl[2]


def avg(tupl):
    return sum(tupl) / len(tupl)


def rgb_to_brightness_using(matrix, matrix_height, matrix_width, mthod):
    for pi in xrange(matrix_width):
        for pj in xrange(matrix_height):
            matrix[pi][pj] = mthod(matrix[pi][pj])
    return matrix

'''
    Now we need to convert this Brightness array to ascii character array
    Maths used to calculate which character to use is simple 
    Lets say the color range is 0-100 and character range is 0-20
     
'''


def convert_to_ascii(brightness_matrix, ascii_character_list = ascii_characters_list):
    ascii_matrix = []
    for row in brightness_matrix:
        ascii_row = []
        for j in row:
            ascii_row.append(ascii_character_list[int(j / MAX_PIXEL_VALUE * len(ascii_character_list)) - 1])
        ascii_matrix.append(ascii_row)
    return ascii_matrix



def print_ascii_image(matrix):
    for i in matrix:
        l = [p + p + p for p in i]
        print ''.join(l)


def runner(path_to_image):
    im = Image.open(path_to_image)
    im = resize(im)
    height, width = im.size
    rgb_matrix = create_matrix(im)
    brightness_matrix = rgb_to_brightness_using(rgb_matrix, height, width, luminocity)
    ascii_matrix = convert_to_ascii(brightness_matrix)
    print_ascii_image(ascii_matrix)


if __name__ == '__main__':
    import sys

    path = sys.argv[-1]
    if path == 'ascii.py':
        print "Provide path to an image"
    else:
        runner(path)

# def print_ascii_matrix(ascii_matrix):
#     for row in ascii_matrix:
#         l = [p*3 for p in row]
#         print ''.join(row)

# print print_ascii_matrix(convert_to_ascii(pixels,ascii_characters_list))


# from PIL import Image
#
# ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
# ASCII_CHARS = ASCII_CHARS[::-1]
#
# '''
# method resize():
#     - takes as parameters the image, and the final width
#     - resizes the image into the final width while maintaining aspect ratio
# '''
# def resize(image, new_width=100):
#     (old_width, old_height) = image.size
#     aspect_ratio = float(old_height)/float(old_width)
#     new_height = int(aspect_ratio * new_width)
#     new_dim = (new_width, new_height)
#     new_image = image.resize(new_dim)
#     return new_image
# '''
# method grayscalify():
#     - takes an image as a parameter
#     - returns the grayscale version of image
# '''
# def grayscalify(image):
#     return image.convert('L')
#
# '''
# method modify():
#     - replaces every pixel with a character whose intensity is similar
# '''
# def modify(image, buckets=25):
#     initial_pixels = list(image.getdata())
#     new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
#     return ''.join(new_pixels)
#
# '''
# method do():
#     - does all the work by calling all the above functions
# '''
# def do(image, new_width=100):
#     image = resize(image)
#     image = grayscalify(image)
#
#     pixels = modify(image)
#     len_pixels = len(pixels)
#
#     # Construct the image from the character list
#     new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]
#
#     return '\n'.join(new_image)
#
# '''
# method runner():
#     - takes as parameter the image path and runs the above code
#     - handles exceptions as well
#     - provides alternative output options
# '''
# def runner(path):
#     image = None
#     try:
#         image = Image.open(path)
#     except Exception:
#         print("Unable to find image in",path)
#         #print(e)
#         return
#     image = do(image)
#
#     # To print on console
#     print(image)
#
#     # Else, to write into a file
#     # Note: This text file will be created by default under
#     #       the same directory as this python file,
#     #       NOT in the directory from where the image is pulled.
#     f = open('img.txt','w')
#     f.write(image)
#     f.close()
#
# '''
# method main():
#     - reads input from console
#     - profit
# '''
# if __name__ == '__main__':
#     import sys
#     import urllib.request
#     if sys.argv[1].startswith('http://') or sys.argv[1].startswith('https://'):
#         urllib.request.urlretrieve(sys.argv[1], "asciify.jpg")
#         path = "asciify.jpg"
#     else:
#         path = sys.argv[1]
#     runner(path)
#
#
#
#
#
#
#
