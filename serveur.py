#!/usr/bin/python2.7
#--*--coding=UTF-8--*--
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto import Random
import socket,pickle,base64,logging
from Crypto.Hash import MD5

"""generateur de clé de RSA"""
def rsaKey():
    random_generator=Random.new().read
    return RSA.generate(2048,random_generator)
key=rsaKey()
pubKey=pickle.dumps(key.publickey())
"""RSA chiffrement"""
def EnRSA(msg,pubKey):
    return pubKey.encrypt(msg,"test")
"""RSA dechiffrement"""
def DecRSA(enc_msg,key):
    return (key.decrypt(enc_msg))

""" AES chiffrement"""
def EncAES(text, Passphrase, IV):
    aes = AES.new(Passphrase, AES.MODE_CFB, IV);
    cipher_text = base64.b64encode(aes.encrypt(text));
    return cipher_text;

""" AES dechiffrement """
def DecAES(cipher_text, Passphrase, IV):
    aes = AES.new(Passphrase, AES.MODE_CFB, IV);
    text = aes.decrypt(base64.b64decode(cipher_text));
    return text

""" lancer le serveur"""
host=u''
port=1489
connextion_principale=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connextion_principale.bind((host,port))
print u"serveur ecoute le port {}".format(port)
connextion_principale.listen(1)
connextion_avec_client,info_client=connextion_principale.accept()
print info_client
msg=""

""" Envoyer la cle publique de RSA au client"""
connextion_avec_client.send(pubKey)


""" Recevoir la cle de AES du client """
msg=connextion_avec_client.recv(1024)
msg=pickle.loads(msg)
aesKey=DecRSA(msg,key)
IV=connextion_avec_client.recv(1024)

"""Communication etablie"""
while msg !='fin':
    msg=connextion_avec_client.recv(1024)
    msg=DecAES(msg,aesKey,IV)
    print msg
    connextion_avec_client.send("recu")
print u"Fermeture de la connextion"
connextion_avec_client.close()
connextion_principale.close()
