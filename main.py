
incidente = []

def citeste_nota_valida(mesaj):
    """Cere o nota de la tastatura pana cand utilizatorul introduce ceva intre 1 si 10."""
   
    while True:
        verificare = input(mesaj)

        if verificare.isdigit():
            nota = int(verificare)
            if 1 <= nota <= 10:
                return nota
            else:
                print("Eroare: Introdu o nota intre 1 si 10 !")
        else:
            print("Eroare: Nu ai introdus un numar! Incearca din nou. ")
            
def adauga_incidente():
    """Colecteaza datele pentru un nou incident, calculeaza media si il salveaza in lista."""
    print("Adauga incident nou: ")
    tip = input("Tip de atatc: ")
    analist = input("Analist responsabi: "  )
    impact = citeste_nota_valida("Nota Impact (1-10): ")
    complexitate = citeste_nota_valida("Nota Complexitate (1-10): ")
    vulnerabilitate = citeste_nota_valida("Nota vulnerabilitae (1-10): ")
    media = (impact + complexitate + vulnerabilitate) / 3

    incident = {
        "tip": tip,
        "analist": analist,
        "impact": impact,
        "complexitate": complexitate,
        "vulnerabilitate": vulnerabilitate,
        "scor": round(media ,2)
    }

    incidente.append(incident)
    print("\n Incident adaugat cu success!")
    
def preia_tipul(incident):
    """Functie ajutatoare pentru a extrage tipul incidentului (folosita la sortare)."""
    return incident['tip']

def preia_scorul(incident):
    """Functie ajutatoare pentru a extrage scorul incidentului (folosita la sortare)."""
    return incident['scor']

def afisare_incidente():
    """Afiseaza pe ecran toate incidentele salvate pana in prezent."""
    if not incidente:
        print("\n --> Sistemul nu are incidente ")
        return
    
    print("\n --> Toate incidentele" )
    
    for inc in incidente:
        print(f"Atac: {inc['tip']} | Analist: {inc['analist']} | Risc: {inc['scor']}")




def modificare_incidente():
    """Cauta un incident dupa numele analistului si permite editarea detaliilor acestuia."""
    nume = input("Intodu numele analistului: ")

    for inc in incidente:
        if inc['analist'] == nume:
            inc['tip'] = input("Introdu noul tip de atac: ")
            inc['impact'] = citeste_nota_valida("Introduu noul tip de impact (1-10): ")
            inc['complexitate'] = citeste_nota_valida("Introdu noua nota de complexitate (1-10): ")
            inc['vulnerabilitate'] = citeste_nota_valida("Introdu noua nota de vulnerabilitate (1-10)")
            suma = inc['impact'] + inc['complexitate'] + inc['vulnerabilitate']
            inc['scor'] = round(suma / 3 , 2)
            print("Datele au fost actualizate!")
            return
    print("Eroare: Incidentul nu a fost gasit! ")

def stergere_incidente():
    """Cauta un incident dupa analist si il elimina definitiv din lista."""
    nume = input("Intodu numele analistului: ")
    for inc in incidente:
        if inc['analist'] == nume:
            incidente.remove(inc)
            print("Incident a fost sters cu success!")
            return
    print("Eroare: Incidentul nu a fost gasit!")

def cauta_incidente():
    """Cauta un incident anume folosind combinatia dintre numele analistului si tipul de atac."""
    analist_cautat = input("Introdu numele analistului cautat: ")
    tip_cautat = input("Introdu tipul de atac cautat: ")
    for inc in incidente:
        if inc['analist'] == analist_cautat and inc['tip'] == tip_cautat:
            print(f"\n Rezultat: {inc}")
            return
    print("Nu sa gasit nimic!")


def incidente_critice():
    """Filtreaza si afiseaza doar incidentele care au un scor de risc mai mare de 5."""
    print("\n --> Incidente critice Scor > 5 ")
    for inc in incidente:
        if inc['scor'] > 5:
            print(f"Critic: {inc['tip']} | Analist: {inc['analist']}")


def afisare_dupa_scor():
    """Afiseaza incidentele sortate descrescator, de la cel mai mare risc la cel mai mic."""
    sortare = sorted(incidente, key=preia_scorul, reverse=True)
    print("\n --> incidente in ordinea scorului de risc ")
    for inc in sortare:
        print(f"Scor: {inc['scor']} | Atac : {inc['tip']}")

def afisare_incidente_alfabetic():
    """Afiseaza incidentele sortate alfabetic dupa tipul atacului."""
    sortate = sorted(incidente, key=preia_tipul)

    if not sortate:
        print("\n Nu sunt incidente de sortat. ")
        return
    
    print("\n --> Lista Alfabetica de atacuri ")
    for inc in sortate:
        print(f"Tip incident: {inc['tip']} | Analist: {inc['analist']}")


while True :

    print("\n 1: Adauga | 2. Afisare | 3. Modificare | 4. Stergere | 5. Cauta | 6. Afisare dupa scor | 7. Incidente critice | 8. Afisare alfabetic | 0. Iesire")

    optiune = input("Alege una dintre optiunile urmatoare: ")
    
    if optiune == '0':
        print("Exit")
        break
    elif optiune == '1': 
        adauga_incidente()
    elif optiune == '2': 
        afisare_incidente()
    elif optiune == '3': 
        modificare_incidente()
    elif optiune == '4': 
        stergere_incidente()
    elif optiune == '5': 
        cauta_incidente()
    elif optiune == '6': 
        afisare_dupa_scor()
    elif optiune == '7': 
        incidente_critice()
    elif optiune == '8': 
        afisare_incidente_alfabetic()
    else:
        print("Optiune invalida! Te rog selecteaza una din optiuniile de mai sus!")
    