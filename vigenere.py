with open("text_files/file_012499.txt", 'r') as f:
    contents = f.read()

def vigenere(text, keyword):
    result = ""
    count = 0
    for c in text:
        num = ord(text[count]) - ord(keyword[count % 6])
        while num > 126:
            num -= 95
            
        while num < 32:
            num += 95
            
        result += chr(num)
        count += 1
    return result

print(vigenere(contents, "enigma"))
key = "enigma" * 3000

