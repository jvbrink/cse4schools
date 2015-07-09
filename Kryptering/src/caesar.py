def text2ascii(message):
    numbers = []
    for char in message:
        numbers.append(ord(char))
    return numbers

def ascii2text(message):
    letters = ""
    for number in message:
        letters += chr(number)
    return letters

def caesarcipher(message, key):
    for i in range(len(message)):
        n = message[i]
        if chr(n).isalpha():
            
            if 65 < n < 90:
                n += key
                if n > 90:
                    n -= 26
                elif n < 65:
                    n += 26
            else:
                n += key
                if n > 122:
                    n -= 26
                    print n
                elif n < 9:
                    n += 26
        message[i] = n


def decrypt(message, key):
    for i in range(len(message)):
        n = message[i]
        if chr(n).isalpha():
            if 65 < n < 90:
                n -= key    
                if n > 90:
                    n -= 26
                elif n < 65:
                    n += 26
            else:
                n -= key    
                if n > 122:
                    n -= 26
                elif n < 97:
                    n += 26
        message[i] = n

num = text2ascii("Hei! Mitt navn er Jonas")
caesarcipher(num, 5)
print ascii2text(num) 

for i in range(27):
    a = num
    decrypt(a, 1) 
    print i+1, ascii2text(a)
