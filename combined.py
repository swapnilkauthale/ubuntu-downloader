
import os,re

p = "/home/swapnil/Desktop/U_Mirror"

os.system("wget http://releases.ubuntu.com/12.04/MD5SUMS -P "+p+"/new_hash/v12/")
os.system("wget http://releases.ubuntu.com/14.04/MD5SUMS -P "+p+"/new_hash/v14/")
os.system("wget http://releases.ubuntu.com/16.04/MD5SUMS -P "+p+"/new_hash/v16/")
os.system("wget http://releases.ubuntu.com/17.10/MD5SUMS -P "+p+"/new_hash/v17/")

os.system("touch "+p+"/new_hash/NEW_MD5.txt")
        
with open(p+'/new_hash/NEW_MD5.txt', 'a') as f1:
    for line in open(p+'/new_hash/v12/MD5SUMS'):
            f1.write(line)
            print '\n'+line 

with open(p+'/new_hash/NEW_MD5.txt', 'a') as f1:
    for line in open(p+'/new_hash/v14/MD5SUMS'):
            f1.write(line)
            print '\n'+line              

with open(p+'/new_hash/NEW_MD5.txt', 'a') as f1:
    for line in open(p+'/new_hash/v16/MD5SUMS'):
            f1.write(line) 
            print '\n'+line         

with open(p+'/new_hash/NEW_MD5.txt', 'a') as f1:
    for line in open(p+'/new_hash/v17/MD5SUMS'):
            f1.write(line) 
            print '\n'+line   

      
