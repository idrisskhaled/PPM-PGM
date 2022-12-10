import math

import matplotlib.pyplot as plt

import numpy as np
from numpy import array, int32



def moyenneGris(matrice):
    somme = 0
    for i in range(0, matrice.shape[0]):
        for j in range(0, matrice.shape[1]):
            somme += matrice[i][j]

    return somme / (matrice.shape[0] * matrice.shape[1])


def ecartypeGris(matrice):
    somme = 0
    moy = moyenneGris(matrice)
    for i in range(0, matrice.shape[0]):
        for j in range(0, matrice.shape[1]):
            somme += (matrice[i][j] - moy) ** 2

    return np.sqrt(somme / (matrice.shape[0] * matrice.shape[1]))


def pgmread(filename):
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
    img = []
    buf = f.read()
    elem = buf.split()
    if len(elem) != width * height:
        print('Error in number of pixels')
        exit()
    for i in range(height):
        tmpList = []
        for j in range(width):
            tmpList.append(elem[i * width + j])
        img.append(tmpList)
    return (array(img), width, height)

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
    return [array(img), height, width]



def ppmwrite(img, filename, maxVal=255, magicNum='P3'):
    f = open(filename + ".ppm", 'w')
    file = open(filename + ".txt", "w+")
    content = str(img)
    file.write(content)
    file.close()
    width = img[2]
    height = img[1]
    f.write(magicNum + '\n')
    f.write(str(width) + ' ' + str(height) + '\n')
    f.write(str(maxVal) + '\n')
    for i in range(height):
        for j in range(width * 3):
            f.write(str(img[0][i][j]) + ' ')
        f.write('\n')
    f.close()



def pgmwrite(img, filename, maxVal=255, magicNum='P2'):
    img = int32(img).tolist()
    f = open(filename + ".pgm", 'w')
    file = open(filename + ".txt", "w+")
    content = str(img)
    file.write(content)
    file.close()
    width = 0
    height = 0
    for row in img:
        height = height + 1
        width = len(row)
    f.write(magicNum + '\n')
    f.write(str(width) + ' ' + str(height) + '\n')
    f.write(str(maxVal) + '\n')
    for i in range(height):
        count = 1
        for j in range(width):
            f.write(str(img[i][j]) + ' ')
            if count >= 17:
                # No line should contain gt 70 chars (17*4=68)
                # Max three chars for pixel plus one space
                count = 1
                f.write('\n')
            else:
                count = count + 1
        f.write('\n')
    f.close()


def histo(img):
    arr = np.zeros(256)
    for el in img:
        for num in el:
            arr[num] += 1;
    return arr


def cumule(img):
    arr = histo(img)
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
    arr = histo(img)
    #print(arr)
    arr_cumul = cumule(img)
    #print(arr_cumul)
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
    new_img = [len(img[0]) * [0]] * len(img)
    for i,line in enumerate(img):
        for j,column in enumerate(line):
           new_img[i][j] = n1[column]

    return new_img

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

    ppmwrite(img,'peppers-out-'+operateur)



# seuiller("peppers.ppm",50,50,50,'et')
# seuiller("peppers.ppm",50,50,50,'ou')
# seuiller("peppers.ppm",50,50,50,'normale')
# appliquer seuillage et ou sur image seuillée

