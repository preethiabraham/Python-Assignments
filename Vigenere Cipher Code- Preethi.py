# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:25:49 2021

@author: Preethi Abraham
"""

# Group 6: Preethi Susan Abraham and Alvin Varghese

#Vigenere Cipher Code

# P.S: This code works correctly only if I don't have any spaces in string1 and key and if len(key)<len(string1)


#Here we have asked the user to enter a string and a key
string1=input('Enter a string without any numbers or special characters').lower();
key=input('Enter a key string without any numbers or special characters').lower();


#a is a list which contains the numbers from 0 till the length of string1
a=list(range(len(string1)));

#Empty array which we will append the ASCII values of the alphabets of string1
indices=[];

#ord() gives the ASCII value of each alphabet in string1. 
#we have subtracted 97 from ord(string1[i]) in order to get the actual position of the alphabet in string1 i.e a=0, b=1...z=25
for i in a:
    index=ord(string1[i])-97;
    indices.append(index); #These values are appended to the indices array

#a is a list which contains the numbers from 0 till the length of key
b=list(range(len(key)));


#Empty array which we will append the ASCII values of the alphabets of key
key_indices=[];


#we have subtracted 97 from ord(key[i]) in order to get the actual position of the alphabet in key i.e a=0, b=1...z=25
for j in b:
    key_index=ord(key[j])-97;
    key_indices.append(key_index);

#since we want the len(key)=len(string1) we use the below lines of code
size=len(indices)-len(key_indices);
new=key_indices*size;
key_array_indices=new[0:len(indices)];


#we want to add the values of indices and key_array indices and store it in a new array called 'encrypt'
encrypt=[];
for i in range(len(indices)):
    e=indices[i]+key_array_indices[i];
    encrypt.append(e);

#However, in some cases, the result is greater than 25. So we subtract only those values with 26 to get values between 0 and 25 (i.e a to z)
#If the encrypt array contains -61, we assign -65 to it since the ascii value of a space is -65
for i in range(len(encrypt)):
    if encrypt[i]>25:
        encrypt[i]=encrypt[i]-26
    elif encrypt[i]==-61:
        encrypt[i]=-65;

#we convert the values from encrypt to characters by using chr(). we have added 97 because ASCII value of a is 97
encrypt_char=[]
for i in range(len(encrypt)):
    f=chr(encrypt[i]+97);
    encrypt_char.append(f);

#we print out the final cipher code
new_message=print(''.join(encrypt_char));