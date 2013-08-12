""" A module for working with images in matrix format.
    An image is represented by two matrices, representing points and colors.
    The points matrix has row labels {'x', 'y', 'u'} and column labels (0,0) through (w, h), inclusive,
    where (w, h) are the width and height of the original image
    The colors matrix has row labels {'r', 'g', 'b'} and column labels (0,0) through (w-h, h-1).

    The column labels for these matrices represent "lattice points" on the original image.
    For pixel (i,j) in the original image, the (i,j) column in the colors matrix represents
    the pixel color and the (i,j), (i+1, j), (i+1, j+1), and (i, j+1) columns in the points
    matrix represent the boundary of the pixel region
    """

import mat
import image

from image import setbrowser, getbrowser

# Native imports
import math

def file2mat(path, row_labels = ('x', 'y', 'u')):
    """input: a filepath to an image in .png format
    output: the pair (points, matrix) of matrices representing the image."""
    return image2mat(image.file2image(path), row_labels)

def image2mat(image, row_labels = ('x', 'y', 'u')):
    """ input: an image in list-of-lists format
        output: a pair (points, colors) of matrices representing the image.
        Note: The input list-of-lists can consist of either integers n [0, 255] for grayscale
        or 3-tuple of integers representing the rgb color coordinates
    """
    h = len(image)
    w = len(image[0])
    rx, ry, ru = row_labels
    ptsD = (set(row_labels), {(x,y) for x in range(w+1) for y in range(h+1)})
    ptsF = {}
    colorsD = ({'r', 'g', 'b'}, {(x,y) for x in range(w) for y in range(h)})
    colorsF = {}
    for y in range(h+1):
        for x in range(w+1):
            pt = (x,y)
            ptsF[(rx, pt)] = x
            ptsF[(ry, pt)] = y
            ptsF[(ru, pt)] = 1
            if x < w and y < h:
                col = image[y][x]
                if type(col) is int:
                    red, green, blue = col, col, col
                else:
                    red, green, blue = col
                colorsF[('r', pt)] = red
                colorsF[('g', pt)] = green
                colorsF[('b', pt)] = blue
    return mat.Mat(ptsD, ptsF), mat.Mat(colorsD, colorsF)

# Expand a polygon around its center
def _expandpoly(poly):
    xs, ys = zip(*poly)
    xc = sum(xs) / len(xs)
    yc = sum(ys) / len(ys)
    dxs = [x - xc for x in xs]
    dys = [y - yc for y in ys]
    alpha = 0.625 / max(math.hypot(*d) for d in zip(dxs, dys))
    return [(x + alpha * dx, y + alpha * dy) for (x, y, dx, dy) in zip(xs, ys, dxs, dys)]

def mat2display(pts, colors, row_labels = ('x', 'y', 'u'),
                scale=1, xmin=0, ymin=0, xmax=None, ymax=None,
                crosshairs=False, expand=False, browser=None):
    """ input: matrix pts and matrix colors representing an image
        result: Displays the image in a web browser

        Optional arguments:
        
        row_labels - A collection specifying the points matrix row labels,
        in order.  The first element of this collection is considered the x
        coordinate, the second is the y coordinate, and the third is the u
        coordinate, which is assumed to be 1 for all points.

        scale - The display scale, in pixels per image coordinate unit

        xmin, ymin, xmax, ymax - The region of the image to display.  These can
        be set to None to use the minimum/maximum value of the coordinate
        instead of a fixed value.

        crosshairs - Setting this to true displays a crosshairs at (0, 0) in
        image coordinates

        expand - If True, increases the size of each pixel slightly to prevent
        gaps, at the cost of some loss of sharpness.

        browser - A browser string to be passed to webbrowser.get().
        Overrides the module default, if any has been set.
    """
    rx, ry, ru = row_labels
    if ymin is None:
        ymin = min(v for (k, v) in pts.f.items() if k[0] == ry)
    if xmin is None:
        xmin = min(v for (k, v) in pts.f.items() if k[0] == rx)
    if ymax is None:
        ymax = max(v for (k, v) in pts.f.items() if k[0] == ry)
    if xmax is None:
        xmax = max(v for (k, v) in pts.f.items() if k[0] == rx)

    # Include (0, 0) in the region
    if crosshairs:
        ymin = min(ymin, 0)
        xmin = min(xmin, 0)
        ymax = max(ymax, 0)
        xmax = max(xmax, 0)


    hpath = image.create_temp('.html')
    with open(hpath, 'w') as h:
        h.writelines(
            ['<!DOCTYPE html>\n',
            '<head> <title>image</title> </head>\n',
            '<body>\n',
            '<svg height="%s" width="%s" xmlns="http://www.w3.org/2000/svg">\n' % ((ymax-ymin) * scale, (xmax-xmin) * scale),
            '<g transform="scale(%s) translate(%s, %s) ">\n' % (scale, -xmin, -ymin)])

        # go through the quads, writing each one to canvas
        for l in colors.D[1]:
            lx, ly = l
            r = image.color_int(colors[('r', l)])
            g = image.color_int(colors[('g', l)])
            b = image.color_int(colors[('b', l)])

            # coords of corners
            x0 = pts[(rx, l)]
            y0 = pts[(ry, l)]
            x1 = pts[(rx, (lx+1, ly))]
            y1 = pts[(ry, (lx+1, ly))]
            x2 = pts[(rx, (lx+1, ly+1))]
            y2 = pts[(ry, (lx+1, ly+1))]
            x3 = pts[(rx, (lx, ly+1))]
            y3 = pts[(ry, (lx, ly+1))]

            if(expand):
                (x0, y0), (x1, y1), (x2, y2), (x3, y3) = _expandpoly([(x0, y0), (x1, y1), (x2, y2), (x3, y3)])

            h.writelines(['<polygon points="%s, %s %s, %s, %s, %s %s, %s" fill="rgb(%s, %s, %s)" stroke="none" />\n'
                         % (x0, y0, x1, y1, x2, y2, x3, y3, r, g, b)])

        # Draw crosshairs centered at (0, 0)
        if crosshairs:
            h.writelines(
                ['<line x1="-50" y1="0" x2="50" y2="0" stroke="black" />\n',
                '<line x1="0" y1="-50" x2="0" y2="50" stroke="black" />\n',
                '<circle cx="0" cy="0" r="50" style="stroke: black; fill: none;" />\n'])

        h.writelines(['</g></svg>\n', '</body>\n', '</html>\n'])

    image.openinbrowser('file://%s' % hpath, browser)
