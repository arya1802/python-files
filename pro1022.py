import sys
nato_alphabet = {
    'a': 'aragora',
    'b': 'balelaka',
    'c': 'chikko',
    'd': 'doritos',
    'e': 'eruma kada',
    'f': 'fool',
    'g': 'gundan',
    'h': 'hola',
    'i': 'indiana',
    'j': 'julieteee',
    'k': 'kilogram',
    'l': 'lime sida',
    'm': 'miracle',
    'n': 'nova amber',
    'o': 'ostrich',
    'p': 'paper roast',
    'q': 'queen',
    'r': 'road roller',
    's': 'singam',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'waterloo',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu'
}
try:
    sys.argv[1]
except:
    print("Usage: natoalphabet.py <word>")
    exit(1)
for letter in sys.argv[1]:
    if letter.lower() not in nato_alphabet:
        print(letter)
    else:
        print(nato_alphabet[letter])