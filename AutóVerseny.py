#csapat;        versenyzo;     eletkor;   palya;                korido;     kor
#Versenylovak;  Fürge Ferenc;  29;        Gran Prix Circuit;    00:01:11;   1
#  0            1              2          3                     4           5

#függvény
def köridő(sor):
    '''
Ha bedobjuk a köridőt string-ként (00:00:00), akkor visszatér a másodpercekkel integer-ként!'''
    perc  = int(sor[4][3:5])
    sec   = int(sor[4][6:])
    return perc*60 + sec

#Előkészületek
with open("autoverseny.csv", 'r', encoding='UTF-8-sig') as f:
    fejlec = f.readline()
    matrix = [sor.strip().split(';') for sor in f]
    
#3.feladat
    
print(f' 3. feladat: {len(matrix)}')

#4.feladat

for sor in matrix:
    if sor[1] == 'Fürge Ferenc' and sor[5] == '3' and sor[3] == 'Gran Prix Circuit':       
        print(f' 4. feladat: {köridő(sor)} másodperc')
        
#5.feladat

print(f' 5. feladat:')
nev = input(f' Kérem egy versenyző nevét:\n')

#6.feladat

mini  = '99:99:99'
palya = ''
for sor in matrix:
    if sor[1] == nev:
        if sor[4] < mini:
            mini  = sor[4]
            palya = sor[3]
if palya == '':
    print(f' Nincs ilyen versenyző az állományban!')
else:
    print(f' 6. feladat: {palya},{mini}')
            