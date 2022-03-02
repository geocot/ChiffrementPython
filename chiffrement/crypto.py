from cryptography.fernet import Fernet
"""
#Création de la clé
key = Fernet.generate_key()
fichierCle = open("maCle.key", "wb")
fichierCle.write(key)
fichierCle.close()

#Ouvrir fichier clé
fichierCle = open("maCle.key", "rb")
key = fichierCle.read()

f = Fernet(key)
#Ouvrir fichier à chiffrer
fichierAChiffrer = open("mesInfos.txt", "rb")
aChiffrer = fichierAChiffrer.read()
fichierAChiffrer.close()
#Chiffrement des données
chiffrement = f.encrypt(aChiffrer)

#Sauvegarde des données chiffrées
fichierChiffrement = open("mesInfosChiffres.txt", "wb")
fichierChiffrement.write(chiffrement)
fichierChiffrement.close()
"""
#Ouvrir fichier chiffré
fichierChiffre = open("mesInfosChiffres.txt", "rb")
infosChiffres = fichierChiffre.read()
fichierChiffre.close()

#Ouvrir fichier clé
fichierCle = open("maCle.key", "rb")
key = fichierCle.read()

f = Fernet(key)

dechiffrement = f.decrypt(infosChiffres)

#Fichier déchiffré
fichierDechiffre = open("mesInfosDechiffres.txt", "wb")
fichierDechiffre.write(dechiffrement)
fichierDechiffre.close()
