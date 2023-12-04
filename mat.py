import random
def number_to_word(number):
    words = {
        1: 'viens',
        2: 'divi',
        3: 'trīs',
        4: 'četri',
        5: 'pieci',
        6: 'seši',
        7: 'septiņi',
        8: 'astoņi',
        9: 'deviņi',
        10: 'desmit'
    }

    return words.get(number, str(number))
def convert_to_roman(n):
    roman_numerals = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 11: 'XI', 12: 'XII'
    }
    return roman_numerals.get(n, '')
def generet_uzdevumu(tema, skaits, klase, ar_atlikumu=True):
    uzdevumi = []
    if klase == 1:
        if tema == "saskaitisana":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                rezultats = a + b
                uzdevums = f"{a} + {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "atnemsana":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, a)
                rezultats = a - b
                uzdevums = f"{a} - {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "salidzināšana":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                salidz = random.choice(['<', '>', '='])
                uzdevums = f"{a} {salidz} {b} ?"
                if salidz == '<':
                    rezultats = a < b
                elif salidz == '>':
                    rezultats = a > b
                else:
                    rezultats = a = b
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "nezinamais":
            for _ in range(skaits):
                nezinamais = random.randint(1, 10)
                saskaitamais = random.randint(1, 10)
                rezultats = nezinamais + saskaitamais
                uzdevums = f" ? + {saskaitamais} = {rezultats}"
                uzdevumi.append((uzdevums, nezinamais))
        elif tema == "lielumu_meri":
            for _ in range(skaits):
                if random.choice([True, False]):
                    # Laika mēri - stundas un minūtes salīdzināšana
                    stundas = random.randint(0, 12)
                    minutes = random.randint(0, 59)
                    uzdevums = f"{stundas}:{minutes} > ?"
                    rezultats = stundas * 60 + minutes
                else:
                    # Attāluma lielumi
                    attalums = random.uniform(1, 1000)
                    mervienibas = ['mm', 'cm', 'dm', 'm', 'km']
                    uzdevums = f"Pārvērtiet {attalums} {random.choice(mervienibas)} uz metri (m)"
                    
                    # Pārvēršana uz metri (m)
                    if uzdevums.find('mm') != -1:
                        rezultats = attalums / 1000
                    elif uzdevums.find('cm') != -1:
                        rezultats = attalums / 100
                    elif uzdevums.find('dm') != -1:
                        rezultats = attalums / 10
                    elif uzdevums.find('km') != -1:
                        rezultats = attalums * 1000
                    else:
                        rezultats = attalums

                uzdevumi.append((uzdevums, rezultats))
        elif tema == "teksta_uzdevumi":
            for _ in range(skaits):
                uzdevums = ""
                rezultats = 0

                # Uzdevumu izvēle
                uzdevuma_veids = random.randint(1, 15)
                
                if uzdevuma_veids == 1:
                    # KAD MIGĀ IELĪDA LĀCĒNI, TAD KOPĀ BIJA  LĀCĒNI.
                    # CIK LĀCĒNU BIJA MIGĀ IEPRIEKŠ?
                    ielidosie_lācēni = random.randint(1, 5)
                    kopējie_lācēni = random.randint(ielidosie_lācēni, 2 * ielidosie_lācēni)
                    uzdevums = f"Kad Migā ielīda {ielidosie_lācēni} lācēni, tad kopā bija {kopējie_lācēni} lācēni. Cik lācēnu bija Migā iepriekš?"
                    rezultats = kopējie_lācēni - ielidosie_lācēni
                
                elif uzdevuma_veids == 2:
                    # PAGALMĀ IR  ZĒNI AR BRŪNIEM MATIEM UN  ZĒNI AR MELNIEM MATIEM.
                    # CIK ZĒNU PAVISAM IR PAGALMĀ?
                    brunie_mati = random.randint(1, 3)
                    melnie_mati = random.randint(3, 7)
                    uzdevums = f"Pagalmā ir {brunie_mati} zēni ar brūniem matiem un {melnie_mati} zēni ar melniem matiem. Cik zēnu pavisam ir pagalmā?"
                    rezultats = brunie_mati + melnie_mati

                elif uzdevuma_veids == 3:
                    # PAGALMĀ BIJA  MEITENES,  MEITENES AIZGĀJA.
                    # CIK MEITEŅU PALIKA PAGALMĀ?
                    bija_meitenes = random.randint(8, 15)
                    aizgajusas_meitenes = random.randint(1, 5)
                    uzdevums = f"Pagalmā bija {bija_meitenes} meitenes, 5 meitenes aizgāja. Cik meiteņu palika pagalmā?"
                    rezultats = bija_meitenes - aizgajusas_meitenes

                elif uzdevuma_veids == 4:
                    # PAGALMĀ IR PAVISAM  BĒRNI. NO VIŅIEM  IR ZĒNI.
                    # CIK IR MEITEŅU?
                    zēni_pagalmā = random.randint(1, 5)
                    visi_bērni = random.randint(6, 12)
                    uzdevums = f"Pagalmā ir pavisam {visi_bērni} bērni. No viņiem {zēni_pagalmā} ir zēni. Cik ir meitenes pagalmā?"
                    rezultats = visi_bērni - zēni_pagalmā

                elif uzdevuma_veids == 5:
                    # KAD NO KLASES IZGĀJA  SKOLĒNI, TUR PALIKA  SKOLĒNI.
                    # CIK SKOLĒNU BIJA KLASĒ SĀKUMĀ?
                    izgajusie_skolēni = random.randint(1, 10)
                    palikusie_skolēni = random.randint(1, 10)
                    uzdevums = f"Kad no klases izgāja {izgajusie_skolēni} skolēni, tur palika {palikusie_skolēni} skolēni. Cik skolēnu bija klasē sākumā?"
                    rezultats = izgajusie_skolēni + palikusie_skolēni
                elif uzdevuma_veids == 6:
                    # STROPĀ BIJA  BITES. KAD DAŽAS IELIDOJA, TAD STROPĀ BIJA  BITES.
                    # CIK BITES IELIDOJA?
                    ielidosas_bites = random.randint(1, 5)
                    sākotnējās_bites = random.randint(ielidosas_bites, 2 * ielidosas_bites)
                    uzdevums = f"Stropā bija {sākotnējās_bites} bites. Kad dažas ielidoja, tad stropā bija {sākotnējās_bites + ielidosas_bites} bites. Cik bites ielidoja?"
                    rezultats = ielidosas_bites

                elif uzdevuma_veids == 7:
                    # IERAKSTI TRŪKSTOŠOS SKAITĻUS NO DOTĀS VIENĀDĪBAS!
                    # 10 - 3 = 7 ↗↘
                    # 10 IR PAR 7 VAIRĀK NEKĀ ...
                    # 3 IR PAR ... MAZĀK NEKĀ ...
                    skaitlis1 = random.randint(5, 10)
                    skaitlis2 = random.randint(1, 5)
                    uzdevums = f"{skaitlis1} - {skaitlis2} = {skaitlis1 - skaitlis2} ↗↘\n{skaitlis1} ir par {skaitlis1 - skaitlis2} vairāk nekā ... \n{skaitlis2} ir par {skaitlis1 - skaitlis2} mazāk nekā ..."
                    rezultats = skaitlis2

                elif uzdevuma_veids == 8:
                    # LITAI BIJA  PILDSPALVAS, BET ZĪMUĻU PAR  VAIRĀK.
                    # CIK LITAI BIJA ZĪMUĻU?
                    pildspalvas = random.randint(3, 7)
                    skaitli = random.randint(1, 5)
                    zīmuļi = pildspalvas + skaitli
                    uzdevums = f"Litai bija {pildspalvas} pildspalvas, bet zīmuļu par {skaitli} vairāk. Cik litai bija zīmuļu?"
                    rezultats = zīmuļi

                elif uzdevuma_veids == 9:
                    # DĀRZĀ BIJA  NARCISES, BET TULPES PAR  MAZĀK.
                    # CIK BIJA TULPJU?
                    narcises = random.randint(5, 10)
                    mazak = random.randint(1, 5)
                    tulpes = narcises - mazak
                    uzdevums = f"Dārzā bija {narcises} narcises, bet tulpes par {mazak} mazāk. Cik bija tulpju?"
                    rezultats = tulpes

                elif uzdevuma_veids == 10:
                    # PAGALMĀ IR  ZĒNI JEB PAR  MAZĀK NEKĀ MEITEŅU.
                    # CIK MEITEŅU PAGALMĀ?
                    zēni = random.randint(1, 5)
                    mazak = random.randint(1, 10)
                    meitenes = zēni + mazak
                    uzdevums = f"Pagalmā ir {zēni} zēni jeb par {mazak} mazāk nekā meiteņu. Cik meiteņu pagalmā?"
                    rezultats = meitenes

                elif uzdevuma_veids == 11:
                    # PĻAVĀ IR  ZAĶI UN  STIRNAS.
                    # PAR CIK STIRNU MAZĀK NEKĀ ZAĶU?
                    zaķi = random.randint(6, 10)
                    stirnas1 = random.randint(1, 6)
                    stirnas = zaķi - stirnas1
                    uzdevums = f"Pļavā ir {zaķi} zaķi un {stirnas1} stirnas. Par cik stirnu mazāk nekā zaķu?"
                    rezultats = zaķi - stirnas

                elif uzdevuma_veids == 12:
                    # IVARIŅAM IR  KONFEKTES. JA VIŅŠ  KONFEKTES APĒSTU, TAD VIŅAM BŪTU TIKPAT DAUDZ, CIK ANNIŅAI. CIK KONFEKTES IR ANNIŅAI?
                    # ANNIŅAI IR ... KONFEKTES
                    ivariņa_konfektes = random.randint(6, 10)
                    anninas_konfektes = ivariņa_konfektes - 3
                    uzdevums = f"Ivariņam ir {ivariņa_konfektes} konfektes. Ja viņš 3 konfektes apēstu, tad viņam būtu tikpat daudz, cik anniņai. Cik konfektes ir anniņai?"
                    rezultats = anninas_konfektes

                elif uzdevuma_veids == 13:
                    # AKVĀRIJĀ IR  ZIVTIŅAS. CIK ZIVTIŅU JĀIELAIŽ AKVĀRIJĀ, LAI TUR BŪTU  ZIVIS? AKVĀRIJĀ JĀIELAIŽ ... ZIVTIŅAS
                    zivtinas_akvarija = random.randint(1, 6)
                    jāielaiž_zivtinas = zivis - zivtinas_akvarija
                    zivis = random.randint(4,10)
                    uzdevums = f"Akvārijā ir {zivtinas_akvarija} zivtiņas. Cik zivtiņu jāielaiž akvārijā, lai tur būtu {zivis} zivis?"
                    rezultats = jāielaiž_zivtinas

                elif uzdevuma_veids == 14:
                    # JA EGLĪTĒ IEKĀRTU VĒL  MANTIŅAS, TAD TUR BŪTU  MANTIŅAS. CIK MANTIŅU IR EGLĪTĒ? EGLĪTĒ IR ... MANTIŅAS
                    mantiņas_eglītē = random.randint(1, 5)
                    mantinas = random.randint(1,10)
                    piekārtotās_mantiņas = mantinas - mantiņas_eglītē
                    uzdevums = f"Ja eglītē iekārtu vēl {mantiņas_eglītē} mantiņas, tad tur būtu {mantinas} mantiņas. Cik mantiņu ir eglītē?"
                    rezultats = piekārtotās_mantiņas

                elif uzdevuma_veids == 15:
                    # KAD ANNA UZZĪMĒS VĒL  KARTĪTES, TAD VIŅA BŪS SAGATAVOJUSI  KARTĪTES.
                    # CIK KARTĪŠU ANNA JAU IR UZZĪMĒJUSI?
                    annas_kartītes = random.randint(1, 6)
                    kartinas = random.randint(5,10)
                    sagatavotās_kartītes = annas_kartītes + kartinas
                    uzdevums = f"Kad Anna uzzīmēs vēl {annas_kartītes} kartītes, tad viņa būs sagatavojusi {kartinas} kartītes. Cik kartīšu Anna jau ir uzzīmējusi?"
                    rezultats = sagatavotās_kartītes


                uzdevumi.append((uzdevums, rezultats))
        return uzdevumi
    elif klase ==2:
        if tema == "Saskaitīšana līdz 20":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                rezultats = a + b + c
                uzdevums = f"Cik ir {a} plus {b} un plus {c}?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "Atņemšana līdz 20":
            for _ in range(skaits):
                a = random.randint(9, 20)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                d = a + b + c
                rezultats = a 
                uzdevums = f"Cik ir {d} mīnus {b} un mīnus {c} viens?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == " random darbība":
            for _ in range(skaits):
                a = random.randint(1, 20)
                b = random.randint(1, 10)
                # Randomly select addition or subtraction operation
                operation = random.choice(["pieskaita", "atņem", "reiz", "dalit"])
                if operation == "pieskaita":
                    rezultats = a + b
                    uzdevums = f"Cik ir {number_to_word(a)} plus {number_to_word(b)}?"
                elif operation == "atņem":
                    rezultats = a - b
                    uzdevums = f"Cik ir {number_to_word(a)} mīnus {number_to_word(b)}?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "teksta uzdevums":
            for _ in range(skaits):
                uzdevums = ""
                rezultats = 0
                # Uzdevumu izvēle
                uzdevuma_veids = random.randint(1, 2)
                c = random.randint(20, 30)
                a = random.randint(1, 5)
                b = random.randint(1,4)
                if uzdevuma_veids == 1:
                    izlietoja = a * b
                    palika = c - izlietoja
                    uzdevums = f"Maisā bija {c} kg miltu. Saimniece katru dienu izlietoja {a} kg. Cik kilogramu miltu palika maisā pēc {b} dienām?"
                    rezultats = palika
               
                elif uzdevuma_veids ==2:    
                    uzdevums = f"Katrā saldējuma karotē ir {a} saldējuma bumbiņas. Cik bumbinas kopā ir {b} karotēs, ja no katras karotes atņema vienu bumbiņu?"
                    rezultats = a*b-b
                elif uzdevuma_veids ==3:    
                    uzdevums = f"Biļete uz filmu maksā {a} eiro, un biļete uz izrādi maksā {b} eiro. Cik kopā jums būs jāsamaksā, ja tu un tava draudzene dosies gan uz filmu, gan uz izrādi?"
                    rezultats = a + b + a + b
                elif uzdevuma_veids ==4:    
                    uzdevums = f" Zoo ir 4 dažādi dzīvnieki: lapsa, tīģeris, zirgs un zilonis. Cik kājām kopā ir šie dzīvnieki, ja katram ir viens bērņiņš?"
                    rezultats = 4*4*2
                elif uzdevuma_veids ==5:    
                    uzdevums = f"  tēv bija {c} ziedus, tu iegādājies {a} ziedus. Katrs zieds ir ievietots vāzēs. Cik vāzēs vajag, ja viena vāzē var ievietot tikai {b} ziedus?"
                    rezultats = (c+a)/b
                elif uzdevuma_veids ==6:    
                    uzdevums = f"Dārzeņu Iepirkšanās. Aprēķini kopējo summu. Dārzenis 1: {a} eiro, Dārzenis 2: {b} eiro, Dārzenis 3: {c} eiro, Dārzenis 4: {a} eiro, Dārzenis 5: {b} eiro. Kopējā summa: {a} eiro"
                    rezultats = a + b + c + a + b + a
                elif uzdevuma_veids ==7:    
                    uzdevums = f"Rīta temperatūra ir bijusi -{a} grādi, bet pēcpusdienā tā paaugstinājusies par {b} grādiem. Kāda ir pēcpusdienas temperatūra?"
                    rezultats = b-a
                elif uzdevuma_veids ==8:    
                    uzdevums = f"Tavā grāmatu plauktā ir {a} grāmatas rindā, un katrā rindā ir {c} grāmatas. Cik vēl grāmatas tu vari nopirkt, ja katra rindā var stavēt {c+b}?"
                    rezultats =a*(c+b)-(a*c)
        elif tema == "reizinajums":
            for _ in range(skaits):
                a = random.randint(1, 5)
                b = random.randint(1, 5)
                rezultats = a * b
                uzdevums = f"{a} * {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "dalijums":
            for _ in range(skaits):
                b = random.randint(1, 5)
                rezultats = random.randint(1, 5)
                a = b * rezultats
                uzdevums = f"{a} / {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        return uzdevumi
    elif klase ==3:
        if tema == "saskaitisana":
            for _ in range(skaits):
                a = random.randint(1, 50)
                b = random.randint(1, 50)
                rezultats = a + b
                uzdevums = f"{a} + {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "atnemsana":
            for _ in range(skaits):
                a = random.randint(1, 100)
                b = random.randint(1, a)
                rezultats = a - b
                uzdevums = f"{a} - {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "reizinajums lidz 100":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                while a * b > 100:  # Ensure the product is <= 100
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                rezultats = a * b
                uzdevums = f"{a} * {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "dalijums lidz 100":
            for _ in range(skaits):
                b = random.randint(1, 5)
                rezultats = random.randint(1, 5)
                a = b * rezultats
                uzdevums = f"{a} / {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "saskaitisana_rakstos":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                rezultats = a + b
                uzdevums = f"{number_to_word(a)} + {number_to_word(b)} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "atnemsana_rakstos":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, a)
                rezultats = a - b
                uzdevums = f"{number_to_word(a)} - {number_to_word(b)} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "reizinajums":
            for _ in range(skaits):
                a = random.randint(10, 99)  # Generate a two-digit number
                b = random.randint(1, 10)
                rezultats = a * b
                uzdevums = f"{a} * {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "dalijums":
            for _ in range(skaits):
                random.choice([True, False])
                b = random.randint(1, 10)
                atlikumss = random.randint(1, b - 1)
                if ar_atlikumu:
                    a = random.randint(1, 10) * b + atlikumss # Ensure a is a multiple of b for remainder
                else:
                    a = random.randint(1, 10) * b   # Random number without remainder

                rezultats = a // b  # Integer division for problems without remainder
                atlikums = a % b  # Remainder for problems with remainder

                if ar_atlikumu:
                    uzdevums = f"{a} / {b} = ? (atlikums: {atlikums})"
                else:
                    uzdevums = f"{a} / {b} = ?"

                uzdevumi.append((uzdevums, rezultats))
        elif tema == "Trīsciparu skaitļi":
            for _ in range(skaits):
                a = random.randint(100, 999)  # Generate a three-digit number
                uzdevums = f"{number_to_word(a)} = ?"
                uzdevumi.append((uzdevums, a))
        elif tema == "Trīsciparu skaitļa reizināšana ar viencipara skaitli rakstos":
            for _ in range(skaits):
                a = random.randint(100, 999)  # Generate a three-digit number
                b = random.randint(1, 9)  # Generate a single-digit number
                rezultats = a * b
                uzdevums = f"{a} * {b} = ?"
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "Trīsciparu skaitļa dalīšana ar viencipara skaitli rakstos":
            for _ in range(skaits):
                a = random.randint(100, 999)  # Generate a three-digit number
                b = random.randint(1, 9)  # Generate a single-digit number
                rezultats = a // b  # Integer division
                atlikums = a % b  # Remainder
                uzdevums = f"{a} / {b} = ? (atlikums: {atlikums})"
                uzdevumi.append((uzdevums, rezultats))
        return uzdevumi
    elif klase ==4:
        if tema == "Skaitļi līdz 100":
            for _ in range(skaits):
                skaitlis = random.randint(1, 100)
                a = skaitlis + 1
                b = a + 1
                c = b + 1
                uzdevums = f"uzraksti trīs nakamos skaitļus skaitlim: {skaitlis}"
                uzdevumi.append((a, b, c))
        elif tema == "Saskaitīšana un atņemšana":
            for _ in range(skaits):
                a = random.randint(1, 50)
                b = random.randint(1, 50)
                uzdevums = f"Cik ir {a} + {b} un cik ir {a} - {b}?"
                rezultats = (a + b, a - b)
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "Reizināšana un dalīšana":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                uzdevums = f"Cik ir {a} * {b} un cik ir {a * b} / {c}?"
                uzdevumi.append((a*b,(a*b)/c))
        elif tema == "salīdzināšana":
            for _ in range(skaits):
                a = random.randint(1, 100)
                b = random.randint(1, 100)
                uzdevums = f"Salīdzini skaitļus {a} un {b}. Kurš skaitlis lielāks?"
                rezultats = max(a, b)
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "saskaitisana paros":
            for _ in range(skaits):
                a = random.randint(10, 20)
                b = a + d
                c = a - d
                d = random.randint(1, 10)
                # Saskaitīšanas īpašības: a + b + c = (a + b) + c = a + (b + c)
                uzdevums = f"Izrēķiniet izteiksmi: {a} + {b} + {c}"
                rezultats = a + b + c
                uzdevumi.append((uzdevums, rezultats))
        elif tema == "nezinamais":
            for _ in range(skaits):
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                rezultats = random.choice([a + b, a - b, a * b])
                zimes = random.choice(['+', '-', '*'])
                if zimes == "+":
                    rezultats = a + b
                elif zimes == "-":
                    rezultats = a - b
                elif zimes == "*":
                    rezultats = a * b
                uzdevums = f"Izrēķiniet izteiksmi: x {zimes} {a} = {rezultats}"
                uzdevumi.append((uzdevums, b))
        elif tema =="lielumi":
            for _ in range(skaits):
                lielums = random.randint(1, 1000)
                mervieniba1 = random.choice(["cm", "m", "km"])
                if mervieniba1 =="cm":
                    mervieniba = random.choice(["cm", "m", "km"])
                    uzdevums = f"Izmēri {lielums} {mervieniba} iegūstot rezultātu centimetros (cm):"
                    rezultats = lielums * 100 if mervieniba == "m" else (lielums * 100000 if mervieniba == "km" else lielums)
                    uzdevumi.append((uzdevums, rezultats))
                if mervieniba1 =="m":
                    mervieniba = random.choice(["cm", "m", "km"])
                    uzdevums = f"Izmēri {lielums} {mervieniba} iegūstot rezultātu centimetros (m):"
                    rezultats = lielums / 100 if mervieniba == "cm" else (lielums * 100 if mervieniba == "km" else lielums)
                    uzdevumi.append((uzdevums, rezultats))
                if mervieniba1 =="km":
                    mervieniba = random.choice(["cm", "m", "km"])
                    uzdevums = f"Izmēri {lielums} {mervieniba} iegūstot rezultātu centimetros (km):"
                    rezultats = lielums / 1000 if mervieniba == "m" else (lielums / 100000 if mervieniba == "cm" else lielums)
                    uzdevumi.append((uzdevums, rezultats))
        elif tema =="laiki":
            klab = random.randint(1,9)
            if klab == 1:
                for _ in range(skaits):
                    diena = random.randint(1, 100)
                    uzdevums = f"Cik stundas ir {diena} dienas garumā?"
                    rezultats = diena * 24
                    uzdevumi.append((uzdevums, rezultats))
            if klab == 2:
                for _ in range(skaits):
                    stunda_sakums = random.randint(0, 23)
                    min_sakums = random.randint(0, 59)
                    stunda_beigas = random.randint(stunda_sakums, 23)
                    min_beigas = random.randint(min_sakums, 59)
                    
                    uzdevums = f"Cik ir laika intervāls no {stunda_sakums:02d}:{min_sakums:02d} līdz {stunda_beigas:02d}:{min_beigas:02d}?(atbildi raksti minutēs)"
                    rezultats = (stunda_beigas * 60 + min_beigas) - (stunda_sakums * 60 + min_sakums)
                    uzdevumi.append((uzdevums, rezultats))
            if klab == 3:
                for _ in range(skaits):
                    romiesu_cipars = random.randint(1, 12)
                    uzdevums = f"Pārvērtiet skaitli {convert_to_roman(romiesu_cipars)} arabu ciparos."
                    rezultats = romiesu_cipars
                    uzdevumi.append((uzdevums, rezultats))
            if klab == 4:
                for _ in range(skaits):
                    stunda = random.randint(0, 23)
                    minutes = random.randint(0, 59)
                    uzdevums = f"Ieraksti laiku: {stunda:02d}:{minutes:02d}. Cik ir minūtes kopš dienas sākuma?"
                    rezultats = stunda * 60 + minutes
                    uzdevumi.append((uzdevums, rezultats))
            if klab == 5:
                for _ in range(skaits):
                    stunda = random.randint(0, 23)
                    minutes = random.randint(0, 59)
                    sekundes = random.randint(0, 59)
                    uzdevums = f"Ieraksti laiku: {stunda:02d}:{minutes:02d}:{sekundes:02d}. Cik ir sekundes kopš dienas sākuma?"
                    rezultats = stunda * 3600 + minutes * 60 + sekundes
                    uzdevumi.append((uzdevums, rezultats))
            if klab == 6:
                for _ in range(skaits):
                    nedela = random.randint(1, 52)
                    diena_nedela = random.randint(1, 7)
                    uzdevums = f"Cik dienas ir pagājušas, ja ir {nedela} nedēļas un {diena_nedela} dienas?"
                    rezultats = nedela * 7 + diena_nedela
                    uzdevumi.append((uzdevums, rezultats))
            if klab == 7:
                for _ in range(skaits):
                    gads = random.randint(1, 100)
                    menesis = random.randint(1, 12)
                    uzdevums = f"Cik mēneši ir pagājuši, ja ir {gads} gadi un {menesis} mēneši?"
                    rezultats = gads * 12 + menesis
                    uzdevumi.append((uzdevums, rezultats))
            if klab == 8:
                for _ in range(skaits):
                    nedelas = random.randint(1, 10)
                    dienas = random.randint(1, 6)
                    stundas = random.randint(1, 23)
                    uzdevums = f"Saskaiti laika mērus: {nedelas} nedēļas, {dienas} dienas un {stundas} stundas.(atbildi raksti stundas)"
                    rezultats = nedelas * 7 * 24 + dienas * 24 + stundas
                    uzdevumi.append((uzdevums, rezultats))
            if klab == 9:
                for _ in range(skaits):
                    gadi = random.randint(1, 10)
                    uzdevums = f"Cik stundas ir {gadi} gados (1 gads = 365 dienas)?"
                    rezultats = gadi * 365 * 24
                    uzdevumi.append((uzdevums, rezultats))
                    return uzdevumi
        elif tema == "daļas salidzināšana":
                
                dala1_skaititajs = random.randint(1,10)
                dala1_saucetajs = random.randint(1,10)
                dala2_skaititajs = random.randint(1,10)
                dala2_saucetajs = random.randint(1,10)
                uzdevums = f" izvelies pareizo zīmi skaititajs-{dala1_skaititajs} saucetajs-{dala1_saucetajs} (>,<,=) skaititajs-{dala2_skaititajs} saucetajs-{dala2_saucetajs}"
                if dala1_skaititajs * dala2_saucetajs > dala2_skaititajs * dala1_saucetajs:
                    rezultats = ">"
                    return f"{dala1_skaititajs}/{dala1_saucetajs} ir lielāka par {dala2_skaititajs}/{dala2_saucetajs}"
                    
                elif dala1_skaititajs * dala2_saucetajs < dala2_skaititajs * dala1_saucetajs:
                    rezultats = "<"
                    return f"{dala2_skaititajs}/{dala2_saucetajs} ir lielāka par {dala1_skaititajs}/{dala1_saucetajs}"
                else:
                    rezultats = "="
                    return f"{dala1_skaititajs}/{dala1_saucetajs} ir vienāda ar {dala2_skaititajs}/{dala2_saucetajs}"
        elif tema == "taisnstura laukums":
            lielums = random.randint(1, 100)
            skaits1 = random.randint(1, 100)
            mervieniba1 = random.choice(["cm", "m", "km"])
            if mervieniba1 =="cm":
                    mervieniba = random.choice(["cm", "m", "km"])
                    uzdevums = f"Aprēķini taisnstūra laukumu, ja tā garums ir {lielums} {mervieniba1}, un platums ir {skaits1} {mervieniba}(parveido {mervieniba}) "
                    rezultats = lielums*(skaits1 * 100 if mervieniba == "m" else (skaits1 * 100000 if mervieniba == "km" else skaits1))
                    uzdevumi.append((uzdevums, rezultats))
            if mervieniba1 =="m":
                    mervieniba = random.choice(["cm", "m", "km"])
                    uzdevums = f"Aprēķini taisnstūra laukumu, ja tā garums ir {lielums} {mervieniba1}, un platums ir {skaits1} {mervieniba} (parveido {mervieniba})"
                    rezultats = skaits1*(lielums * 100 if mervieniba == "cm" else (lielums * 100 if mervieniba == "km" else lielums))
                    uzdevumi.append((uzdevums, rezultats))
            if mervieniba1 =="km":
                    mervieniba = random.choice(["cm", "m", "km"])
                    uzdevums = f"Aprēķini taisnstūra laukumu, ja tā garums ir {lielums} {mervieniba1}, un platums ir {skaits1} {mervieniba}(parveido {mervieniba}))"
                    rezultats = skaits1*(lielums * 1000 if mervieniba == "m" else (lielums * 100000 if mervieniba == "cm" else lielums ))
                    uzdevumi.append((uzdevums, rezultats))
            return uzdevumi
        elif tema == "teksta  uzdevumi":
            for _ in range(skaits):
                uzdevums = ""
                rezultats = 0
                # Uzdevumu izvēle
                variks = random.randint(1, 4)
                if variks == 1:
                    a = random.randint(200, 700)
                    b = random.randint(100, 200)
                    uzdevums = f"Parkā ir {a} liepas, bet ozolu ir par {b} mazāk. Cik reizes liepas ir vairāk nekā ozolu?"
                    rezultats = a/(a-b)
                elif variks == 2:
                    a = random.randint(1, 1000)
                    b = random.randint(100, 200)
                    uzdevums = f"Ja ir {a} ķirši, bet banānu ir par {b} mazāk nekā ķiršu, cik reizes ķirši ir vairāk nekā banāni?"
                    rezultats = a/(a-b)
                elif variks == 3:
                    a = random.randint(1, 1000)
                    b = random.randint(100, 200)
                    uzdevums = f"Cik reizes {a} kļavu koki ir lielāki par {b} ozolu koku skaitu?"
                    rezultats = a/b
                elif variks == 4:
                    a = random.randint(1, 1000)
                    b = random.randint(100, 200)
                    uzdevums = f"Ja ir {a} sarkano piparu, bet zaļo piparu ir par {b} mazāk nekā sarkanu, cik reizes sarkanie pipari ir vairāk nekā zaļie?"
                    rezultats = a/(a-b)

def main():
    klase = int(input("izvēlies klasi 1, 2, 3, 4:"))
    if klase == 1:
        tema = input("Izvēlieties tēmu (saskaitisana, atnemsana, salidzināšana, nezinamais, lielumu_meri, teksta_uzdevumi): ")
    elif klase == 2:
        tema = input("Izvēlieties tēmu (Saskaitīšana līdz 20, Atņemšana līdz 20, random darbība, teksta uzdevums, reizinajums, dalijums,)")
    elif klase == 3:
        tema = input("Izvēlieties tēmu (saskaitisana, atnemsana, reizinajums lidz 100, dalijums lidz 100, saskaitisana_rakstos, atnemsana_rakstos, reizinajums, dalijums, Trīsciparu skaitļi, Trīsciparu skaitļa reizināšana ar viencipara skaitli rakstos, Trīsciparu skaitļa dalīšana ar viencipara skaitli rakstos)") 
    elif klase == 4:
        tema = input("Izvēlieties tēmu (Skaitļi līdz 100, Saskaitīšana un atņemšana, Reizināšana un dalīšana, salīdzināšana, saskaitisana paros, nezinamais, lielumi, laiki, daļas salidzināšana, taisnstura laukums )")    
    skaits = int(input("Ievadiet uzdevumu skaitu: "))

    uzdevumi = generet_uzdevumu(tema, skaits, klase)

    atzime = 0
    for uzdevums, rezultats in uzdevumi:
        print(f"Uzdevums: {uzdevums}")
        ievade = int(input("Ievadiet rezultātu: "))
        if ievade == rezultats:
            print("Pareizi!")
            atzime += 1
        else:
            print(f"Nepareizi! Pareizais rezultāts ir {rezultats}")

    vid_atskaite = atzime / skaits * 10
    print(f"Jūs dabujat {vid_atskaite:.2f} konfektes no 10")
if __name__ == "__main__":
    main()
