taller = 1
taller= int(input('tryk 1 -> 1310nm eller 2 -> 1550nm'))
tab1310nm= 0.35# *10=3,5
sende=-9
modtage=-22
sikkerhedsmargin=3
reparationer=0.5
splidsning= 0.1#0.4
konnektor= 0.5#*4=2
pris1310= 7
tab1550nm= 0.2#2
pris1550= 8.5
while taller == 1:
    print("Du har nu valgt 1310nm")
    transcive=sende-modtage
    print("Brutto overskud", transcive,"dB")
    km1=int(input('Indtast længde i kilometer'))
    splidsninger=int(input('Indstast antal splidsninger'))
    Konnektor=int(input('Indtast antal konnektor'))
    samlet_tab1310=transcive-splidsning-konnektor-(tab1310nm*km1)
    print("Tab ved 1310nm",samlet_tab1310,"dB")
    netto_overskud=samlet_tab1310-sikkerhedsmargin-reparationer
    pris_ialt=pris1310*km1
    print('Netto overskud', netto_overskud, 'dB')
    print('Pris for 1310 ialt:', pris_ialt, 'Kr.')
    print('')
    taller = int(input('tryk 1 for 1310nm eller 2 for 1550nm'))

while taller == 2:
    print("Du har nu valgt 1550nm")
    transcive2=sende-modtage
    print("Brutto overskud",transcive2,"dB")
    km=int(input('Indtast længde i kilometer'))
    splidsninger=int(input('Indstast antal splidsninger'))
    konnektor2=int(input('Indtast antal konnektor'))
    samlet_tab1550=transcive2-splidsning-konnektor2-tab1550nm*km
    print("Tab ved 1550nm",samlet_tab1550,"dB")
    netto_overskud2=samlet_tab1550-sikkerhedsmargin-reparationer
    fiberpris=pris1550*km
    print('Netto overskud', netto_overskud2, 'dB')
    print("1550nm Fiber pris ialt:",fiberpris,'Kr.')
    print('')
    taller = int(input('tryk 1 for 1310nm eller 2 for 1550nm'))
