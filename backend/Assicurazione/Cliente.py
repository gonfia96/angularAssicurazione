import sqlite3

from Configurazione import Configurazione


def raccoltaDati(nome, cognome, dataDiNascita, cittaDiResidenza, professione, dipendenteOautonomo, statoCivile, sesso, etaMoglie, professioneMoglie, figli, quantiFigli, etaFigli, professioneFigli, nucleoFamiliare,personaDiReferimento,copertureAssicurative, indicareBisogni, consistenzaPatrimoniale, redditoAnnuo, impegniFinanziari ):
    db = Configurazione.config('Database')
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO CLIENTE(Nome, Cognome, Data di Nascita, Città di residenza, 
    Professione,Dipendente/Lavoratore autonomo, Stato civile, Sesso, Età moglie, Professione moglie, Figli, 
    Quanti figli, Professioni figli, Nucleo familiare è composto da quante persone, Persona di riferimento del nucleo familiare, Ho già altre coperture assicurative esclusa rc auto,
    Vorrei indicare i miei bisogni assicurativi/un aiuto a stabilire le mie priorità assicurative, La mia consistenza patrimoniale è di, I mio reddito annuo è di, Ho impegni finanziari annuali) 
    VALUES(?,?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """, (
        nome, cognome, dataDiNascita, cittaDiResidenza, professione, dipendenteOautonomo, statoCivile, sesso, etaMoglie, professioneMoglie,
        figli, etaFigli, quantiFigli, professioneFigli, nucleoFamiliare,
        personaDiReferimento, copertureAssicurative, indicareBisogni, consistenzaPatrimoniale, redditoAnnuo,
        impegniFinanziari,))
    id = cursor.lastrowid
    print(id)
    conn.commit()
    conn.close()

def elaboration(nome, cognome, dataDiNascita):
    print(nome)
    print(cognome)
    print(dataDiNascita)


if __name__ == '__main__':
    nome = input('Inserisci il tuo nome: ')
    cognome = input('Inserisci il tuo cognome: ')
    dataDiNascita = input('Inserisci data di nascita: ')
    cittaDiResidenza = input('Inserisci la tua città di residenza: ')
    professione = input('Inserisci la tua professione: ')
    dipendenteOautonomo = input('Inserisci se dipendete o autonomo: ')
    statoCivile = input('Inserisci lo stato civile: ')
    sesso = input('Inserisci il tuo sesso: ')
    if (sesso == 'M' and statoCivile == 'Sposato'):
        etaMoglie = input('Inserisci età')
        professioneMoglie = input('Inserisci la professione moglie: ')
    figli = input('Inserisci se hai figli: ')
    if (figli == 'si'):
        quantiFigli = input('Inserisci quanti figli hai: ')
        etaFigli = input('Inserisci età')
        professioneFigli = input('Inserisci la professione figli: ')
    nucleoFamiliare = input('Inserisci il nucleo familiare: ')
    personaDiReferimento = input('Inserisci se sei persona di referimento: ')
    copertureAssicurative = input('Inserisci se si hanno altre coperture assicurative: ')
    indicareBisogni = input('Inserisci il bisogno: ')
    consistenzaPatrimoniale = input('Inserisci la tua consistenza patrimoniale: ')
    redditoAnnuo = input('Inserisci il tuo reddito annule: ')
    impegniFinanziari = input('Inserisci i tuoi impegni finanziari: ')
    raccoltaDati(nome, cognome, dataDiNascita, cittaDiResidenza, professione, dipendenteOautonomo, statoCivile, sesso, etaMoglie, professioneMoglie, figli, quantiFigli, etaFigli, professioneFigli, nucleoFamiliare,personaDiReferimento,copertureAssicurative, indicareBisogni, consistenzaPatrimoniale, redditoAnnuo, impegniFinanziari)


