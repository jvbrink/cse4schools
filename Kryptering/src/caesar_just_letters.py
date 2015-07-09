# -*- coding: utf-8 -*-

alfabet = "abcdefghijklmnopqrstuwxyzæøå"

plaintext = "jonas"

print "Gjør beskjeden om til tall"
for char in plaintext:
    print "%s ---> %d" % (char, alfabet.index(char))

print "\nKrypter tallene"
for char in plaintext:
    p = alfabet.index(char)
    c = (p + 5) % 29
    print "(%2d + 5) %% 29 ---> %d" % (p, c)

print "\nGjør de krypterte tallene tilbake til bokstaver"
ciphertext = ""
for char in plaintext:
    p = alfabet.index(char)
    c = (p + 5) % 29
    ciphertext += alfabet[c]    
    print "%2d ---> %s" % (c, alfabet[c])

print "\nDa har vi endret besjeden som dette"
print "%s ---> %s" % (plaintext, ciphertext)


