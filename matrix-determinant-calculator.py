print('Welcome to the Determinant Calculator.')
print('This program will calculate the determinant of a 2x2, 3x3, or 4x4 matrices.')
validSizes = [2,3,4]

# Get the size of the matrix
size = int(input('Enter the size of the matrix (2,3, or 4): '))

while (size not in validSizes):
    print('Please enter a valid matrix size (2,3, or 4)')
    size = int(input('Enter the size of the matrix (2,3, or 4): '))

def calculate2x2(a11, a12, a21, a22):
    result = (a22 * a11) - (a21 * a12)  
    return result

def calculate3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    result = (a11 * ( (a33 * a22) - (a32 * a23) )) + ( (-1 * a12) * ((a33 * a21) - (a31 * a23)) ) + (a13 * ((a32 * a21) - (a31 * a22)))
    return result

def calculate4x4(a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44):
    first3x3 = calculate3x3(a22, a23, a24, a32, a33, a34, a42, a43, a44)
    second3x3 = calculate3x3(a21, a23, a24, a31, a33, a34, a41, a43, a44)
    third3x3 = calculate3x3(a21, a22, a24, a31, a32, a34, a41, a42, a44)
    fourth3x3 = calculate3x3(a21, a22, a23, a31, a32, a33, a41, a42, a44)
    result = (a11 * first3x3) - (a12 * second3x3) + (a13 * third3x3) - (a14 * fourth3x3) 
    return result



if (size == 2):
    a11 = float(input('a11: '))
    a12 = float(input('a12: '))
    a21 = float(input('a21: '))
    a22 = float(input('a22: '))
    result = calculate2x2(a11, a12, a21, a22)
    print('Your matrix is: ')
    print(a11, a12)
    print(a21, a22)

elif (size == 3):
    a11 = float(input('a11: '))
    a12 = float(input('a12: '))
    a13 = float(input('a13: '))
    a21 = float(input('a21: '))
    a22 = float(input('a22: '))
    a23 = float(input('a22: '))
    a31 = float(input('a31: '))
    a32 = float(input('a32: '))
    a33 = float(input('a33: '))
    result = calculate3x3(a11, a12, a13, a21, a22, a23, a31, a32, a33)
    print('Your matrix is: ')
    print(a11, a12, a13)
    print(a21, a22, a23)
    print(a31, a32, a33)

else:
    a11 = float(input('a11: '))
    a12 = float(input('a12: '))
    a13 = float(input('a13: '))
    a14 = float(input('a14: '))
    a21 = float(input('a21: '))
    a22 = float(input('a22: '))
    a23 = float(input('a23: '))
    a24 = float(input('a24: '))
    a31 = float(input('a31: '))
    a32 = float(input('a32: '))
    a33 = float(input('a33: '))
    a34 = float(input('a34: '))
    a41 = float(input('a41: '))
    a42 = float(input('a42: '))
    a43 = float(input('a43: '))
    a44 = float(input('a44: '))
    result = calculate4x4(a11, a12, a13, a14, a21, a22, a23, a24, a31, a32, a33, a34, a41, a42, a43, a44)
    print('Your matrix is: ')
    print(a11, a12, a13, a14)
    print(a21, a22, a23, a24)
    print(a31, a32, a33, a34)
    print(a41, a42, a43, a44)



print('Determinant of this matrix is: ' + str(result))



    