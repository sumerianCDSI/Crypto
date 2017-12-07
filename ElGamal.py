#!/usr/bin/python2.7
#--*-- coding: utf-8 --*--

from Crypto.PublicKey import ElGamal
from Crypto import Random

randfunc = Random.new().read

print("... Génération clef en cours ...")
EG = ElGamal.generate(1024,randfunc)

print "p = ", EG.p
print "g = ", EG.g
print "x = ", EG.x
print "y = ", EG.y

# g n'est pas toujours primitif dans cette version ...

M ='Le cheval de mon cousin ne mange du foin que le dimanche.'

print("Chiffrement :")
C = EG.encrypt(M, 4567); """ s = 4567 """
print C

print("Déchiffrement :")
D = EG.decrypt(C)
print D

print("Signature :")
s = EG.sign(M, 4567)
print s

print("Verif signature :")
v = EG.verify(M,s)
print v
