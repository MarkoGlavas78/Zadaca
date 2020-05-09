import likovi
from math import pi

def opseg(lik):
    if isinstance(lik, likovi.Kruznica):
        return 2*lik.radius()*pi
    if isinstance(lik, likovi.Kvadrat):
        return 4*lik.stranica()

def povrsina(lik):
    if isinstance(lik, likovi.Kruznica):
        return lik.radius()*lik.radius()*pi
    if isinstance(lik, likovi.Kvadrat):
        return lik.stranica()*lik.stranica()

if __name__=="__main__":
    print('*** test funkcije ***')
    print(opseg.__name__)
    print(povrsina.__name__)
