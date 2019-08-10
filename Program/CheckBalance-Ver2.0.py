starting="'{\"addr\":\""
ending="\"}' https://www.blockonomics.co/api/balance"

from sys import argv
import os
import subprocess

ReadFile=open("../Import/GeneratedAdd",'r')

KeysPub=[]
KeysPriv=[]

for eachline in ReadFile.readlines():
    flag=True
    count=-1
    while flag!=False:
        count=count+1
        if not eachline[count].isalnum():
            flag=False
    PublicKey=eachline[0:count-1]
    PrivKey=eachline[count+1:]
    KeysPub.append(PublicKey)
    KeysPriv.append(PrivKey)
    url=starting
    for i in PublicKey:
        url=url+PublicKey+' '
    url=url+ending
    pipe = subprocess.Popen("curl -d "+url, shell=True, stdout=subprocess.PIPE).stdout
    print(pipe.read())
