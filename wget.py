
#*/10 * * * * python /etc/cron.hourly/wget.py

import os,re

path = "/home/swapnil/Desktop/U_Mirror/versions/17/old_MD5/MD5SUMS"
l=[]
with open(path,'r') as f:
    for line in f:
        for word in line.split():
           l.append(word)   

old_hash = l[0]

#os.system("wget http://releases.ubuntu.com/17.10/ubuntu-17.10-desktop-amd64.iso -P /home/swapnil/Desktop/U_Mirror/versions/")
os.system("wget http://releases.ubuntu.com/17.10/MD5SUMS -P /home/swapnil/Desktop/U_Mirror/versions/17/new_MD5SUM/")

path1 = "/home/swapnil/Desktop/U_Mirror/versions/17/new_MD5SUM/MD5SUMS"
l1=[]
with open(path,'r') as f:
    for line in f:
        for word in line.split():
           l1.append(word)   

new_hash = l1[0]


os.system("openssl dgst -md5 /home/swapnil/Desktop/U_Mirror/versions/17/ubuntu-17.10-desktop-amd64.iso > /home/swapnil/Desktop/U_Mirror/versions/17/MD5_cross_check.txt")


with open("/home/swapnil/Desktop/U_Mirror/versions/17/MD5_cross_check.txt",'r') as f:
	md  = f.readline() 

l2=[]	
for parts in md.split("= "):
	l2.append(parts)

md_cross_check = l2[1]
#print old
#print newm
#print md

#if old != newm and old != md :
#	os.system("wget http://releases.ubuntu.com/17.10/ubuntu-17.10-desktop-amd64.iso -P /home/swapnil/Desktop/U_Mirror/versions/17/")
#	os.system("wget http://releases.ubuntu.com/17.10/MD5SUMS -P /home/swapnil/Desktop/U_Mirror/versions/17/")

flag = 0 
while flag!=1:
	if old_hash != new_hash:
		os.system("wget http://releases.ubuntu.com/17.10/ubuntu-17.10-desktop-amd64.iso -P /home/swapnil/Desktop/U_Mirror/versions/17/")
		os.system("cp /home/swapnil/Desktop/U_Mirror/versions/17/new_MD5SUM/MD5SUMS /home/swapnil/Desktop/U_Mirror/versions/17/old_MD5/")
		os.system("rm -rf /home/swapnil/Desktop/U_Mirror/versions/17/new_MD5SUM && mkdir /home/swapnil/Desktop/U_Mirror/versions/17/new_MD5SUM")
		if new_hash == md_cross_check:
			flag = 1

	

	










