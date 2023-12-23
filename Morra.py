import random

#Insieme dei tre simboli del gioco della morra
smb = ['carta', 'sasso', 'forbice']


def mostra(Simboli):
    """
    Funzione che sceglie un simbolo a caso in una lista di simboli

    Parametri:
        Simboli -- Lista dei simboli tra cui scegliere
        dim_lista -- Dimensione della lista di simboli

    Ritorna: Simbolo scelto in forma di stringa

    """

    rnd = random.randint(0,len(Simboli)-1)
    return Simboli[rnd]


def scelta_avversario(avversario):
    """
    Funzione che descrive il simbolo della morra che l'avversario ha scelto

    Parametri
        Avversario -- Simbolo scelto dall'avversario

    Ritorna
        Una stringa che spiega cosa ha scelto l'avversario
    """

    return 'L\'avversario ha scelto ' + avversario


def guida():
    """
        Funzione che stampa in output il manuale del gioco

        Ritorna
            None
    """
    print('Digita c per scegliere Carta, s per scegliere Sasso,'
          ' f per scegliere forbice, a per la guida, u per uscire dal gioco'
          'e successivamente premi il tasto Invio')


def controlla_input(tasto, carattere):
    """
        Funzione che controlla che la stringa passata in input sia uguale ad un determinato carattere

        Parametri:
            tasto -- Stringa in input
            carattere -- Carattere a cui confrontare la stringa
    """
    return tasto == carattere


def condizione_fine_gioco(v, s, numero):
    """
        Funzione che verifica che il numero di vittorie o di sconfitte sia uguale ad un numero predeterminato
        ai fini della fine del gioco

        Parametri:
            v -- Numero di vittorie dato in input alla funzione
            s -- Numero di sconfitte dato in input alla funzione
            numero -- Numero predeterminato di vittorie o sconfitte in input alla funzione

        Ritorna
            Valore booleano che indica se il numero di vittorie oppure il numero di sconfitte è uguale al numero
            predeterminato dato in input alla funzione
    """
    return (v >= numero) or (s >= numero)


def vittoria():
    """
        Funzione che restituisce la stringa predefinita in output in caso di vittoria

        Ritorna:
            Stringa predefinita in caso di vittoria
    """
    return 'quindi hai vinto!'


def sconfitta():
    """
        Funzione che restituisce la stringa predefinita in output in caso di sconfitta

        Ritorna:
            Stringa predefinita in caso di sconfitta
    """
    return 'quindi hai perso'


def pareggio():
    """
        Funzione che restituisce la stringa predefinita in output in caso di pareggio

        Ritorna:
            Stringa predefinita in caso di pareggio
    """
    return 'quindi avete pareggiato'

def fine_partita(vittorie, sconfitte, pareggi):
    """
        Funzione che stampa in output le statistiche e dei messaggi specifici a fine partita

        Parametri
            vittorie -- Numero di vittorie conseguite durante la partita
            sconfitte -- Numero di sconfitte subite durante la partita
            pareggi -- Numero di pareggi avvenuti durante la partita

        Ritorna:
            None
    """
    print('La partita è finita')
    statistiche(vittorie, sconfitte, pareggi)


def statistiche(v, s, p):
    """
        Funzione che stampa le statistiche della partita in termini di vittorie, sconfitte e pareggi

        Paramteri:
            v -- Numero di vittorie durante la partita dato in input alla funzione
            s -- Numero di sconfitte durante la partita dato in input alla funzione
            p -- Numero di pareggi durante la partita dato in input alla funzione
    """
    print('Vittorie: ', v, 'Sconfitte: ', s, 'Pareggi:', p)


def morra():
    """
        Procedura che simula il gioco della morra

        Ritorna
            None
    """
    esecuzione = True

    vittorie = sconfitte = pareggi = 0

    #Il numero di vittorie o sconfitte necessarie a terminare una partita va convertito in intero
    #altrimenti non viene riconosciuto dalla funzione di verifica della condizione di fine partita
    numero = int(input('Quante vittorie o sconfitte massime decidono l\'esito della partita? '))

    guida()

    while esecuzione:

        avversario = mostra(smb)

        #Ho preferito prendere un input da tastiera
        scelta_simbolo = input()

        if controlla_input(scelta_simbolo, 'c'):
            if avversario == 'sasso':

                print(scelta_avversario(avversario) + ' ' + vittoria())

                vittorie = vittorie + 1

            elif avversario == 'carta':

                print(scelta_avversario(avversario) + ' ' + pareggio())

                pareggi = pareggi + 1

            else:

                print(scelta_avversario(avversario) + ' ' + sconfitta())

                sconfitte = sconfitte + 1

        elif controlla_input(scelta_simbolo, 'f'):
            if(avversario == 'sasso'):

                print(scelta_avversario(avversario) + ' ' + sconfitta())

                sconfitte = sconfitte + 1

            elif(avversario =='carta'):

                print(scelta_avversario(avversario) + ' ' + vittoria())

                vittorie = vittorie + 1

            else:

                print(scelta_avversario(avversario) + ' ' + pareggio())

                pareggi = pareggi + 1

        elif controlla_input(scelta_simbolo, 's'):
            if(avversario == 'sasso'):

                print(scelta_avversario(avversario) + ' ' + pareggio())

                pareggi = pareggi + 1
            elif(avversario == 'carta'):

                print(scelta_avversario(avversario) + ' ' + sconfitta())

                sconfitte = sconfitte + 1
            else:

                print(scelta_avversario(avversario) + ' ' + vittoria())

                vittorie = vittorie + 1
        elif controlla_input(scelta_simbolo, 'a'):

            guida()

        elif controlla_input(scelta_simbolo, 'u'):

            fine_partita(vittorie,sconfitte,pareggi)

            #Dato che il programma è legato al valore esecuzione settato a True, se diviene False il programma termina
            esecuzione = False
        else:

            print('Scelta non valida')

            guida()

        if condizione_fine_gioco(vittorie, sconfitte, numero):
            fine_partita(vittorie,sconfitte,pareggi)
            esecuzione = False


morra()