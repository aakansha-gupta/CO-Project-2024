import sys
#dictionary for opcodes
opcodes = {"add":"0110011", "sub":"0110011", "sll":"0110011", "slt":"0110011", "sltu":"0110011", "xor":"0110011", 
           "srl":"0110011", "or":"0110011", "and":"0110011", "lw":"0000011", "addi":"0010011", "sltiu":"0010011", 
           "jalr":"1100111", "sw":"0100011", "beq":"1100011", "bne":"1100011", "blt":"1100011", "bge":"1100011", 
           "bltu":"1100011", "bgeu":"1100011", "lui":"0110111", "auipc":"0010111", "jal":"1101111",}

#list for different types of instructions - 
r_type_inst = ["add", "sub", "sll", "slt", "sltu", "xor", "srl", "or", "and"]
i_type_inst = ["lw", "addi", "sltiu", "jalr"]
s_type_inst = ["sw"]
b_type_inst = ["beq", "bne", "blt", "bge", "bltu", "bgeu"]
u_type_inst = ["lui", "auipc"]
j_type_inst = ["jal"]

#decimal to 7-bit binary conversion 
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

#decimal to original-bit binary conversion 
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

#binary to decimal conversion 
def binary_decimal(binary):
    l = len(binary) - 1
    val = 0
    for i in binary:
        val += (int(i)) * (2 ** l)
        l -= 1
    return val

#binary to decimal point number conversion
def fbinary_decimal(binary):
    val = 0
    for i in range(len(binary)):
        val += (int(binary[i])) * (2 ** -(i+1))
    return val

def floattobin(num): # num is a float number in decimal system
    intpart = int(num//1)
    fracpart = float(num%1)
    intbinary = dec_binf(intpart)
    fracbinary = ''
    while fracpart > 0:
        fracpart *= 2
        if fracpart >= 1:
            fracbinary+="1"
            fracpart-=1
        else:
            fracbinary+="0"
    binary = intbinary + "." + fracbinary
    return binary

def bintofloat(bin): # bin is a binary representation
    if "." in bin:
        for i in range(len(bin)):
            if bin[i]==".":
                intbinary = bin[:i]
                fracbinary = bin[i+1:]
        intpart = bin_dec(intbinary)
        fracpart = fbin_dec(fracbinary)
        val = intpart + fracpart
        return val
    else: 
        val = bin_dec(bin)
        return val
