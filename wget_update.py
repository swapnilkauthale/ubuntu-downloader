
#*/10 * * * * python /etc/cron.hourly/wget.py

import os,re

p = "/home/swapnil/Desktop/U_Mirror/versions/17"

path = p+"/old_MD5/MD5SUMS"
l=[]
with open(path,'r') as f:
    for line in f:
        for word in line.split():
           l.append(word)   

old_hash = l[0]


os.system("wget http://releases.ubuntu.com/17.10/MD5SUMS -P "+p+"/new_MD5SUM/")

path1 = p+"/new_MD5SUM/MD5SUMS"
l1=[]
with open(path,'r') as f:
    for line in f:
        for word in line.split():
           l1.append(word)   

new_hash = l1[0]

print 'till here'			
os.system("openssl dgst -md5 "+p+"/ubuntu-17.10-desktop-amd64.iso > "+ p +"/MD5_cross_check.txt")


with open(p+"/MD5_cross_check.txt",'r') as f:
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

print 'till hererererere'

if old_hash != new_hash:
	os.system("wget http://releases.ubuntu.com/17.10/ubuntu-17.10-desktop-amd64.iso -P"+ p+"/")
	os.system("rm -rf "+p+"/old_MD5 && mkdir "+p+"/old_MD5")
	os.system("cp "+p+"/new_MD5SUM/MD5SUMS "+p+"/old_MD5/")
	os.system("rm -rf "+p+"/new_MD5SUM && mkdir "+p+"/new_MD5SUM")

os.system("rm -rf "+p+"/new_MD5SUM && mkdir "+p+"/new_MD5SUM")

#if new_hash != md_cross_check:
#	flag=flag+1

	

	










