# -*- coding: utf-8 -*-

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            n = alfabet.index(char)
            e = (n+key) % len(alfabet)
            print e
            print len(alfabet)
            ciphertext += alfabet[e]
        else:
            ciphertext += char
    return ciphertext

def decrypt(cipher, key):
    plaintext = ""
    for char in ciphertext:
        e = alfabet.index(char)
        n = (e-key) % len(alfabet)
        plaintext += alfabet[n]
    return ciphertext

print encrypt("THE PRIZE FOR DECODING THIS MESSAGE IS CANDY", 10)
print encrypt("ATTACK AT DAWN", 9)