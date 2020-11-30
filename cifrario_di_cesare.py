import time

ALFABETO = "abcdefghijklmnopqrstuvwxyz"
class cesareCifrario:
    #costruttore
    def __init__(self,k):
        pass
    #codifica una singola lettera
    def codifica_lettera(self,c,k):
        pos_lettera = ALFABETO.find(c)
        pos_let_cifrata = (int(pos_lettera) +int(k)) % 26
        # ((ALFABETO.find(ALFABETO[lettera])+k)%26 )

        return ALFABETO[pos_let_cifrata]
    
    #decodifica una singola lettera
    def decodifica_lettera(self , c,k):
        pos_lettera = ALFABETO.find(c)
        pos_let_cifrata = (int(pos_lettera) - int(k)) % 26

        return ALFABETO[pos_let_cifrata]

    #codifica un testo

    def codifica_testo(self, text,k):
        text_puro = ""
        text_codficato = ""
        for i in range(len(text)) :
            lettera = ALFABETO.find(text[i]) 
    
            if lettera != -1 :
                text_codficato = text_codficato + cesareCifrario.codifica_lettera(self , ALFABETO[lettera],k)
                text_puro = text_puro + text[i] 
   
  
        #print("il testo senza schifezze : " + text_puro)


        return text_codficato
    
    #decodifica un testo

    def decodifica_testo(self , text, k):
        text_codficato = ""
        for i in range(len(text)) :
            lettera = ALFABETO.find(text[i]) 
    
            if lettera != -1 :
                text_codficato = text_codficato + cesareCifrario.decodifica_lettera(self , ALFABETO[lettera],k)
      
   
   
        return text_codficato

    def decodifica_senza_key(self,text):
        k=0
        while k<26:
            print("TESTO DECODIFICATO CON LA CHIAVE : " + str(k) + " "+ cesareCifrario.decodifica_testo(self,text,k))
            time.sleep(1)
            k+=1


         

