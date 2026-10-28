def encrypt(plaintext, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in plaintext:
        if ch.isalpha():
            p = ord(ch.upper()) - ord('A')
            k = ord(key[j % len(key)]) - ord('A')

            c = (p + k) % 26
            result += chr(c + ord('A'))
            j += 1
        else:
            result += ch

    return result


plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

ciphertext = encrypt(plaintext, key)

print("Encrypted text:", ciphertext)

