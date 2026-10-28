def decrypt(ciphertext):
    result = ""

    a_inverse = 9
    b = 15

    for ch in ciphertext:
        if ch.isalpha():
            c = ord(ch.upper()) - ord('A')
            p = (a_inverse * (c - b)) % 26
            result += chr(p + ord('A'))
        else:
            result += ch

    return result


ciphertext = input("Enter the ciphertext: ")

plaintext = decrypt(ciphertext)

print("Decrypted text:", plaintext)
