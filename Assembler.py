import sys

def decimal_binary(dec):
    dec = int(dec)
    binary = ''
    while dec != 0:
        if dec % 2 == 0:
            binary += '0'
        if dec % 2 == 1:
            binary += '1'
        dec = dec // 2

    unused = 7 - len(binary)
    binary = binary[-1::-1]
    binary = '0' * unused + binary
    return binary

def decimal_binaryf(dec):
    dec = int(dec)
    binary = ''
    while dec != 0:
        if dec % 2 == 0:
            binary += '0'
        if dec % 2 == 1:
            binary += '1'
        dec = dec // 2
    binary = binary[-1::-1]
    return binary

def binary_decimal(binary):
    l = len(binary) - 1
    val = 0
    for i in binary:
        val += (int(i)) * (2 ** l)
        l -= 1
    return val

def fbinary_decimal(binary):
    val = 0
    for i in range(len(binary)):
        val += (int(binary[i])) * (2 ** -(i+1))
    return val
