#csapat;        versenyzo;     eletkor;   palya;                korido;     kor
#Versenylovak;  Fürge Ferenc;  29;        Gran Prix Circuit;    00:01:11;   1
#  0            1              2          3                     4           5

#függvény
#def köridő(sor):
#     '''
#Ha bedobjuk a köridőt string-ként (00:00:00), akkor visszatér a másodpercekkel integer-ként!'''
#    perc  = int(sor[4][3:5])
#    sec   = int(sor[4][6:])
#    return perc*60 + sec

#Class
class Autóverseny:
    def __init__(self,sor):
        s = sor.strip().split(';')
        self.csapat        = s[0]
        self.versenyzo     = s[1]
        self.eletkor       = int(s[2])
        self.palya         = s[3]
        self.korido        = s[4]
        self.korido_sec    = int(s[4][:2])*3600 + int(s[4][3:5])*60 + int(s[4][6:])
        self.kor           = int(s[5])

#Előkészületek
with open("autoverseny.csv", 'r', encoding='UTF-8-sig') as f:
    fejlec = f.readline()
    matrix = [Autóverseny(sor) for sor in f]
    
#3.feladat
    
print(f' 3. feladat: {len(matrix)}')

#4.feladat

for sor in matrix:
    if sor.versenyzo == 'Fürge Ferenc' and sor.kor == 3 and sor.palya == 'Gran Prix Circuit':       
        print(f' 4. feladat: {sor.korido_sec} másodperc')
        
#5.feladat

print(f' 5. feladat:')
nev = input(f' Kérem egy versenyző nevét:\n')

#6.feladat

mini  = 2**32
palya = ''
for sor in matrix:
    if sor.versenyzo == nev:
        if sor.korido_sec < mini:
            mini   = sor.korido_sec
            palya  = sor.palya
            korido = sor.korido
if palya == '':
    print(f' Nincs ilyen versenyző az állományban!')
else:
    print(f' 6. feladat: {palya},{korido}')


    
            