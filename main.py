from pie import pi, e
import string
encryption_bits = 2048
randomizer = 3
alphabets = string.ascii_uppercase + string.punctuation + " " + string.digits + "\n" + "  " + "   " + "\t"

def encrypt(key, e_string):
    key_dict = {}
    if int(str(key)[3]) % 2 == 0:
        schema = e + pi
    else:
        schema = pi + e
    randomize = str(key)[4] + schema[key - randomizer: key]
    randomize = int(randomize)
    for alphabet in alphabets:
        eight_bit_key = schema[key:(key + encryption_bits)]
        int_string = ""
        for key_element in eight_bit_key:
            if int(key_element) % 2 == 0:
                int_string = int_string + "1"
            else:
                int_string = int_string + "0"

        key_dict[alphabet] = int_string
        key += encryption_bits + randomize



    encrypted_string = ""
    for element in e_string:
        encrypted_string = encrypted_string + key_dict[str(element).upper()]
    return encrypted_string


def decrypt(key, d_string):
    decrypt_dic = {}
    if int(str(key)[3]) % 2 == 0:
        schema = e + pi
    else:
        schema = pi + e
    randomize = str(key)[4] + schema[key - randomizer: key]
    randomize = int(randomize)
    for alphabet in alphabets:
        eight_bit_key = schema[key:(key + encryption_bits)]
        int_string = ""
        for key_element in eight_bit_key:
            if int(key_element) % 2 == 0:
                int_string = int_string + "1"
            else:
                int_string = int_string + "0"

        decrypt_dic[int_string] = alphabet
        key += encryption_bits + randomize

    decrypt_string = ""
    dec_pos = 0
    dec_list = []
    dec_no = len(d_string) / encryption_bits
    for dec_ele in range(int(dec_no)):
        dec_list.append(d_string[dec_pos:dec_pos + encryption_bits])
        dec_pos += encryption_bits

    for element in dec_list:
        decrypt_string = decrypt_string + decrypt_dic[element]

    return decrypt_string

test_message = input("Type the message to encrypt: ")
encryption_key = input("Give a six digit numeric only key to encrypt: ")
test = encrypt(int(encryption_key), test_message)

print("Encrypted Message:", test)
print("Length of the encrypted message: ", len(test))
def decrypting():
    try:
        decryption_key = input("Give a six digit numeric only key to decrypt: ")
        print("Decrypting...")
        print("Decrypted message:", decrypt(int(decryption_key), test))
        print("Decryption successful!")
    except:
        print("Sorry! Wrong key entered.")
        warning = input("Do you want to try again? Y/N ")
        if str(warning).upper() == "Y":
            decrypting()
        else:
            exit()

decrypting()