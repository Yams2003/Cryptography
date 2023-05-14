import random
import string


def message_to_ascii(message):
    ascii_message = ""
    for char in message:
        ascii_message += str(ord(char)) + " "
    return ascii_message


def ascii_to_binary(ascii_message):
    binary_message = ""
    for number in ascii_message.split():
        binary_message += bin(int(number))[2:].zfill(8) + " "
    return binary_message


def generate_pad(length):
    pad = ''.join(random.choices(string.printable, k=length))
    while len(pad) < length:
        pad += random.choice(string.ascii_letters + string.digits)
    return pad


def pad_to_binary(ascii_pad):
    binary_pad = ""
    for char in ascii_pad.split():
        binary_pad += bin(int(char))[2:].zfill(8) + " "
    return binary_pad


def xor_strings(ascii_message, ascii_pad):
    i = 0
    ascii_result = ''
    for char in ascii_message.split():
        result = int(char) ^ int(ascii_pad.split()[i])
        i += 1
        ascii_result += bin(int(result))[2:].zfill(8) + " "
    return ascii_result


def binary_to_text(ascii_result):
    result_bytes = ascii_result.split()
    result_text = ''.join([chr(int(byte, 2)) for byte in result_bytes])
    return result_text


def encrypt(message):
    print('Encryption')
    print('-' * 35)
    print("Message:", message)

    # Convert message to ASCII
    ascii_message = message_to_ascii(message)
    print('Message in ASCII Numbers:', ascii_message)

    # Convert ASCII to binary
    binary_message = ascii_to_binary(ascii_message)
    print('Message in Binary:', binary_message)

    # Generate pad
    pad = generate_pad(len(message))
    ascii_pad = message_to_ascii(pad)
    print("Key:", end=" ")
    print(pad)

    # Convert pad to binary
    binary_pad = pad_to_binary(ascii_pad)
    print("Key in Binary:", binary_pad)

    # Apply XOR on each character from the message and pad
    ascii_result = xor_strings(ascii_message, ascii_pad)
    print('XOR Binary Result:', ascii_result)

    # Convert XOR result to text
    result_text = binary_to_text(ascii_result)

    # Print the result
    print("Cipher Text:", end=" ")
    print(result_text)

    return result_text, pad


def decrypt(cipher_text, pad):
    print('Decryption')
    print('-' * 35)
    print('Cipher Text:', end=" ")
    print(cipher_text)
    print('Key:')
    print(pad)

    # Convert pad to ASCII
    ascii_pad = message_to_ascii(pad)

    # Apply XOR on each character from the cipher text and pad
    ascii_result = xor_strings(message_to_ascii(cipher_text), ascii_pad)

    # Convert XOR result to text
    result_text = binary_to_text(ascii_result)
    print('Original message:', end=" ")
    print(result_text)

    print()
    print('Using a new key:')
    print('Deleting old key...')
    del pad
    print('Generating new key...')

    # Generate a new key
    pad = generate_pad(len(result_text))
    new_ascii_pad = message_to_ascii(pad)
    print('New Key:', pad)

    # Decrypt with the new key
    print('Decrypting with new key...')
    ascii_result = xor_strings(message_to_ascii(cipher_text), new_ascii_pad)

    # Convert XOR result to text
    result_text = binary_to_text(ascii_result)
    print('Result:', result_text)

    if result_text == cipher_text:
        print('Result matches original message')
    else:
        print('Result does not match original message')


message = encrypt("Hello World")
print()
decrypt(message[0], message[1])