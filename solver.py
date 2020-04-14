#!/usr/bin/env python3



# -----------------------------------------------------------------------------------------------------------------------------
# DECLARATION DES BIDULES, C'EST PAS ENCORE ICI QUE LE CODE S'EXECUTE, ici il se définit. La logique d'exéctution c'est plus bas.
# -----------------------------------------------------------------------------------------------------------------------------

jb = [] # c'est un chouette nom de variable en période de coronavirus / contiendra les futurs "bonne position, bon chiffre"
jm = [] # hashtag j'aime / bon chiffre, mauvaise position
rb = [] # trouve une blague sur le nom de cette variable, partage et clic sur subscribe / rien n'est bon

# juste une fonction pour pas se faire chier à retaper du code
def pq():
    print("code :")
    code = input()
    print("nombre de chiffres concernés :")
    num =  input()
    return (code,num)

# Cette fonction servira à vérifier qu'un code potentiel ne contient pas de chiffre dans "rien n'est bon"
def check_charset(code,rb):
    for fr in rb:
        for c in code:
            if c in fr:
                return False
    return True

# Cette fonction servira à vérifier que le bon nombre de chiffre à la bonne position est présent dans un code potention
def match_jb(code,jb):
    valid_rule = 0
    for j in jb:
        x = 0
        match = 0
        for c in code:
            if c == j[0][x]:
                match = match + 1
            x = x + 1
        if match == int(j[1]):
            valid_rule = valid_rule + 1

    return valid_rule == len(jb)

# Bon chiffre, mauvaise position
def match_jm(code,jm):
    valid_rule = 0
    for j in jm:
        match = 0
        for c in code:
            if c in j[0]:
                match = match + 1
        if match >= int(j[1]):
            valid_rule = valid_rule + 1

    return valid_rule == len(jm)

# Cette fonction vérifie qu'il n'y a pas plus d'une occurence du même chiffre dans le code
def each_once(code):
    nums = "0123456789"
    for n in nums:
        if code.count(n) > 1: return False
    else:
        return True

# On génère toutes les solutions possible en 0 et le nombre max selon le nombre de chiffres (par ex, 4 chiffres, le nombre max est 9999. en comptant 0000 ça nous fait 10'000 solutions)
# Chaque solution possible passe par les 4 fonction ci-dessus. Puis une dernière fois, il est vérifié que "bon mais pas dans la bonne position" ne soit pas "bon et dans la bonne position".
# On vérifie aussi que chaque chiffre n'est pas à double.
# Tout ce qui passe ces cinq tests sort dans le terminal
def crack_da_code(l, jb,jm,rb):
    print()
    print("Résultats :")
    for code in range(0, (10**l)):
        code = str(code)
        while len(code) < l:
            code = "0" + code
        if check_charset(code, rb) and match_jb(code, jb) and match_jm(code,jm) and each_once(code) and not match_jb(code,jm):
            print(code)

# Cette fonction permet d'utiliser le programmer et d'enregistrer les paramètres
def menu():
    print("-------------------------")
    print("SUPER RAISOUDREUR DE CODE")
    print("-------------------------")
    print("Nombre de chiffres dans le code :")
    l = int(input())
    print()
    print("1 : Juste et bonne position")
    print("2 : Juste mais mauvaise position")
    print("3 : Rien n'est bon")
    print("4 : KALKULÄTE DER DIE DAS TZOLOUSSIONNE")
    while True :
        print("-------------------------")
        choice = int(input())
        if   choice == 1 :
            jb.append(pq())
        elif choice == 2 :
            jm.append(pq())
        elif choice == 3 :
            print("code :")
            rb.append(input())
        elif choice == 4 :
            break
        else :
            print("Yo ziva on t'a dit entre 1 et 3")
            print("Ca y est, t'as gagné, le programme se ferme")
            exit()
    crack_da_code(l, jb,jm,rb)


# ICI ON LANCE CETTE FONCTION ET C'EST PARTI MON KIKI
if __name__ == "__main__":
    menu()
