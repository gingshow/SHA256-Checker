# SHA256-Checker
A simply SHA256-Checker written in Python.

# How to use SHA256-Checker?
Step 1: Download the file you want to check and SHA256 checksum file from the Internet then put them inside dist folder.
Step 2: Open hash.exe.
Step 3: Type the file name.
(Example:pycharm-community-2020.2.exe). 
Then the program will generate hash from the check file and compare the hash inside sha256sum.txt.
If two of them are matched.The program will display "Hash correct".
Otherwise the program will display "Hash incorrect".

# Notice:
If the website only provided you a SHA256SUM value then you need to create a text file called sha256sum.txt
After that paste the hash value inside the text file.
The SHA256SUM hash format should look like this.
hashvalue *filename.extension
or
hashvalue filename.extension

For example:
65afa1b90f3ecc45946793c4c43a47a46dff2e1da0737ce602f5ee12bd946f1e *pycharm-community-2020.2.exe

93863e17ac24eeaa347dfb91dddac654f214c189e0379d7c28664a306e0301e7  debian-10.5.0-amd64-netinst.iso
14ca00bafcaf124ef2cab9da2f51d75044232ba9630a067d8664fabcb5e26ec2  debian-10.5.0-amd64-xfce-CD-1.iso
7fe10f143b7f697ecabe3d4b2f94d523ad74ffb1743e5c86586a3f57ea904f35  debian-edu-10.5.0-amd64-netinst.iso
461af35784ef816401297902c531a03614429003bdea0ea26fb19f57e0aaa4c6  debian-mac-10.5.0-amd64-netinst.iso

# If you think the download source is untrusted.Never download any files or hash files from them. 

If you have any question feel free to ask me. Thank you!
Email:gingshowgit@gmail.com

This program is written by Gingshow


