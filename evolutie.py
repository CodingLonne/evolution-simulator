from tkinter import *
from math import sqrt, cos, sin, atan2, pi, floor, log10, ceil, floor, copysign
from random import randint, choice, uniform, shuffle, random
from time import sleep
#simulatie scherm
HEIGHT = 500
WIDTH = 500
sw = 400
sh = 500
window = Tk()
c = Canvas(window, height=HEIGHT, width=WIDTH, bg="black")
s = Canvas(window, bg='#01c4ff',width=sw, height=sh)
window.title('natuurlijke selectie')
c.grid(row=0, column=0)
s.grid(row=0, column=1)
#hoofd design stats
buf = 10
modussen = ['balken', 'grafiek', 'alle ids']
modussenIds = []
HuidigeModus = modussen[0]
HoogteNav = 40
for i in range(len(modussen)):
    rect = s.create_rectangle(buf+(sw-2*buf)/len(modussen)*i, buf,
                              buf+(sw-2*buf)/len(modussen)*(i+1), buf+HoogteNav, fill="white")
    text = s.create_text((sw-2*buf)/len(modussen)*(i+0.5), buf+HoogteNav/2, text=modussen[i])
    modussenIds.append([rect, text])

#grafiek/balken
HoogteGrafiek = 100
startPagina = 2*buf+HoogteNav
GrafiekCoords = {}
AchterWitIDs = {}
GrafiekLijn = {}
GrafiekSoorten = ['radius', 'speed', 'zicht', 'bevolking', 'eten']
GrafiekKleur = {'radius' : 'blue', 'speed' : 'red', 'zicht' : 'aqua', 'bevolking' : 'blue',
                'eten' : '#ff00ff'}
AantalBalkjes = 40
VorigeBalkenSchaal = {soort : 0 for soort in ['radius', 'speed', 'zicht']}
BreedteBalkjes = (sw-2*buf)/AantalBalkjes
BalkenIDs = {}
BalkenCijfersIDs = {}
for i in range(len(GrafiekSoorten)-1):
    coords = [buf, startPagina+i*(HoogteGrafiek+buf),
              sw-buf, startPagina+i*(HoogteGrafiek+buf)+HoogteGrafiek]
    GrafiekCoords[GrafiekSoorten[i]] = coords.copy()
    AchterWitIDs[GrafiekSoorten[i]] = s.create_rectangle(coords, fill="white")
    GrafiekLijn[GrafiekSoorten[i]] = s.create_line(coords[0], coords[3],
                                                  coords[2], coords[3],
                                                   fill=GrafiekKleur[GrafiekSoorten[i]])
    if GrafiekSoorten[i] in ['radius', 'speed', 'zicht', 'bevolking']:
        if GrafiekSoorten[i] != 'bevolking':
            BalkenIDs[GrafiekSoorten[i]] = []
            for x in range(AantalBalkjes):
                ID = s.create_rectangle(buf+x*BreedteBalkjes, coords[3],
                                        buf+(x+1)*BreedteBalkjes, coords[3],
                                        fill=GrafiekKleur[GrafiekSoorten[i]])
                BalkenIDs[GrafiekSoorten[i]].append(ID)
        BalkenCijfersIDs[GrafiekSoorten[i]] = []
        for x in range(6):
            ID = s.create_text(coords[0], coords[3])
            BalkenCijfersIDs[GrafiekSoorten[i]].append(ID)
BalkenCijfersIDs['eten'] = BalkenCijfersIDs['bevolking']
GrafiekCoords['eten'] = GrafiekCoords['bevolking']
AchterWitIDs['eten'] = AchterWitIDs['bevolking']
GrafiekLijn['eten'] = s.create_line(coords[0], coords[3],
                              coords[2], coords[3],
                              fill="#ff00ff")
balkenPagina = [AchterWitIDs[name] for name in ['radius', 'speed', 'zicht']]
for soort in ['radius', 'speed', 'zicht']:
    balkenPagina += BalkenIDs[soort]
    balkenPagina += BalkenCijfersIDs[soort]
grafiekPagina = [AchterWitIDs[name] for name in AchterWitIDs] + \
                [GrafiekLijn[name] for name in GrafiekLijn]
for soort in ['radius', 'speed', 'zicht', 'bevolking']:
    grafiekPagina += BalkenCijfersIDs[soort]
#alle ids
IdsY = 0
selectedID = 0
paspoorten = [] #lijst van gegevens van verschillende
paspoortIDs = []
HoogtePaspoort = 50
IDFont = 'Courier'
IDFontSize = 12
IdentiteitsVB = [s.create_rectangle(buf, startPagina,
                                    sw-buf, startPagina+HoogtePaspoort,
                                    fill='white'),
                 s.create_text(buf+25, startPagina+25,
                               fill='black', text='ID', font=(IDFont, 50)),
                 s.create_text(buf+200, startPagina+25, fill='blue',
                               text='Grootte' + 30*' ', font=(IDFont, IDFontSize)),
                 s.create_text(buf+200, startPagina+25, fill='red',
                               text=8*' ' + 'Speed' + 24*' ', font=(IDFont, IDFontSize)),
                 s.create_text(buf+200, startPagina+25, fill='aqua',
                               text=14*' ' + 'Zicht' + 18*' ', font=(IDFont, IDFontSize)),
                 s.create_text(buf+200, startPagina+25, fill='#ff8800',
                               text=20*' ' + 'Conditie' + 9*' ', font=(IDFont, IDFontSize)),
                 s.create_text(buf+200, startPagina+25, fill='magenta',
                               text=29*' ' + 'Leeftijd', font=(IDFont, IDFontSize)),
                 s.create_rectangle(sw-buf-20, startPagina+5,
                                    sw-buf-10, startPagina+HoogtePaspoort-5,
                                    fill='red'),
                 s.create_rectangle(sw-buf-20, startPagina+15,
                                    sw-buf-10, startPagina+HoogtePaspoort-5,
                                    fill='green')]
IDsPagina = IdentiteitsVB + []
#namen ids
letters = [['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z'],
           ['a', 'e', 'i', 'o', 'u', 'aa', 'au', 'ee', 'ei', 'eu', 'ie', 'oe', 'oo', 'ou', 'uu', 'ij'],
           ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'x', 'z'],
           ['a', 'e', 'i', 'o', 'u', 'aa', 'au', 'ee', 'ei', 'eu', 'ie', 'oe', 'oo', 'ou', 'uu', 'ij'],
           ['b', 'c', 'd', 'f', 'g', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'x']]
for i in range(len(letters)):
    shuffle(letters[i])
#alle 3 de pagina's
paginaIDs = {'balken' : balkenPagina, 'grafiek' : grafiekPagina, 'alle ids' : IDsPagina}
#collecting data
GemRad = []
MaxRad = 0
GemSpeed = []
MaxSpeed = 0
GemZicht = []
MaxZicht = 0
NumEten = []
MaxEten = 0
NumBevolking = []
MaxBevolking = 0
#variabele
Achtergrond = c.create_oval(0, 0, WIDTH, HEIGHT, fill="white")
Populatie = c.create_text(0, 0, anchor="nw", fill="white",
                            font=('Helvetica', 20), text='Populatie:')
PopulatieID = c.create_text(0, 30, anchor="nw", fill="white",
                            font=('Helvetica', 40), text=0)
VoedselNum = c.create_text(WIDTH, 0, anchor="ne", fill="white",
                            font=('Helvetica', 20), text='Voedsel:')
VoedselNumID = c.create_text(WIDTH, 30, anchor="ne", fill="white",
                            font=('Helvetica', 40), text=0)
RadiusAchtergrond = WIDTH/2
buffer = 20
SnoepRadius = 3
StartEnergie = 150000
MinFactor = 0.9
#lijsten
VoedselPos = []
VoedselId = []
CId = []
CPosities = []
CRadius = []
CSpeed = []
CRichting = []
CEnergie = []
CVoedsel = []
CZicht = []
CActiviteit = []
CLeeftijd = []
#korte rekenfuncties
def afstand(x, y):
    return sqrt(x**2 + y**2)
def afstand_center(x, y):
    return afstand(x-RadiusAchtergrond, y-RadiusAchtergrond)
def afstand_rand(x, y):
    AfstandMidden = afstand_center(x, y)
    return RadiusAchtergrond-AfstandMidden  
def rich_to_coord(rich, lengte):
    x = lengte*sin(rich)
    y = -lengte*cos(rich)
    return x, y
def rich(x, y):
    rich = atan2(x, -y)
    return rich
def coord_to_rich(x, y):
    richting = rich(x, y)
    lengte = afstand(x, y)
    return rich, lengte
#korte functies voor stats
def add(lijst):
    som = 0
    for i in lijst:
        som += i
    return som
def product(lijst):
    pro = 1
    for i in lijst:
        pro *= i
    return pro
def gemiddelde(lijst):
    som = add(lijst)
    if len(lijst)==0:
        gem = 0
    else:
        gem = som/len(lijst)
    return gem
def state(lijstIDs, State):
    for ID in lijstIDs:
        s.itemconfig(ID, state=State)
def selecteer(num):
    for i in range(len(paspoortIDs)):
        s.itemconfig(paspoortIDs[i][0], width=1)
    s.itemconfig(paspoortIDs[num][0], width=3)
def beveilig_afwijkingen(getal):
    string = str(getal)
    if len(string)>3:
        if (string[len(string)-1] != '0') and ((string[len(string)-2] == '0') or (string[len(string)-2] == '.' and string[len(string)-3] == '0')):
            string = string[:len(string)-1] + '0'
            if '.' in string:
                getal = float(string)
            else:
                getal = int(string)
    string = str(getal)
    if len(string)>6 and string[len(string)-5:].count('9')>=3:
        punt = string.index('.')
        plusF = '0.'
        for i in range(punt+1, len(string)-1, 1):
            plusF = plusF + '0'
        plusF += '1'
        LenF = 10 - int(string[len(string)-1])
        PlusF = float(plusF)*LenF
        getal += PlusF
    if getal == int(getal):
        getal = int(getal)
    return getal
#verschillende scherm updates
def update_grafiek(ID, coords, lijst, maxItem, soort):
    if len(lijst)==0:
        s.coords(ID, coords[0], coords[3], coords[2], coords[3])
    else:
        f = HoogteGrafiek/maxItem
        if len(lijst)==1:
            s.coords(ID, coords[0], lijst[0]*f, coords[2], lijst[0]*f)
        else:
            a = (sw-2*buf)/(len(lijst)-1)
            co = []
            for i in range(len(lijst)):
                co.append(coords[0]+i*a)
                co.append(coords[3]-lijst[i]*f)
            s.coords(ID, co)
    if len(lijst)>0:
        tussen = data_punten(len(lijst), 5)
        BreedteScherm = sw-2*buf
        Interval = BreedteScherm/len(lijst)
        for i in range(6):
            if Interval*(tussen*i)>BreedteScherm:
                break
            s.coords(BalkenCijfersIDs[soort][i], buf+Interval*(tussen*i), coords[3])
            s.itemconfig(BalkenCijfersIDs[soort][i],
                         text=str(beveilig_afwijkingen(tussen*i)),
                         state=NORMAL)
    else:
        i = 0
    for i in range(i, 6):
        s.itemconfig(BalkenCijfersIDs[soort][i], state=HIDDEN)
def data_punten(Max, aantalPunten):
    a = Max/aantalPunten
    tal = floor(log10(a))
    aangepasteA = a/(10**tal)
    afgerondeA = ceil(aangepasteA)
    nieuweA = afgerondeA*(10**tal)
    return beveilig_afwijkingen(nieuweA)
def verdeel_balken(lijst, waardeGebied, aantal):
    aantallen = [0 for i in range(aantal)]
    for i in lijst:
        aantallen[int(i/waardeGebied)] += 1
    return aantallen
def schaal(gemiddelde, Max, vorige):
    if Max>vorige:
        output = max([gemiddelde, Max])
    elif max([gemiddelde, Max])*1.2<vorige:
        output = max([gemiddelde, Max])
    else:
        output = vorige
    return output
def update_balken(soort, lijst, Coords):
    global VorigeBalkenSchaal
    Max = VorigeBalkenSchaal[soort] = schaal(gemiddelde(lijst)*2, max(lijst)*1.1,
                                             VorigeBalkenSchaal[soort])
    aantallen = verdeel_balken(lijst, Max/AantalBalkjes, AantalBalkjes)
    MaxWaarde = max(aantallen)
    f = HoogteGrafiek/MaxWaarde
    for i in range(AantalBalkjes):
        co = s.coords(BalkenIDs[soort][i])
        co[1] = co[3]-f*aantallen[i]
        s.coords(BalkenIDs[soort][i], co)
    tussen = data_punten(Max, 5)
    BreedteScherm = sw-2*buf
    Interval = BreedteScherm/Max
    for i in range(6):
        if Interval*(tussen*i)>BreedteScherm:
            break
        s.coords(BalkenCijfersIDs[soort][i], buf+Interval*(tussen*i), Coords[3])
        s.itemconfig(BalkenCijfersIDs[soort][i],
                     text=str(beveilig_afwijkingen(tussen*i)),
                     state=NORMAL)
    for i in range(i, 6):
        s.itemconfig(BalkenCijfersIDs[soort][i], state=HIDDEN)
def show_grafieken():
    update_grafiek(GrafiekLijn['radius'], GrafiekCoords['radius'], GemRad, MaxRad, 'radius')
    update_grafiek(GrafiekLijn['speed'], GrafiekCoords['speed'], GemSpeed, MaxSpeed, 'speed')
    update_grafiek(GrafiekLijn['zicht'], GrafiekCoords['zicht'], GemZicht, MaxZicht, 'zicht')
    update_grafiek(GrafiekLijn['bevolking'], GrafiekCoords['bevolking'], NumBevolking,
                   max([MaxBevolking, MaxEten]), 'bevolking')
    update_grafiek(GrafiekLijn['eten'], GrafiekCoords['eten'], NumEten,
                   max([MaxBevolking, MaxEten]), 'eten')
def show_balken():
    if len(CRadius)>0 and len(CSpeed)>0 and len(CZicht)>0:
        update_balken('radius', CRadius, GrafiekCoords['radius'])
        update_balken('speed', CSpeed, GrafiekCoords['speed'])
        update_balken('zicht', CZicht, GrafiekCoords['zicht'])
#gegevens
def werk_data_bij():
    global MaxRad, MaxSpeed, MaxZicht, MaxEten, MaxBevolking, paspoorten
    #radius
    gemrad = gemiddelde(CRadius)
    GemRad.append(gemrad)
    if MaxRad<gemrad:
        MaxRad = gemrad
    #speed
    gemspeed = gemiddelde(CSpeed)
    GemSpeed.append(gemspeed)
    if MaxSpeed<gemspeed:
        MaxSpeed = gemspeed
    #zicht
    gemzicht = gemiddelde(CZicht)
    GemZicht.append(gemzicht)
    if MaxZicht<gemzicht:
        MaxZicht=gemzicht
    #eten wordt in hoofdloop gedaan
    #bevolking
    if len(NumBevolking)>0 and MaxBevolking<NumBevolking[len(NumBevolking)-1]:
        MaxBevolking=NumBevolking[len(NumBevolking)-1]
    paspoorten_data()
def paspoorten_data():
    global paspoorten
    paspoorten = []
    for ID in range(len(CId)):
        Paspoort = (CId[ID], CRadius[ID], CSpeed[ID], CZicht[ID],
                    conditie(ID), CLeeftijd[ID])
        paspoorten.append(Paspoort)
def add_paspoort():
    global IDsPagina
    start = startPagina+HoogtePaspoort+buf
    rechthoek = s.create_rectangle(buf, start,
                                    sw-buf, start+HoogtePaspoort,
                                    fill='white')
    Id = s.create_text(buf+190, start+25,
                       fill='black', text='ID', font=(IDFont, IDFontSize)),
    Grootte = s.create_text(buf+190, start+25, fill='blue',
                            font=(IDFont, IDFontSize)),
    Speed = s.create_text(buf+190, start+25, fill='red',
                          font=(IDFont, IDFontSize)),
    Zicht = s.create_text(buf+190, start+25, fill='aqua',
                          font=(IDFont, IDFontSize)),
    Conditie = s.create_text(buf+190, start+25, fill='#ff8800',
                             font=(IDFont, IDFontSize)),
    Leeftijd = s.create_text(buf+190, start+25, fill='magenta',
                             font=(IDFont, IDFontSize))
    Balkje = s.create_rectangle(sw-buf-20, start+5,
                                sw-buf-10, start+HoogtePaspoort-5,
                                fill='red'),
    Fuel = s.create_rectangle(sw-buf-20, start+15,
                              sw-buf-10, start+HoogtePaspoort-5,
                              fill='green')
    paspoort = (rechthoek, Id, Grootte, Speed, Zicht,
                Conditie,Leeftijd, Balkje, Fuel)
    paspoortIDs.append(paspoort)
    IDsPagina += list(paspoort)
def naam_id(aantal):
    ll = [len(i) for i in letters]
    aantal = aantal % product(ll)
    indexen = []
    naam = ''
    for i in range(len(letters)):
        h = product([ll[a] for a in range(i+1, len(ll))])
        index = floor(aantal/h)
        aantal -= index*h
        naam += letters[i][index]
    return naam
def werk_paspoort_bij(num, ynum):
    paspoort = paspoorten[ynum]
    data = [naam_id(paspoort[0]), str(round(paspoort[1], 2)), str(round(paspoort[2], 2)),
            str(round(paspoort[3], 2)), str(round(paspoort[4], 2)), str(round(paspoort[5], 2))]
    '''ID = naam_id(paspoort[num][0])
    Grootte = str(round(CRadius[num], 2))
    Speed = str(round(CSpeed[num], 2))
    Zicht = str(round(CZicht[num], 2))
    Conditie = str(round(conditie(num), 2))
    Leeftijd = str(CLeeftijd[num])
    #data = [ID, Grootte, Speed, Zicht, Conditie, Leeftijd]'''
    lengths = [len(i) for i in data]
    fontSize = int((sw-50)/add(lengths)*1.25)
    for i in range(6):
        leftBuf = add([lengths[d] for d in range(0, i)]) + i
        RightBuf = add([lengths[d] for d in range(i+1, len(data))]) + len(data)-i
        s.itemconfig(paspoortIDs[ynum][1+i], text=leftBuf*' ' + data[i] + RightBuf*' ',
                     font=(IDFont, fontSize))
def scroll_id(ynum, num):
    y = IdsY+ynum*(buf+HoogtePaspoort)
    start = startPagina+HoogtePaspoort+buf
    lijstIds = paspoortIDs[ynum]
    s.coords(lijstIds[0], buf, y+start, sw-buf, y+start+HoogtePaspoort) #achtergrond
    for i in range(1, 7):
        s.coords(lijstIds[i], buf+190, y+start+25)
    s.coords(lijstIds[7], sw-buf-20, y+start+5, sw-buf-10, y+start+HoogtePaspoort-5)
    if paspoorten[ynum][0] in CId:
        energie = CEnergie[CId.index(paspoorten[ynum][0])]
        if energie != 'dood':
            s.coords(lijstIds[8], sw-buf-20, y+start+HoogtePaspoort-5, sw-buf-10,
                     y+start+HoogtePaspoort-5-(energie/StartEnergie*40))
        else:
            s.coords(lijstIds[8], sw-buf-20, y+start+HoogtePaspoort-5,
                     sw-buf-10, y+start+HoogtePaspoort-5)
    else:
        s.coords(lijstIds[8], sw-buf-20, y+start+HoogtePaspoort-5,
                 sw-buf-10, y+start+HoogtePaspoort-5)
def scroll():
    global IdsY
    naarY = -((selectedID-3)*(buf+HoogtePaspoort))
    #IdsY = naarY
    if naarY<IdsY-80:
        IdsY += (naarY-IdsY)/6+5
    elif naarY>IdsY+80:
        IdsY -= -(naarY-IdsY)/6+5
    if IdsY>0:
        IdsY = 0
    for ID in IdentiteitsVB:
        s.tag_raise(ID)
    for ID in range(len(paspoortIDs)):
        hoogte = startPagina+IdsY+(ID + 1)*(HoogtePaspoort+buf)
        if 60<hoogte<sh and ID<len(paspoorten):
            scroll_id(ID, ID)
            werk_paspoort_bij(ID, ID)
            state(paspoortIDs[ID], NORMAL)
        else:
            state(paspoortIDs[ID], HIDDEN)
def werk_paspoorten_bij():
    global selectedID
    for i in range(len(paspoortIDs), len(CId)):
        add_paspoort()
    for ID in range(len(paspoortIDs)):
        hoogte = startPagina+IdsY+(ID + 1)*(HoogtePaspoort+buf)
        if 60<hoogte<sh and ID<len(paspoorten):
            werk_paspoort_bij(ID, ID)
            scroll_id(ID, ID)
            state(paspoortIDs[ID], NORMAL)
        else:
            state(paspoortIDs[ID], HIDDEN)
    if selectedID>=len(paspoorten):
        selectedID = len(paspoorten)-1
    if selectedID<0:
        selectedID=0
    if len(paspoorten)!=0:
        selecteer(selectedID)
def show_gegevens():
    if HuidigeModus=='balken':
        show_balken()
    elif HuidigeModus=='grafiek':
        show_grafieken()
    else:
        werk_paspoorten_bij()
        scroll()
#switch gegevens
def switch_pagina():
    for i in range(3):
        s.itemconfig(modussenIds[i][0], width=1)
    s.itemconfig(modussenIds[modussen.index(HuidigeModus)][0], width=3)
    for IDs in paginaIDs:
        state(paginaIDs[IDs], HIDDEN)
    state(paginaIDs[HuidigeModus], 'normal')
    show_gegevens()
def toetsen(event):
    global HuidigeModus, IdsY, selectedID
    letter = event.keysym
    if letter=='1':
        HuidigeModus = 'balken'
        switch_pagina()
    elif letter=='2':
        HuidigeModus = 'grafiek'
        switch_pagina()
    elif letter=='3':
        HuidigeModus = 'alle ids'
        switch_pagina()
    elif letter=='Up':
        selectedID -= 1
        if selectedID<0:
            selectedID=0
        selecteer(selectedID)
        scroll()
    elif letter == 'Down':
        selectedID += 1
        if selectedID>=len(paspoorten):
            selectedID=len(paspoorten)-1
        selecteer(selectedID)
        scroll()
s.bind_all('<Key>', toetsen)
#klikken op evolutiescherm
def klik_c(eventorigin):
    x = eventorigin.x
    y = eventorigin.y
c.bind("<Button 1>",klik_c)
#klikken op 
def klik_s(eventorigin):
    global HuidigeModus
    x = eventorigin.x
    y = eventorigin.y
    if buf<y<buf+HoogteNav:
        x1 = x-buf
        breedteKnop = (sw-2*buf)/len(modussen)
        if 0*breedteKnop<x1<1*breedteKnop:
            HuidigeModus = 'balken'
            switch_pagina()
        elif 1*breedteKnop<x1<2*breedteKnop:
            HuidigeModus = 'grafiek'
            switch_pagina()
        elif 2*breedteKnop<x1<3*breedteKnop:
            HuidigeModus = 'alle ids'
            switch_pagina()
s.bind("<Button 1>",klik_s)
#coordinaten in cirkel
def coord_in_circle():
    done = True
    while done:
        x = randint(0, WIDTH)
        y = randint(0, HEIGHT)
        if afstand_center(x, y)<RadiusAchtergrond-SnoepRadius-buffer:
            done = False
    return x, y
#factor van variatie
def factor():
    n = uniform(MinFactor, 1)
    if choice([True, False]):
        n = 1/n
    return n
#snoep functies
def maak_snoep(x, y):
    ID = c.create_oval(x-SnoepRadius, y-SnoepRadius, x+SnoepRadius, y+SnoepRadius, fill='green')
    VoedselId.append(ID)
    VoedselPos.append([x, y])
def leg_snoep_neer(aantal):
    for i in range(aantal):
        x, y = coord_in_circle()
        maak_snoep(x, y)
def cancel_snoep(snoepID):
    c.delete(VoedselId[snoepID])
    VoedselPos[snoepID] = "op"
    VoedselId[snoepID] = "op"
def verwijder_snoep(snoepID):
    del VoedselPos[snoepID]
    del VoedselId[snoepID]
def haal_snoep_weg():
    for i in range(len(VoedselId)-1, -1, -1):
        if VoedselId[i]!='op':
            cancel_snoep(i)
        verwijder_snoep(i)
#kleuren
def RGB(r, g, b):
    R = [floor(r / 16), r - (16 * (floor(r / 16)))]
    G = [floor(g / 16), g - (16 * (floor(g / 16)))]
    B = [floor(b / 16), b - (16 * (floor(b / 16)))]
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'a', 'b', 'c', 'd', 'e', 'f']
    R[0] = num[R[0]]
    R[1] = num[R[1]]
    G[0] = num[G[0]]
    G[1] = num[G[1]]
    B[0] = num[B[0]]
    B[1] = num[B[1]]
    hexa = '#' + R[0] + R[1] + G[0] + G[1] + B[0] + B[1]
    return hexa
def snelheid_to_color(snelheid):
    g = int(snelheid*20)
    if g>255:
        g = 255
    return RGB(255, g, 0)
#wezen functies
def cancel_wezen(ID):
    c.delete(CId[ID])
    CId[ID] = "dood"
    CPosities[ID] = "dood"
    CRadius[ID] = "dood"
    CSpeed[ID] = "dood"
    CRichting[ID] = "dood"
    CEnergie[ID] = "dood"
    CVoedsel[ID] = "dood"
    CZicht[ID] = "dood"
    CLeeftijd[ID] = "dood"
def verwijder_wezen(ID):
    del CId[ID]
    del CPosities[ID]
    del CRadius[ID]
    del CSpeed[ID]
    del CRichting[ID]
    del CEnergie[ID]
    del CVoedsel[ID]
    del CZicht[ID]
    del CLeeftijd[ID]
def maak_wezen(x, y, Rad, Zicht, speed):
    ID = c.create_oval(x-Rad, y-Rad, x+Rad, y+Rad, fill=snelheid_to_color(speed))
    CId.append(ID)
    CPosities.append([x, y])
    CRadius.append(Rad)
    CSpeed.append(speed)
    CRichting.append(rich(x-RadiusAchtergrond, y-RadiusAchtergrond))
    CEnergie.append(StartEnergie)
    CVoedsel.append(0)
    CZicht.append(Zicht)
    CLeeftijd.append(0)
    c.itemconfig(PopulatieID, text=len(CId))
    paspoorten_data()
    if HuidigeModus == 'alle ids':
        werk_paspoorten_bij()
def maak_wezens(aantal):
    Rad, Zicht, speed = 5, 40, 2
    hoek = (2*pi)/aantal
    for i in range(aantal):
        x, y = rich_to_coord(hoek*i, RadiusAchtergrond)
        x, y = x+RadiusAchtergrond, y+RadiusAchtergrond
        maak_wezen(x, y, Rad, Zicht, speed)
    NumBevolking.append(len(CId))
    werk_data_bij()
    show_gegevens()
#beweging
def loop(ID, rich, speed):
    if CEnergie[ID]>=0:
        x, y = rich_to_coord(rich, speed)
        c.move(CId[ID], x, y)
        CPosities[ID] = [CPosities[ID][0]+x, CPosities[ID][1]+y]
        CRichting[ID] = rich
        CEnergie[ID] = CEnergie[ID]-(CRadius[ID]**3*CSpeed[ID]**2+CZicht[ID])
        CActiviteit[ID] = True
def conditie(ID):
    afstand = CEnergie[ID]/(CRadius[ID]**3*CSpeed[ID]**2+CZicht[ID])*CSpeed[ID]
    return afstand
#kijk/denk -functies
def vijand(ID):
    BelangrijksteVijand = 'none'
    AfstandTotVijand = 'none'
    MinGrootte = CRadius[ID]*1.2
    pos = CPosities[ID]
    zicht = CZicht[ID]
    for i in range(len(CRadius)-1, -1, -1):
        if CId[i] == 'dood':
            continue
        if CRadius[i]>=MinGrootte:
            pos2 = CPosities[i]
            a = afstand(pos[0]-pos2[0], pos[1]-pos2[1])
            if a<zicht:
                if BelangrijksteVijand == 'none':
                    BelangrijksteVijand = i
                    AfstandTotVijand = a
                elif a<AfstandTotVijand:
                    BelangrijksteVijand = i
                    AfstandTotVijand = a
    if BelangrijksteVijand == 'none':
        return False
    else:
        vx, vy = CPosities[BelangrijksteVijand]
        richting = rich(vx-pos[0], vy-pos[1])
        richting += pi
        loop(ID, richting, CSpeed[ID])
        return True
def eet_prooi(ID, prooiID):
    CVoedsel[ID] += 2
    cancel_wezen(prooiID)
def kanibaal(ID):
    BelangrijksteProoi = 'none'
    AfstandTotProoi = 'none'
    MaxGrootte = CRadius[ID]/1.2
    pos = CPosities[ID]
    zicht = CZicht[ID]
    for i in range(len(CRadius)-1, -1, -1):
        if CId[i] == "dood":
            continue
        if CRadius[i]<=MaxGrootte:
            pos2 = CPosities[i]
            a = afstand(pos[0]-pos2[0], pos[1]-pos2[1])
            if a<CRadius[ID]+CRadius[i]: #als ik hem raak
                if CId[i] != 'dood':
                    eet_prooi(ID, i) #eet op
                    continue
            if a<zicht: # zie ik hem?
                if BelangrijksteProoi == 'none':
                    BelangrijksteProoi = i
                    AfstandTotProoi = a
                elif a<AfstandTotProoi:
                    BelangrijksteProoi = i
                    AfstandTotProoi = a
    return BelangrijksteProoi
def eet(ID, snoepID):
    cancel_snoep(snoepID)
    CVoedsel[ID] += 1
def snoep(ID):
    DichtsteVoedsel = "none"
    AfstandVoedsel = "none"
    pos = CPosities[ID]
    zicht = CZicht[ID]
    for i in range(len(VoedselId)-1, -1, -1):
        if VoedselId[i]=="op":
            continue
        pos2 = VoedselPos[i]
        a = afstand(pos[0]-pos2[0], pos[1]-pos2[1])
        if a<SnoepRadius+CRadius[ID]:
            eet(ID, i)
            continue
        if a<zicht:
            if DichtsteVoedsel == "none":
                DichtsteVoedsel = i
                AfstandVoedsel = a
            elif a<AfstandVoedsel:
                DichtsteVoedsel = i
                AfstandVoedsel = a
    return DichtsteVoedsel
#voedsel denk functie
def voedsel(ID):
    PosId = CPosities[ID]
    snoepje = snoep(ID)
    prooi = kanibaal(ID)
    if prooi=="none" and snoepje=="none":
        return False
    else:
        if prooi=="none" and snoepje != "none": #ziet een snoepje
            pos = VoedselPos[snoepje]
            soort="snoepje"
            voedselId = snoepje
        elif prooi!="none" and snoepje=="none":#ziet prooi
            pos = CPosities[prooi]
            soort="prooi"
            voedselId = prooi
        else:
            PosProoi = CPosities[prooi]
            AfstandProoi = afstand(PosProoi[0]-PosId[0], PosProoi[1]-PosId[1])
            PosSnoep = VoedselPos[snoepje]
            AfstandSnoepje = afstand(PosSnoep[0]-PosId[0], PosSnoep[1]-PosId[1])
            if AfstandSnoepje<AfstandProoi:
                soort='snoepje'
                pos = PosSnoep
                voedselId = snoepje
            else:
                soort = 'prooi'
                pos = PosProoi
                voedselId = prooi
        #beslissing
        if CVoedsel[ID]==0:
            loop(ID, rich(pos[0]-PosId[0], pos[1]-PosId[1]), CSpeed[ID])#loop erheen
        elif CVoedsel[ID]==1:
            if conditie(ID)>afstand(PosId[0]-pos[0], PosId[1]-pos[1]) + \
               afstand_rand(pos[0], pos[1]):
                loop(ID, rich(pos[0]-PosId[0], pos[1]-PosId[1]), CSpeed[ID]) #loop erheen
            else:
                if afstand_center(CPosities[ID][0], CPosities[ID][1])<RadiusAchtergrond:
                    loop(ID, rich(PosId[0]-RadiusAchtergrond,
                                  PosId[1]-RadiusAchtergrond),
                         CSpeed[ID]) #loop naar de rand
                
        else:
            loop(ID, rich(PosId[0]-RadiusAchtergrond,
                          PosId[1]-RadiusAchtergrond),
                 CSpeed[ID])
        return True
#korte opdrachten
def geef_energie():
    for ID in range(len(CId)):
        CEnergie[ID] = StartEnergie
def magen_leeg():
    for ID in range(len(CId)):
        CVoedsel[ID] = 0
#zoekend rondbewegen in geval van geen functie in zicht
def dwaal(ID):
    if afstand_center(CPosities[ID][0], CPosities[ID][1])<RadiusAchtergrond:
        loop(ID, CRichting[ID], CSpeed[ID]) #loop rechtdoor
    else:
        loop(ID, rich(RadiusAchtergrond-CPosities[ID][0],
                      RadiusAchtergrond-CPosities[ID][1]),
             CSpeed[ID]) #loop naar het midden
#gaspecialiseerde functie
def richt_naar_midden():
    for ID in range(len(CId)):
        CRichting[ID] = rich(RadiusAchtergrond-CPosities[ID][0],
                             RadiusAchtergrond-CPosities[ID][1])
#brein van de wezens
def brein(ID):
    actief = True
    if not vijand(ID): #als er geen vijand te zien is
        if not voedsel(ID): #als er geen voedsel te zien is
            if CVoedsel[ID]>0: # als ik al voedsel heb gehad
                if afstand_center(CPosities[ID][0], CPosities[ID][1])<RadiusAchtergrond:
                    #als ik nog niet thuis ben
                    loop(ID, rich(CPosities[ID][0]-RadiusAchtergrond,
                                  CPosities[ID][1]-RadiusAchtergrond),
                         CSpeed[ID]) #loop naar huis
            else: #als ik nog geen voedsel heb gehad
                dwaal(ID) #dwaal rond op zoek naar voedsel
#simpele onderhouds functies
def clean_up(): #simpele functie voor complete verwijdering van wezens
    for ID in range(len(CId)-1, -1, -1):
        if CId[ID] == 'dood':
            verwijder_wezen(ID)
def nacht(): #laat wezens overlijden
    for ID in range(len(CId)-1, -1, -1):
        if afstand_center(CPosities[ID][0],
                          CPosities[ID][1])<RadiusAchtergrond or CVoedsel[ID] == 0:
            #als ze nog niet thuis zijn of verhongerd zijn
            cancel_wezen(ID) #dit verwijderd de gegevens en de visuele representatie van het wezen,
            #maar nog niet zijn plek in de lijst wegens onvoorspelbare verschuivingen in de lijst
            verwijder_wezen(ID) #verwijderd zijn plek in de lijst
def volgende_dag():
    for ID in range(len(CLeeftijd)):
        CLeeftijd[ID] += 1
def voortplanten():
    for ID in range(len(CId)):
        if CVoedsel[ID]>1:
            maak_wezen(CPosities[ID][0], CPosities[ID][1],
                       CRadius[ID]*factor(), CZicht[ID]*factor(),
                       CSpeed[ID]*factor())#maakt kinderen
#dit script gebeurd elk frame
def logaritme():
    global CActiviteit
    CActiviteit = [False for ID in range(len(CId))]
    for ID in range(len(CId)):
        if CId[ID] != 'dood': #heeft nog energie
            brein(ID)
    return True in CActiviteit
#globale loop
def dag(aantalSnoep):
    global MaxEten
    haal_snoep_weg()
    leg_snoep_neer(aantalSnoep)
    c.itemconfig(VoedselNumID, text=aantalSnoep)
    NumEten.append(aantalSnoep)
    if MaxEten<aantalSnoep:
        MaxEten = aantalSnoep
    richt_naar_midden()
    geef_energie()
    magen_leeg()
    actief = True
    while actief:
        actief = logaritme()
        clean_up()
        if HuidigeModus == 'alle ids':
            scroll()
        window.update()
        sleep(0.01)
    nacht()
    volgende_dag()
    voortplanten()
    NumBevolking.append(len(CId))
    geef_energie()
    werk_data_bij()
    show_gegevens()
    window.update()
#aantal functies die uitgevoerd moeten worden voor de start
switch_pagina()
