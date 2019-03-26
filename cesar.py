'''
J'ai fait quelques ajustements,
Le pb c'est que tu ne semble pas redouter l'existence d'outils élémentaires en Python comme la methode index sur les liste, comme le % modulo.
En rêgle général ça se voit que tu viens d'un language + bas niveau tu éparpille ton code dans 50 fonctions qui sont toutes executées dans le même ordre donc pouraient n'être qu'une.
J'aurais pu faire coller un peu mieux mon remake avec la philosophie python mais ça m'aurais couté de tout refaire donc je me suis contenté de quelques ajustements
'''
#j'ai mis une compréhension de liste ici pour que tu sache comment ça peut servir, c'est pas très pertinent dans ce cas mais ça peut être SUPER puissant
alphabet = [chr(ord('A')+i) for i in range(0,26)] + [chr(ord('a')+i) for i in range(0,26)] + [chr(ord('0')+i) for i in range(0,10)]
alphabet.append((' ', '!'))

print(alphabet.index('a'))

def Crypt(phrase,passphrase):
    '''J'ai essayé de tout décomposer pour que ça reste simple a lire pour un programmeur C++ ^^.
    si j'avais fait le prog par moi-même j'aurais mis une compréhension de liste je pense.
    '''
    rep = ""
    for i in range (0,len(phrase)):
        l = alphabet.index(passphrase[i % len(passphrase)]) # c'est plus simple comme ça :)
        p = alphabet.index(phrase[i])
        c = l+p

        rep += alphabet[c % len(alphabet)]

    return rep

def Uncrypt(phrase,passphrase):
    '''Même rq  que pour Crypt()
    '''
    rep = ''
    for i in range (0,len(phrase)):
        l = alphabet.index(phrase[i])
        p = alphabet.index(passphrase[i % len(passphrase)]) #pourquoi utiliser la grammaire python pour un modulo si on peut créer une fonction en plus me dira-tu ?
        c = l-p

        rep += alphabet[c % len(alphabet)]

    return rep

isContinue = True
while isContinue:
    mode = input("Quel mode (d/c/q) : ")
    while mode != "d" and mode != "c" and mode != "q":
        mode = input("Entrer (d/c/q)!\nQuel mode (d/c/q) : ")
    if mode == "q":
        isContinue = False
        continue
    word = input("Entrer mot : ")
    passphrase = input("Entrer passphrase : ")

    if mode == "c":
        print(Crypt(word,passphrase))
    else:
        print(Uncrypt(word,passphrase))
