from image_mat_util import *
from geometry_lab import *
import math
pmat_cmat = file2mat("pic.png")
#mat2display(pmat_cmat[0], pmat_cmat[1])

#print(translation(2,3))
#print(rotation(math.pi/6))


#mat2display(rotate_about(225,225,math.pi/2)*pmat_cmat[0],scale_color(1,0.5,0.3)*pmat_cmat[1])
mat2display(reflect_about((0,115),(225,115))*pmat_cmat[0],pmat_cmat[1])

