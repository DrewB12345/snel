import os

def newCounts(text):
    counts = [0] * 127
    for c in text:
        n = ord(c)
        counts[n] += 1
    counts = counts[32:127]
    return counts

def mean(counts):
    return sum(counts) / len(counts)

def chi_square(counts):
    expected = mean(counts)
    
    X = 0

    for n in counts:
        X += (n - expected)**2

    return X / expected

def checkFolder(folderName):
    for subdir, dirs, files in os.walk(folderName):
        for file in files:
            filename = os.path.join(subdir, file)
            with open(filename, "r") as f:
                text = f.read()
            counts = newCounts(text)
            if chi_square(counts) > 140:
                print(filename + " " + str(chi_square(counts)))

checkFolder("text_files")

