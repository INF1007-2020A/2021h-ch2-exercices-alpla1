#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    MotMaj = ""
    for i in range(len(mot)):
        NumeroAscii = ord(mot[i])
        if NumeroAscii >= 97 :
            NumeroAscii = NumeroAscii - 32
        MotMaj += str(chr(NumeroAscii))
    mot = MotMaj
    return mot
if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre',
        'allo!'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
