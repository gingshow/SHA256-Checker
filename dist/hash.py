import os
import hashlib
import termcolor

hash1=""
hash2=""

if os.path.isfile('./sha256sum.txt'):
    print("sha256sum.txt exists")
    file1 = open("sha256sum.txt", "r")
else:
    print("sha256sum.txt does not exists,please make sure your file name is correct")
    input("Press enter to exit")
    exit(0)

#Display list of files inside directory
print("Display list of files:")
for x in os.listdir('.'):
    print(x)

filename = input("Please enter the file name: ")
print("Extracting hash from %s ..." % filename)

sha256_hash = hashlib.sha256()
with open(filename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)

hash1=sha256_hash.hexdigest()

l=file1.readlines()
for word in l:
    if filename in word: # find match line by file name
        print(word) #debug
        clearline1 = word.replace(filename, '') # clear file name
        clearline2 = clearline1.replace('*', '')  # clear *
        clearline3 = clearline2.strip() # clear whitespace and new lines
        hash2=clearline3

if hash1 == hash2:
    print("Hash1 is %s"%hash1)
    print("Hash2 is %s" % hash2)
    print("Hash correct")
    input("Press enter to exit")

else:
    print("Hash1 is %s" % hash1)
    print("Hash2 is %s" % hash2)
    termcolor.cprint('Hash incorrect','red')
    input("Press enter to exit")