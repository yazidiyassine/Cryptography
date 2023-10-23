#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def chiffrement_hill(message, matrice_cle):
    # Convertir le message en lettres majuscules et supprimer les espaces
    message = message.replace(" ", "").upper()

    # Vérifier si la longueur du message est compatible avec la taille de la matrice clé
    if len(message) % len(matrice_cle) != 0:
        raise ValueError("La longueur du message doit être un multiple de la taille de la matrice clé")

    # Initialiser le texte chiffré
    texte_chiffre = ""

    # Itérer à travers le message par blocs de la taille de la matrice clé
    for i in range(0, len(message), len(matrice_cle)):
        bloc = message[i:i + len(matrice_cle)]
        vecteur_message = np.array([ord(caractere) - ord('A') for caractere in bloc])
        vecteur_chiffre = np.dot(matrice_cle, vecteur_message) % 26
        bloc_chiffre = ''.join([chr(caractere + ord('A')) for caractere in vecteur_chiffre])
        texte_chiffre += bloc_chiffre

    return texte_chiffre


# In[8]:


matrice_cle = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
message = "HELLOO"
message_chiffre = chiffrement_hill(message, matrice_cle)
print("Message Chiffré:", message_chiffre)


# In[4]:


import numpy as np

def dechiffrement_hill(texte_chiffre, matrice_cle):
    # Calculer la matrice inverse de la matrice de clé
    determinant = int(round(np.linalg.det(matrice_cle)))
    matrice_inverse = np.linalg.inv(matrice_cle)
    matrice_inverse = (matrice_inverse * determinant) % 26
    matrice_inverse = matrice_inverse.astype(int)

    # Convertir le texte chiffré en lettres majuscules
    texte_chiffre = texte_chiffre.upper()

    # Initialiser le texte déchiffré
    texte_dechiffre = ""

    # Itérer à travers le texte chiffré en blocs de la taille de la matrice clé
    for i in range(0, len(texte_chiffre), len(matrice_cle)):
        bloc = texte_chiffre[i:i + len(matrice_cle)]
        vecteur_chiffre = np.array([ord(caractere) - ord('A') for caractere in bloc])
        vecteur_dechiffre = np.dot(matrice_inverse, vecteur_chiffre) % 26
        bloc_dechiffre = ''.join([chr(caractere + ord('A')) for caractere in vecteur_dechiffre])
        texte_dechiffre += bloc_dechiffre

    return texte_dechiffre


# In[10]:


# Exemple d'utilisation :
matrice_cle = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
message_chiffre = "TFJANS"
message_dechiffre = dechiffrement_hill(message_chiffre, matrice_cle)
print("Message Déchiffré:", message_dechiffre)

