import pyqrcode

#Coloque entre as aspas o link que você deseja cria um qrcode 
url = pyqrcode.create('https://www.linkedin.com/in/snt-gabriel/')

url.svg('uca-url.svg', scale=5)

url.eps('uca-url.eps', scale=2)

print(url.terminal(quiet_zone=1))

