#!/usr/bin/python

from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import base64

print '''
\033[1;95m
  ____ _               _    __                     _             
 / ___| |__   ___  ___| |_ / _|_   _ ___  ___ __ _| |_ ___  _ __ 
| |  _| '_ \ / _ \/ __| __| |_| | | / __|/ __/ _` | __/ _ \| '__|
| |_| | | | | (_) \__ \ |_|  _| |_| \__ \ (_| (_| | || (_) | |   
 \____|_| |_|\___/|___/\__|_|  \__,_|___/\___\__,_|\__\___/|_|   
                                                                 
\033[1;31m            << The Python Password-Protected Obfuscator >>\033[1;95m
----------------------------------------------------------------\033[0m
                        
'''

infile = raw_input('\033[1;34m[=]\033[0m Input Python File: ')
outfile = raw_input('\033[1;34m[=]\033[0m Output Path: ')
key = raw_input('\033[1;34m[=]\033[0m Password: ')


BLOCK_SIZE = 16  
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

f = open(infile, 'r')
script = f.read()
f.close()

script = "#GHOSTFUSCATOR\n" + script
script = pad(script)
key = SHA256.new(key.encode('utf-8')).digest()
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CBC, iv)
out = base64.b64encode(iv + cipher.encrypt(script))


outscript1 = '''
from Crypto.Cipher import AES;from Crypto.Hash import SHA256;import base64;unpad=lambda s: s[:-ord(s[len(s)-1:])];print(base64.b64decode('ICBfX19fIF8gICAgICAgICAgICAgICBfICAgIF9fICAgICAgICAgICAgICAgICAgICAgXyAgICAgICAgICAgICAKIC8gX19ffCB8X18gICBfX18gIF9fX3wgfF8gLyBffF8gICBfIF9fXyAgX19fIF9fIF98IHxfIF9fXyAgXyBfXyAKfCB8ICBffCAnXyBcIC8gXyBcLyBfX3wgX198IHxffCB8IHwgLyBfX3wvIF9fLyBfYCB8IF9fLyBfIFx8ICdfX3wKfCB8X3wgfCB8IHwgfCAoXykgXF9fIFwgfF98ICBffCB8X3wgXF9fIFwgKF98IChffCB8IHx8IChfKSB8IHwgICAKIFxfX19ffF98IHxffFxfX18vfF9fXy9cX198X3wgIFxfXyxffF9fXy9cX19fXF9fLF98XF9fXF9fXy98X3wgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQo='));print(base64.b64decode('W2ldIEVzdGUgcHJvZ3JhbWEgZXN0YSBwcm90ZWdpZG8gcG9yIEdob3N0UGFja2VyLiBQYXJhIGNvbnRpbnVhciBjb24gbGEgZWplY3VjaW9uIGRlbCBwcm9ncmFtYSwgaW5ncmVzZSBzdSBjb3JyZXNwb25kaWVudGUgY2xhdmUu')+'\n');x98347748307489465768=raw_input(base64.b64decode('Wz1dIFBhc3N3b3JkOiA='));x98347748307489465768=SHA256.new(x98347748307489465768.encode(base64.b64decode('dXRmLTg='))).digest();
x98347748307489465761=base64.b64decode("''' + out + '''");x98347748307489465762=AES.new(x98347748307489465768,AES.MODE_CBC,x98347748307489465761[:AES.block_size]);x98347748307489465760=unpad(x98347748307489465762.decrypt(x98347748307489465761[AES.block_size:])).decode(base64.b64decode('dXRmOA=='))
if base64.b64decode('I0dIT1NURlVTQ0FUT1I=') in x98347748307489465760:
    exec(x98347748307489465760)
else:
    print(base64.b64decode('Wy1dIENsYXZlIEluY29ycmVjdGEuIFBydWViZSBkZSBudWV2by4='));exit()
'''

outscript2 = '''import base64;exec(base64.b64decode("''' + base64.b64encode(outscript1) + '''"))'''


g = open(outfile, 'w')
g.write(outscript2)
g.close()

print('\033[1;32m[+]\033[0m Script Successfully Obfuscated in: ' + outfile)
exit()




