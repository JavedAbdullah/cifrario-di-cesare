from cifrario_di_cesare import cesareCifrario


def main():

    algoritmo_cesare = cesareCifrario('')
    out_per_utente = '''

    Ciao caro Utente BENVEUTO AL CIFRARIO DI CESARE , cosa desidera fare ?
    1 - codificare una lettera
    2 - decodificare una lettera
    3 - codificare un testo
    4 - decodificare un testo 
    5 - decodificare senza la chiave

    '''
    ricevuto = int(input(out_per_utente))
    if ricevuto == 1:
        lettera = input(" \ndigitare la lettera da codificare \n ")
        k = input("\n digitare la chiave \n")
        print(" lettera codificata : \n "+algoritmo_cesare.codifica_lettera(lettera,k))
    elif ricevuto == 2:
        lettera = input(" \ndigitare la lettera da decodificare \n")
        k = input("\n digitare la chiave \n")
        print(" lettera decodificata \n"+algoritmo_cesare.decodifica_lettera(lettera,k))
    elif ricevuto == 3 : 
        text = input("\ndigitare il testo da codificare \n")
        k = input("\n digitare la chiave \n")
        print(algoritmo_cesare.codifica_testo(text,k))
    elif ricevuto == 4 :
        text = input("\ndigitare il testo da decodificare \n")
        k = input("\n digitare la chiave \n")
        print(algoritmo_cesare.decodifica_testo(text,k))
    elif ricevuto == 5 :
        text =  input(" \ndigitare il testo da decodificare senza la chiave \n5")
        print(algoritmo_cesare.decodifica_senza_key(text))










main()