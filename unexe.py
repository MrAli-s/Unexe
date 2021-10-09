import os
import sys
os.system("pip3 install -r requirements.txt")
os.system("apt install git && apt install python3 -y")
os.system("git clone https://github.com/rocky/python-decompile3")
os.getcwd()
os.chdir("python-decompile3")
os.system("python3 setup.py install")
os.chdir("../")
run = input("Your File: ")
os.system("python3 main.py " + run)
print("Done :D")
