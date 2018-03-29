with open('text_files/file_007271.txt', 'r') as f:
    contents = f.read()

result = ""
for c in contents:
    result += chr(126 + 32 - ord(c))

print(result)
