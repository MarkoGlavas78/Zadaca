class Kruznica(object):
    def __init__(self, radius):
        self.__radius=radius

    def radius(self):
        return self.__radius

    def __str__(self):
        return "kruznica radijusa %s" %("{:.2f}".format(self.__radius))


class Kvadrat(object):
    def __init__(self, stranica):
        self.__stranica=stranica

    def stranica(self):
        return self.__stranica

    def __str__(self):
        return "kvadrat stranice %s"%("{:.2f}".format(self.__stranica))

if __name__=="__main__":
    print('*** test likovi ***')
    kruznica = Kruznica(3)
    kvadrat = Kvadrat(4.5)
    print(kruznica)
    print(kvadrat)
