#!/usr/bin/python2.7
#--*--coding=UTF-8--*--
from __future__ import absolute_import
import socket,pickle,base64,hashlib
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import MD5
"""RSA chiffrement"""
def EnRSA(msg,pubKey):
    return pubKey.encrypt(msg,"test")

"""clé de AES"""
aesKey = b'Sixteen byte key'
Passphrase = aesKey;
aesKey=aesKey.encode()

""" AES chiffrement"""
IV = Random.new().read(AES.block_size);
def EncAES(text, Passphrase, IV):
    aes = AES.new(Passphrase, AES.MODE_CFB, IV);
    cipher_text = base64.b64encode(aes.encrypt(text));
    return cipher_text;
"""AES dechiffrement"""
def DecAES(cipher_text, Passphrase, IV):
    aes = AES.new(Passphrase, AES.MODE_CFB, IV);
    text = aes.decrypt(base64.b64decode(cipher_text));
    return text;

"""connection avec le serveur"""
host=u'127.0.0.1'
port=1489
connextion_avec_serveur=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connextion_avec_serveur.connect((host,port))
msg=''

"""Recevoir la cle publique de RSA"""
pubKey=connextion_avec_serveur.recv(1024)
pubKey=pickle.loads(pubKey)
crypte_aes_key=pickle.dumps(EnRSA(aesKey,pubKey))

"""Envoyer la cle de AES au serveur"""
connextion_avec_serveur.send(crypte_aes_key)
connextion_avec_serveur.send(IV)
print u"communication etabli"
while msg !='fin':
    msg=raw_input(u'>:')
    cipher_msg=EncAES(msg,Passphrase,IV)
    connextion_avec_serveur.send(cipher_msg)
    msg_recu=connextion_avec_serveur.recv(1024)
    print msg_recu.decode()
print u"Fermeture de la connnextion"
connextion_avec_serveur.close()

