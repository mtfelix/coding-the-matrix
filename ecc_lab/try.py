

from vec import Vec
from mat import Mat
from matutil import *
from bitutil import noise
from GF2 import one
from ecc_lab import *
from bitutil import *
H = listlist2mat([[0,0,0,one,one,one,one],[0,one,one,0,0,one,one],[one,0,one,0,one,0,one]])
non_codeword = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one, 6:one})
#print(find_error(H*non_codeword))
code_word = Vec({0,1,2,3,4,5,6}, {0: one, 1:0, 2:one, 3:one, 4:0, 5:one})
R = listlist2mat([[0,0,0,0,0,0,one],[0,0,0,0,0,one,0],[0,0,0,0,one,0,0],[0,0,one,0,0,0,0]])
#print(  R * code_word )

#Vec({0, 1, 2, 3, 4, 5, 6},{3: one})

str = "i am jiang hongFei @ 2013!"
bits = str2bits(str)
str_back = bits2str(bits)
print(str)
print(len(str))
print(bits)
print()
print(len(bits))

matrix_of_bits = bits2mat(bits)
print(matrix_of_bits)

bits_back = mat2bits(matrix_of_bits)
print(bits_back)

print(str_back)
print()
print(len(str_back))


# try the noise
P = bits2mat(str2bits(str))
C = G*P
f = 0.5
E = noise(C, f)
C_tilde = C + E
C_correct = correct(C_tilde)
codeword_decode = R*C_correct
Rcv_str = bits2str(mat2bits(R*C_tilde))
ham_correct_str = bits2str(mat2bits(codeword_decode))
print("[original string]:")
print(str)
print("Prob is ",f)
print("[rcved string]:")
print(Rcv_str.encode('utf-8'))
print("[hamming corrected string]:")
print(ham_correct_str.encode('utf-8'))



