from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
from flask import request, send_file
from stegano import lsb
import os, zipfile
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def AES(key,iv):
    f=open(os.path.join(os.getcwd()+"/Parts","0.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%16!=0):
        while(b%16!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"/Parts","0.txt"),"wb").close()
    f=open(os.path.join(os.getcwd()+"/Parts","0.txt"),"wb")
    f.write(cont)
    f.close();

def BlowFish(key,iv):
    f=open(os.path.join(os.getcwd()+"/Parts","1.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode()
    b=len(content)
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content)
    backend = default_backend()
    cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()
    cont = encryptor.update(content) + encryptor.finalize()
    open(os.path.join(os.getcwd()+"/Parts","1.txt"),"w").close()
    f=open(os.path.join(os.getcwd()+"/Parts","1.txt"),"wb")
    f.write(cont);
    f.close();


def TrippleDES(key,iv):
    f=open(os.path.join(os.getcwd()+"/Parts","2.txt"),"r");
    content=f.read();
    f.close();
    content=content.encode()
    b=len(content);
    if(b%8!=0):
        while(b%8!=0):
            content+=" ".encode()
            b=len(content);
    backend = default_backend();
    cipher = Cipher(algorithms.TripleDES(key), modes.CBC(iv), backend=backend);
    encryptor = cipher.encryptor();
    cont = encryptor.update(content) + encryptor.finalize();
    open(os.path.join(os.getcwd()+"/Parts","2.txt"),"w").close();
    f=open(os.path.join(os.getcwd()+"/Parts","2.txt"),"wb");
    f.write(cont);
    f.close();

def IDEA(key,iv):
	f=open(os.path.join(os.getcwd()+"/Parts","3.txt"),"r")
	content=f.read()
	f.close()
	content=content.encode()
	b=len(content)
	if(b%8!=0):
		while(b%8!=0):
			content+=" ".encode()
			b=len(content)
	backend = default_backend()
	cipher = Cipher(algorithms.IDEA(key), modes.CBC(iv), backend=backend)
	encryptor = cipher.encryptor()
	cont = encryptor.update(content) + encryptor.finalize()
	open(os.path.join(os.getcwd()+"/Parts","3.txt"),"w").close()
	f=open(os.path.join(os.getcwd()+"/Parts","3.txt"),"wb")
	f.write(cont)
	f.close()
def EFernet(key):
    f=open(os.path.join(os.getcwd()+"/Parts","4.txt"),"r")
    content=f.read()
    f.close()
    content=content.encode('utf-8')
    fer = Fernet(key)
    content=fer.encrypt(content)
    open(os.path.join(os.getcwd()+"/Parts","4.txt"),'w').close()
    f=open(os.path.join(os.getcwd()+"/Parts","4.txt"),"wb")
    f.write(content)
    f.close()


def CryptKeys():
    key = Fernet.generate_key()
    f=open('Secured.txt','wb')
    f.write(key)
    f.close()
    listDir=os.listdir(os.getcwd()+"/Keys_IV")
    fer = Fernet(key)
    for i in listDir:
        KI=open(os.getcwd()+'/Keys_IV//'+i,'rb')
        content=KI.read()
        KI.close()
        content=fer.encrypt(content)
        open(os.path.join(os.getcwd()+"/Keys_IV",i),'wb').close()
        f=open(os.path.join(os.getcwd()+"/Keys_IV",i),"wb")
        f.write(content)
        f.close()

def rag():
    #LSB Steg
    r=open(os.path.join(os.getcwd()+"./Secured.txt"),"r")
    content=r.read()
    lsb_stegano_image = lsb.hide("./test_files/cover_image.png", content)
    lsb_stegano_image.save("./test_files/stego_image.png") 


"""def rag():

    # Open the text files and read in their contents
    with open("./Keys_IV/IV.txt", 'rb') as f1, open("./Keys_IV/k1.txt", 'rb') as f2, open("./Keys_IV/k2.txt", 'rb') as f3:
        text1 = f1.read()
        text2 = f2.read()
        text3 = f3.read()

    # Combine the contents of the text files into a single message
    message = text1 + b'\n' + text2 + b'\n' + text3
    lsb_stegano_image = lsb.hide("./test_files/cover_image.png", message)
    lsb_stegano_image.save("./test_files/stego_image.png") """

def zip_files():
    # Get the names of the five files to zip
    files = ['0.txt', '1.txt', '2.txt', '3.txt', '4.txt']

    # Create a new zip file
    zip_filename = 'CryptoSafe.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        # Add each file to the zip file
        for file in files:
            file_path = os.path.join((os.getcwd()+"\\Parts"), file)
            if os.path.exists(file_path):
                zip_file.write(file_path,file)
    return send_file(zip_filename, as_attachment=True)



