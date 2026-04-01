# Fonctions données dans l'énoncé

type Permutation = list[int]

# Lecture d'une permutation
def Lire(texte: str = "s = ") -> Permutation:
   chaine = input(texte)
   return [int(x)-1 for x in chaine.split()]

# Formatage en chaîne
def Formater(s: Permutation) -> str:
   sortie = [i + 1 for i in s]
   if isinstance(s,tuple):
      return str(tuple(sortie))
   elif isinstance(s,set):
      return str(set(sortie))
   else:
      return str(sortie)


def EstPermutation(s: Permutation) -> bool:
    l = [False] * len(s)

    for item in s:
        if item > len(s)-1:
            return False

        if l[item]:
            # L'élément a déjà été visité, il y a donc un doublon
            return False

        l[item] = True

    return True


def Inverser(s: Permutation) -> Permutation:
    inverse: Permutation = [0] * len(s)

    for i in range(len(s)):
        inverse[s[i]] = i

    return inverse


def Composer(t: Permutation, s: Permutation) -> Permutation:
    compose: Permutation = [0] * len(t)

    for i in range(len(s)):
        compose[i] = t[s[i]]

    return compose


print(Composer([1, 4, 3, 2, 0, 5], [2, 4, 1, 5, 0, 3]))
