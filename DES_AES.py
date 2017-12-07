#!/usr/bin/python2.7
#--*-- coding: utf-8 --*--

"""Import DES"""
from Crypto.Cipher import DES
from Crypto import Random
from Crypto.Cipher import DES3
from Crypto.Cipher import AES
import base64

"""Var"""
text = 'abcdefghijklmnop'

iv = Random.get_random_bytes(8);
KeyDES = '01234567';
Key3DES = '1234567897412589'; """Key 16 or 24 bytes"""

Passphrase = b'Sixteen byte key';
IV = Random.new().read(AES.block_size);

"""Fonction"""
def EncDES(text, KeyDES, iv):
	des = DES.new(KeyDES, DES.MODE_CFB, iv);
	cipher_text = des.encrypt(text)
	return cipher_text;

def Enc3DES(text, Key3DES, iv):
	des3 = DES3.new(Key3DES, DES3.MODE_CFB, iv);
	cipher_text = des3.encrypt(text);
	return cipher_text;

def EncAES(text, Passphrase, IV):
	aes = AES.new(Passphrase, AES.MODE_CFB, IV);
	cipher_text = base64.b64encode(aes.encrypt(text));
	return cipher_text;

def DecDES(cipher_text, KeyDES, iv):
	des = DES.new(KeyDES, DES.MODE_CFB, iv);
	text = des.decrypt(cipher_text);
	return text;

def Dec3DES(cipher_text, Key3DES, iv):
	des3 = DES3.new(Key3DES, DES3.MODE_CFB, iv);
	text = des3.decrypt(cipher_text);
	return text;

def DecAES(cipher_text, Passphrase, IV):
	aes = AES.new(Passphrase, AES.MODE_CFB, IV);
	text = aes.decrypt(base64.b64decode(cipher_text));
	return text;

"""Main"""
print("Chiffrement DES");
print("Texte à chiffrer : " + text);
cipher_text = EncDES(text, KeyDES, iv);
print("Texte Chiffré : " + cipher_text);
DecText = DecDES(cipher_text, KeyDES, iv);
print("Texte Déchiffré : " + DecText);
print(" ");

print("Chiffrement 3DES");
print("Texte à chiffrer : " + text);
cipher_text = Enc3DES(text, Key3DES, iv);
print("Texte Chiffré : " + cipher_text);
DecText = Dec3DES(cipher_text, Key3DES, iv);
print("Texte Déchiffré : " + DecText);
print(" ");

print("Chiffrement AES");
print("Texte à chiffrer : " + text);
cipher_text = EncAES(text, Passphrase, IV);
print("Texte Chiffré : " + cipher_text);
DecText = DecAES(cipher_text, Passphrase, IV);
print("Texte Déchiffré : " + DecText);
print(" ");
