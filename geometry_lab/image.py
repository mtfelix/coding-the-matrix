""" 
Basic types:
file - a png file on disk
image - a list of list of pixels. pixels can be triples of RGB intensities, 
        or single grayscale values.
vec - a vector with domain {0..width-1}x{0..height-1}
display - not a type per se, but rather causing the type to be shown on screen

Functions convert between these formats, and also can write to temporary files
and display them with a web browser.
"""

# To do: check types of arguments, check that image has no alpha channel
# Note that right now, we ignore the alpha channel, but allow it. - @dbp

import png
import vec

# Native imports
import webbrowser
import tempfile
import os
import atexit

# Round color coordinate to nearest int and clamp to [0, 255]
def color_int(col):
    return max(min(round(col), 255), 0)

# utility conversions, between boxed pixel and flat pixel formats
# the png library uses flat, we use boxed.
def boxed2flat(row):
    return [color_int(x) for box in row for x in box]

def flat2boxed(row):
    # Note we skip every 4th element, thus eliminating the alpha channel
    return [tuple(row[i:i+3]) for i in range(0, len(row), 4)]

## Image conversions
def isgray(image):
    return type(image[0][0]) == int

def color2gray(image):
    """ Converts a color image to grayscale """
    # we use HDTV grayscale conversion as per https://en.wikipedia.org/wiki/Grayscale
    return [[int(0.2126*p[0] + 0.7152*p[1] + 0.0722*p[2]) for p in row]
                                                          for row in image]

def gray2color(image):
    """ Converts a grayscale image to color """
    return [[(p,p,p) for p in row] for row in image]

#extracting and combining color channels    
def rgbsplit(image):
	""" Converts an RGB image to a 3-element list of grayscale images, one for each color channel"""
	return [[[pixel[i] for pixel in row] for row in image] for i in (0,1,2)]

def rgpsplice(R,G,B):
	return [[(R[row][col],G[row][col],B[row][col]) for col in range(len(R[0]))] for row in range(len(R))]
	
## To and from files
def file2image(path):
    """ Reads an image into a list of lists of pixel values (tuples with 
        three values). This is a color image. """
    (w, h, p, m) = png.Reader(filename = path).asRGBA() # force RGB and alpha
    return [flat2boxed(r) for r in p]


def image2file(image, path):
    """ Writes an image in list of lists format to a file. Will work with
        either color or grayscale. """
    if isgray(image):
        img = gray2color(image)
    else:
        img = image
    with open(path, 'wb') as f:
        png.Writer(width=len(image[0]), height=len(image)).write(f, 
            [boxed2flat(r) for r in img])

## To and from vecs
def image2vec(image):
    """ Converts an image in list of lists format to a vector. Will work with
        either color or grayscale. """
    if isgray(image):
        D = {(x,y) for x in range(len(image[0]))
                   for y in range(len(image))}
        F = {(x,y):image[y][x] for (x,y) in D}
    else:
        D = {(x,y,c) for c in ['r','g','b']
                     for x in range(len(image[0]))
                     for y in range(len(image))}
        F = dict()
        for y in range(len(image)):
            for x in range(len(image[y])):
                F[(x,y,'r')] = image[y][x][0]
                F[(x,y,'g')] = image[y][x][1]
                F[(x,y,'b')] = image[y][x][2]
    return vec.Vec(D, F)

def vec2image(vec):
    """ Converts a vector to an image in list of lists format """
    image = []
    width = max(vec.D, key=lambda p: p[0])[0]
    height = max(vec.D, key=lambda p: p[1])[1]
    # check if grayscale
    e = vec.D.pop()
    vec.D.add(e)
    gray = len(e) == 2
    for y in range(height):
        row = []
        for x in range(width):
            if gray:
                row += [vec[(x,y)]]
            else:
                row += [(vec[(x,y,'r')], vec[(x,y,'g')], vec[(x,y,'b')])]
        image += [row]
    return image
    
## Shortcuts - files to vecs and vice-versa
def file2vec(path):
    """ Reads an image from a file and turns it into a vector """
    return image2vec(file2image(path))

def vec2file(vec, path):
    """ Reads an image from a file and turns it into a vector """
    image2file(vec2image(vec), path)

## Display functions
def image2display(image, browser=None):
    """ Stores an image in a temporary location and displays it on screen
        using a web browser. """
    path = create_temp('.png')
    image2file(image, path)
    hpath = create_temp('.html')
    with open(hpath, 'w') as h:
        h.writelines(["<html><body><img src='file://%s'/></body></html>" % path])
    openinbrowser('file://%s' % hpath, browser)

def vec2display(vec):
    """ Stores an image in vec format in a temporary location and displays it
        on screen using a web browser. """
    image2display(vec2image(vec))

def image2animate(image_array, delay=1, browser=None):
    """ Takes an array of images and displays them as an animation with `delay`
        seconds of pause between each one """
    hpath = create_temp('.html')
    with open(hpath, 'w') as h:
        h.writelines(
            ["<html>\n"
            ,"<script type='text/javascript'>\n"
            ,"function start() {\n"
            ,"var c = document.getElementById('container');\n"
            ,"var active = c.firstChild;\n"
            ,"active.style.zIndex = 1;\n"
            ,"function go() {\n"
            ,"  active.style.zIndex = 0;\n"
            ,"  active = active.nextSibling;\n"
            ,"  if (active != null) {\n"
            ,"    active.style.zIndex = 1;\n"
            ,"    window.setTimeout(go,%d);\n" % int(delay * 1000)
            ,"  }\n"
            ,"}\n"
            ,"window.setTimeout(go,%d);\n" % int(delay * 1000)
            ,"};\n"
            ,"</script>\n"

            ,"<body onload='start()'><div id='container' style='position: relative;'>"])
        for im in image_array:
            path = create_temp('.png')
            image2file(im, path)
            h.writelines(["<img src='%s' style='z-index: 0; position: absolute;'>" % path])
        h.writelines(["</div>\n"])
    openinbrowser('file://%s' % hpath, browser)

_browser = None

def setbrowser(browser=None):
    """ Registers the given browser and saves it as the module default.
        This is used to control which browser is used to display the plot.
        The argument should be a value that can be passed to webbrowser.get()
        to obtain a browser.  If no argument is given, the default is reset
        to the system default.

        webbrowser provides some predefined browser names, including:
        'firefox'
        'opera'

        If the browser string contains '%s', it is interpreted as a literal
        browser command line.  The URL will be substituted for '%s' in the command.
        For example:
        'google-chrome %s'
        'cmd "start iexplore.exe %s"'

        See the webbrowser documentation for more detailed information.

        Note: Safari does not reliably work with the webbrowser module,
        so we recommend using a different browser.
    """
    global _browser
    if browser is None:
        _browser = None  # Use system default
    else:
        webbrowser.register(browser, None, webbrowser.get(browser))
        _browser = browser

def getbrowser():
    """ Returns the module's default browser """
    return _browser

def openinbrowser(url, browser=None):
    if browser is None:
        browser = _browser
    webbrowser.get(browser).open(url)

# Create a temporary file that will be removed at exit
# Returns a path to the file
def create_temp(suffix='', prefix='tmp', dir=None):
    _f, path = tempfile.mkstemp(suffix, prefix, dir)
    os.close(_f)
    remove_at_exit(path)
    return path

# Register a file to be removed at exit
def remove_at_exit(path):
    atexit.register(os.remove, path)
