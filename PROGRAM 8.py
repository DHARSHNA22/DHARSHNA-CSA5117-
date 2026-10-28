plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyword = input("Enter the keyword: ").upper()

cipher = ""

for ch in keyword + plain:
    if ch.isalpha() and ch not in cipher:
        cipher += ch

print("Plain alphabet : ", plain)
print("Cipher alphabet:", cipher)

text = input("Enter the plaintext: ").upper()
result = ""

for ch in text:
    if ch in plain:
        result += cipher[plain.index(ch)]
    else:
        result += ch

print("Encrypted text:", result)
