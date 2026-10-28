def create_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    letters = ""

    for ch in key + alphabet:
        if ch.isalpha() and ch not in letters:
            letters += ch

    return [list(letters[i:i+5]) for i in range(0, 25, 5)]


def decrypt(ciphertext, matrix):
    result = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        r1 = c1 = r2 = c2 = 0

        for r in range(5):
            for c in range(5):
                if matrix[r][c] == a:
                    r1, c1 = r, c
                if matrix[r][c] == b:
                    r2, c2 = r, c

        if r1 == r2:
            result += matrix[r1][(c1 - 1) % 5]
            result += matrix[r2][(c2 - 1) % 5]
        elif c1 == c2:
            result += matrix[(r1 - 1) % 5][c1]
            result += matrix[(r2 - 1) % 5][c2]
        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


key = input("Enter the keyword: ")
ciphertext = input("Enter the ciphertext: ").upper()
ciphertext = ''.join(ch for ch in ciphertext if ch.isalpha())
ciphertext = ciphertext.replace("J", "I")

matrix = create_matrix(key)

print("Decrypted text:", decrypt(ciphertext, matrix))
