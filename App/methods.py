import math

import matplotlib.pyplot as plt

import numpy as np
from numpy import array, int32



def moyenneGris(matrice):
    somme = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            somme += int(matrice[i][j])
    return somme / (len(matrice) * len(matrice[0]))


def ecartypeGris(matrice):
    somme = 0
    moy = moyenneGris(matrice)
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            somme += (int(matrice[i][j]) - moy) ** 2

    return np.sqrt(somme / (len(matrice) * len(matrice[0])))


def pgmread(filename):
    print(filename)
    f = open(filename, 'r')
    # Read header information
    count = 0
    height = 0
    width = 0
    while count < 3:
        line = f.readline()
        if line[0] == '#':  # Ignore comments
            continue
        count = count + 1
        if count == 1:  # Magic num info
            magicNum = line.strip()
            if magicNum != 'P2' and magicNum != 'P5':
                f.close()
                print('Not a valid PGM file')
                exit()
        elif count == 2:  # Width and Height
            [width, height] = (line.strip()).split()
            width = int(width)
            height = int(height)
        elif count == 3:  # Max gray level
            maxVal = int(line.strip())
    # Read pixels information
    print(height,width)
    img = []
    buf = f.read()
    elem = buf.split()
    for i in range(height):
        tmpList = []
        for j in range(width):
            tmpList.append(elem[i * width + j])
        img.append(tmpList)
    return [img, height, width]

def convertToPgm(matrix):
    width = matrix[2]
    height = matrix[1]
    img = []
    for i in range(height):
        tmpList = []
        for j in range(width):
            s = matrix[0][i][j * 3 + 1]  # + matrix[0][i][j*3+1] + matrix[0][i][j*3 +2]
            tmpList.append(s)
        img.append(tmpList)
    return [img, width, height]


def convertToPpm(matrix):
    width = matrix[2]
    height = matrix[1]
    img = []

    for i in range(height):
        tmpList = []
        for j in range(width):
            tmpList.append(matrix[0][i][j])
            tmpList.append(matrix[0][i][j])
            tmpList.append(matrix[0][i][j])
        img.append(tmpList)
    return [img, height, width]

def ppmread(filename):
    f = open(filename, 'r')
    # Read header information
    count = 0
    while count < 3:
        line = f.readline()
        if line[0] == '#':  # Ignore comments
            continue
        count = count + 1
        if count == 1:  # Magic num info
            magicNum = line.strip()
            if magicNum != 'P3' and magicNum != 'P6':
                f.close()
                print('Not a valid PPM file')
                exit()
        elif count == 2:  # Width and Height
            [width, height] = (line.strip()).split()
            width = int(width)
            height = int(height)
        elif count == 3:  # Max gray level
            maxVal = int(line.strip())
    # Read pixels information
    img = []
    buf = f.read()
    elem = buf.split()
    for i in range(height):
        tmpList = []
        for j in range(width * 3):
            tmpList.append(elem[i * width * 3 + j])
        img.append(tmpList)
    return [img, height, width]



def ppmwrite(img, filename, maxVal=255, magicNum='P3'):
    f = open(filename + ".ppm", 'w+')
    width = img[2]
    height = img[1]
    f.write(magicNum + '\n')
    f.write(str(width) + ' ' + str(height) + '\n')
    f.write(str(maxVal) + '\n')
    for i in range(height):
        for j in range(width * 3):
            f.write(str(img[0][i][j]) + ' ')
    f.close()



def pgmwrite(img, filename, maxVal=255, magicNum='P2'):
    f = open(filename + ".pgm", 'w')
    file = open(filename + ".txt", "w+")
    content = str(img)
    file.write(content)
    file.close()
    height = len(img)
    width = len(img[0])
    f.write(magicNum + '\n')
    f.write(str(width) + ' ' + str(height) + '\n')
    f.write(str(maxVal) + '\n')
    for i in range(height):
        for j in range(width):
            f.write(str(img[i][j]) + ' ')
    f.close()


def histogram(img):
    arr = np.zeros(256)
    for el in img:
        for num in el:
            arr[int(num)] += 1;
    return arr


def cumule(img):
    arr = histogram(img)
    arr_cumul = np.zeros(256)
    somm = 0
    for i, el in enumerate(arr):
        somm += el
        arr_cumul[i] = somm
    return arr_cumul

def histo_egal(img):
    p = []
    pc = []
    a = []
    n1 = []
    arr = histogram(img)
    arr_cumul = cumule(img)
    for value in arr:
        p.append(value / sum(arr))
    for value in arr_cumul:
        pc.append(value / sum(arr))
    for index in range(len(pc)):
        a.append(255 * pc[index])
        n1.append(math.floor(a[index]))
    new_arr = [0] * len(arr)
    for index in range(len(arr)):
        if n1[index] < len(arr):
            new_arr[n1[index]] = new_arr[n1[index]] + arr[index]
    for i in range(len(img)):
        for j in range(len(img[0])):
           img[i][j] = n1[int(img[i][j])]
    return img

def seuiller(image : str,seuil_rouge , seuil_vert, seuil_bleu,operateur):
    img = ppmread(image)
    print(img[1],img[2])
    for i in range(img[1]):
        for j in range(img[2]):
            if(operateur == 'et'):
                if (int(img[0][i][j * 3]) > seuil_rouge and int(img[0][i][j * 3 + 1]) > seuil_vert and int(img[0][i][j * 3 + 2]) > seuil_bleu  ):
                    img[0][i][j * 3] = 255
                    img[0][i][j * 3 + 1] = 255
                    img[0][i][j * 3 + 2] = 255
                else:
                    img[0][i][j * 3] = 0
                    img[0][i][j * 3 + 1] = 0
                    img[0][i][j * 3 + 2] = 0
            elif(operateur == 'ou'):
                if (int(img[0][i][j * 3]) > seuil_rouge or int(img[0][i][j * 3 + 1]) > seuil_vert or int(img[0][i][j * 3 + 2]) > seuil_bleu):
                    img[0][i][j * 3] = 255
                    img[0][i][j * 3 + 1] = 255
                    img[0][i][j * 3 + 2] = 255
                else:
                    img[0][i][j * 3] = 0
                    img[0][i][j * 3 + 1] = 0
                    img[0][i][j * 3 + 2] = 0
            else:
                if (int(img[0][i][j * 3]) > seuil_rouge):
                    img[0][i][j * 3] = 255
                else:
                    img[0][i][j * 3] = 0
                if (int(img[0][i][j * 3 + 1]) > seuil_vert):
                    img[0][i][j * 3 + 1] = 255
                else:
                    img[0][i][j * 3 + 1] = 0
                if (int(img[0][i][j * 3 + 2]) > seuil_bleu):
                    img[0][i][j * 3 +2 ] = 255
                else:
                    img[0][i][j * 3 +2] = 0

    ppmwrite(img,'out-'+operateur)



# seuiller("peppers.ppm",50,50,50,'et')
# seuiller("peppers.ppm",50,50,50,'ou')
# seuiller("peppers.ppm",50,50,50,'normale')
# appliquer seuillage et ou sur image seuillée

