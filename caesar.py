def newCounts(message):
    counts = [0] * 127
    for c in message:
        n = ord(c)
        counts[n] += 1
    counts = counts[32:126]
    return counts
    
def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount
    
    while unicode_value > 126:
        unicode_value -= 95

    while unicode_value < 32:
        unicode_value += 95
        
    return chr(unicode_value)

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, shift_amount)

    return result

def decrypt(message, shift_amount):
    return encrypt(message, -1 * shift_amount)

def betterDecrypt(message, counts):
    gotit = False
    while not gotit:
        if not counts.index(max(counts)) == 0:
            message = encrypt(message, 1)
            counts = newCounts(message)
        else:
            gotit = True
    return message

with open('text_files/file_001597.txt', 'r') as f:
    contents = f.read()

counts = newCounts(contents)
decrypted = betterDecrypt(contents, counts)
print(decrypted)
