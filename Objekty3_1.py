# Definice tridy

# Varianta 1 - trida BEZ vlastnosti, metod, ...
# class Zam():
#     pass

# Varianta 2 - trida s konstruktorem, vlastnostmi, metodami, ...
class Zam():
    LastID = 0      # promenna TRIDY, NIKOLI instance (nektere jazyky - staticka promenna)

    @staticmethod   # metoda TRIDY, NIKOLI instance
    def getLastID():    # (muze pouzivat POUZE STATICKE PROMENNE a volat jem STATICKE METODY)
        return Zam.LastID

    # definice konstruktoru (volan pri instancovani objektu)
    # self (1. parametr - obecne jakykoli nazev) je pointer na tu instanci
    # teto tridy (objekt), ve ktere je tento kod vykonavan (jine jazyky this)
    # def __init__(self,ID,Jmeno):    # ZVYKEM je pojmenovavat parametry za self
    #     self.ID = ID                # STEJNE jako vlastnosti, ktere chceme
    #     self.Jmeno = Jmeno          # hodnotami techto parametru inicializovat

    # Varianta 3 - konstruktor s "autoincrementem" (pouuziti staticke promenne)
    def __init__(self,Jmeno):
        Zam.LastID += 1             # pristup ke STATICKE promenne je PRES JMENO TRIDY!!
        self.ID = Zam.LastID
        self.Jmeno = Jmeno

    # definice metod
    def set_case(self,upper):       # self NUTNE i pro definici metod
        if upper:
            self.Jmeno = self.Jmeno.upper()  # self NUTNE pro praci s vlastnostmi objektu!!
        else:
            self.Jmeno = self.Jmeno.lower()

# Prace s objekty (=instancemi trid)

# Varianta 1 - trida BEZ vlastnosti, metod, ...
##objZam1 = Zam()             # vytvoreni objektu
##objZam1.Jmeno = "Franta"    # vytvoreni a naplneni vlastnosti jmeno
##
##objZam2 = Zam()             # vytvoreni 2. objektu
##objZam2.Jmeno = "Eva"
##
##print(objZam1.Jmeno,objZam2.Jmeno)
##
### stejne lze vytvaret metody - do vlastnosti priradime funkci (nebo lambda vyraz)
##
##objZam2.Titul = "Ing."      # vytvoreni vlastnosti Titul jen u objZam2
##print(objZam2.Titul)        # OK
### print(objZam1.Titul)      # chyba - objZam1 NEMA VLASTNOST Titul!!

# Varianta 2 - trida s konstruktorem, vlastnostmi, metodami, ...
##objZam1 = Zam(1,"Franta")     # instancovani pomoci konstruktoru (self se NEUVADI!!)
##objZam2 = Zam(2,"Eva")
##print(objZam1.ID,objZam1.Jmeno,objZam2.ID,objZam2.Jmeno)
##
##objZam2.Titul = "Ing."        # opet lze priradit novou vlastnost (metodu) "zvenku"
##
##objZam1.set_case(True)
##objZam2.set_case(False)
##print(objZam1.ID,objZam1.Jmeno,objZam2.ID,objZam2.Jmeno)

# Varianta 3 - konstruktor s "autoincrementem" (pouuziti staticke promenne)
objZam1 = Zam("Franta")
objZam2 = Zam("Eva")
print(objZam1.ID,objZam1.Jmeno,objZam2.ID,objZam2.Jmeno)

print(Zam.LastID)       # pristup ke staticke promenne zvenku (opet pres jmeno tridy)
print(Zam.getLastID())  # volani staticke metody

