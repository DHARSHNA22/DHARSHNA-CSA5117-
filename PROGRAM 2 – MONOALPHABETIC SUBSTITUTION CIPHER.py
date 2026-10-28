plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

text = input("Enter the plaintext: ")
result = ""

for ch in text:
    if ch.isalpha():
        index = plain.index(ch.upper())
        result += cipher[index]
    else:
        result += ch

print("Encrypted text:", result)
