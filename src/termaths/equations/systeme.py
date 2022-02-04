
from termaths.matrice import *

def resoudre_systeme(self, A: Matrice, B: Matrice) -> Matrice:
	return A.getInverse().produit(B)

