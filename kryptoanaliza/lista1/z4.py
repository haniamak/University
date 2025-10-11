from itertools import cycle

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphalen = len(alphabet)
num2char = dict(enumerate(alphabet))
char2num = { num2char[n]:n for n in num2char }
def encodeChar(c, k):
  return num2char[(char2num[c]+char2num[k]) % alphalen]

def encode(plaintext, key):
  return "".join(map(encodeChar, plaintext, cycle(key)))

def decodeChar(c, k):
  return num2char[(char2num[c]-char2num[k]) % alphalen]

def decode(ciphertext, key):
  return "".join(map(decodeChar, ciphertext, cycle(key)))

cipher = 'FDGEFYQUMYMODKBFASDMBTQD'

for i in range(26):

  plaintext = decode(cipher, alphabet[i])
  letter = num2char[i]
  print(letter, plaintext)
  #res for letter M


cipher2 = 'XHQPMFTFSJBHAMEHGIGHISHLPHLJAECWRVSRJWXNQECBSIQSCQSRHERWTWSVLVMRVLJAECWRVSRJWXNQECBSIFIHCPKS'

def findKey(ciphertext, plaintext):
  key = ''
  for i in range(len(ciphertext)):
    key += decodeChar(ciphertext[i], plaintext[i])
  return key

startplaintext = 'ITMAY'
startcipher = 'XHQPM'
key2 = findKey(startcipher, startplaintext)
for i in range(len(key2)):
  print(key2[0:len(key2)-i], ':', decode(cipher2, key2[0:len(key2)-i]))
