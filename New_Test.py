import string


alphabets = string.ascii_lowercase
print(alphabets)

with open("3x3Letters.txt", "w") as file:
    for letter1, letter2, letter3 in zip(alphabets[0::3], alphabets[1::3], alphabets[2::3]):
        file.write(letter1+letter2+letter3+"\n")

with open("3x3Letters.txt", "r+") as w_file:
    content = w_file.read()
    for i in alphabets:
        if i not in content:
            w_file.write(i)



import glob

file_list = glob.glob("letters\\*.txt")
print(file_list)
alphabets = string.ascii_lowercase
letters = []
py_letters = []

for i in file_list:
    with open(i, "r") as file2:
        content = file2.read()
        if content.strip("\n") in "python":
            py_letters.append(content.strip("\n"))
print(py_letters)
for i in alphabets:
    with open("letters/"+i+".txt", "r") as file:
        letter = file.read()
        letters.append(letter.rstrip("\n"))
print(letters)
