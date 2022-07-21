from cmath import exp
from math import inf as Infinity, pow

class Calculatrice:
    '''
        Classe utilitaire qui permet de faire des opération mathématiques simple
    '''

    def addition(self, nombre1, nombre2):
        '''
            Fonction qui additionne deux nombres et retourne le résultat

            params:
                nombre1: nombre
                nombre2: nombre

            return: resulat de l'addition
        '''
        return nombre1 + nombre2


    def division(self, numerateur, denominateur):
        '''
            Fonction qui retourne le résultat de la division du numérateur par le dénominateur

            params:
                numerateur: nombre
                denominateur: nombre
            return: resultat de la disivion
        '''

        if numerateur == 0:
            return 0

        if denominateur == 0 :
            return Infinity


        return numerateur / denominateur

    def puissance(self, nombre, exposant):
        '''
            Mets un nombre à la puissance indiqué et le retourne

            params:
                nombre: nombre
                exposant: nombre
            
            return: le nombre à la puissance exposant
        '''
        # return pow(nombre, exposant)
        return nombre ** exposant

