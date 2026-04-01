# Fonctions données dans l'énoncé
import math


type Permutation = list[int]
type TCycle = tuple[int, ...]
type Transposition = tuple[int, int]

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


def Orbite(k: int, s: Permutation) -> list[int]:
    orbite: list[int] = []

    last_value: int = s[k]
    orbite += [k]

    while last_value != k:
        orbite += [last_value]
        last_value = s[last_value]

    return orbite


def Cycle(s: Permutation) -> list[TCycle]:
    l: list[TCycle] = []
    B: list[bool] = [False] * len(s)

    for i in range(len(s)):
        if not B[i]:
            orbite = Orbite(i, s)

            if len(orbite) > 1:
                cycle: tuple[int, ...] = tuple()

                while len(orbite) > 0:
                    element = orbite.pop(0)
                    B[element] = True
                    cycle += (element,)

                l += [cycle]

    return l


def Transpositions(s: Permutation) -> list[Transposition]:
    l: list[Transposition] = []
    cycles = Cycle(s)

    for cycle in cycles:
        buffer = tuple()

        for item in cycle:
            buffer += (item,)

            if len(buffer) == 2:
                l += [buffer]
                buffer = (item,)

    return l


def Signature(s: Permutation) -> int:
    return (-1) ** len(Transpositions(s)) # pyright: ignore[reportAny]

t = [3, 5, 1, 2, 0, 4, 6]
print(Cycle(t))
print(Transpositions(t))
