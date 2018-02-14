alphabet = "abcdefghijklmnopqrstuvwxyz !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`{|}~"
key = "qwertyuioplkjhgfdsazxcvbn/m'].;[,?\"}>:{<\\|=_+-0 192837465)!(@*#&$^%`~PLQAOKWSIJEDUHRFYGTZMXNCBV"

def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""
    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result


unencrypted_message = "My Twitter handle is @reenormies123, my favorite color is blue, and I hate eels (and hagfish but mostly eels)."
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)


print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)

