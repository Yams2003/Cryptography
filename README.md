# Cryptography
My journey to learning the basics of Cryptography started with an assignment I recieved in my Discrete Maths class. 
I decided to keep track of my understanding of the topic through coding excersizes or just visual demonstrations of how Cryptography is implemented.

## One-Time Pad
A one-time pad (OTP) is a cryptographic technique that uses a random key to encrypt and decrypt messages. 
It is an encryption method that provides perfect secrecy if used correctly. The key used in a one-time pad is a random sequence of characters or bits that is at least as long as the plaintext message to be encrypted. The key is used only once and should never be reused. The steps are:

1. Generate a random key: Create a random key that is at least as long as the plaintext message you want to encrypt. The key should consist of truly random characters and should never be reused.
2. Convert the plaintext to binary: Convert the plaintext message into binary format. Each character or symbol in the plaintext is represented by its binary equivalent.
3. XOR the key and plaintext: Perform an exclusive OR (XOR) operation between each binary bit of the key and the corresponding bit of the plaintext. This bitwise XOR operation combines the key and the plaintext, producing the ciphertext.
4. Transmit or store the ciphertext: The resulting ciphertext is the encrypted form of the plaintext. It can be transmitted securely or stored for later use.
5. Decrypt the ciphertext: To decrypt the ciphertext and recover the original plaintext, the same key that was used for encryption must be used. Perform the XOR operation between each bit of the key and the corresponding bit of the ciphertext.
6. Convert binary to plaintext: Convert the binary result back into the original plaintext format by mapping each binary symbol to its corresponding character or symbol.

Attached in the repo is a demonstration of this in Python 3. For more information on the topic, watch [this video](https://www.youtube.com/watch?v=QVV_bUxxiZ8).
