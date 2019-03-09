import smtplib
import random

#Lista de pessoas e e - mail dos participantes
pessoas = ["Analu", "Xando", "Arizinho", "Erick", "Emily", "Talitta", "Mychelle", "Suzayde"]
emails = ["analusiqueira@hotmail.com", "asmelo10@hotmail.com", "papel_se@hotmail.com", "erickjsferreira@gmail.com",
          "emilyrs20@hotmail.com", "anatalitta@hotmail.com", "mychelleg2@hotmail.com", "suzaydef@gmail.com"];
#emails = ["asmelo10@hotmail.com", "asmelo10@hotmail.com", "asmelo10@hotmail.com", "asmelo10@hotmail.com",
#          "asmelo10@hotmail.com", "asmelo10@hotmail.com", "asmelo10@hotmail.com", "asmelo10@hotmail.com"];


# Coloca o nome das pessos na caixa
caixa = []
for pessoa in pessoas:
    caixa.append(pessoa)

sorteioFail = True
amigos = []

print('Pessoas: {}'.format(pessoas))
print('Caixa: {}'.format(caixa))

while sorteioFail:
    for inx, pessoa in enumerate(pessoas): #Para caada pessoa sorteia uma pessoa na caixa
        index = random.randrange(0, len(caixa))
        if inx == len(pessoas) - 1: #Caso seja a última pessoa
            if pessoas[inx] == caixa[index]: #Caso a última pessoa pegue ela mesma o sorteio é refeito
                #Coloca o nome de todas as pessoas na caixa novamente
                sorteioFail = True
                caixa = []
                for pessoa in pessoas:
                    caixa.append(pessoa)
                break
            else:
                ##O sorteio deu certo
                # Registra quem é o amigo secreto
                amigos.append(caixa[index])
                sorteioFail = False
                break

        while pessoas[inx] == caixa[index]: #Caso a pessoa tire ela mesma, ela tira outra pessoa
            index = random.randrange(0, len(caixa))

        #Registra quem é o amigo secreto
        amigos.append(caixa[index])

        #Tira o nome sorteado da caixa
        caixa.remove(caixa[index])

print('Sorteio finalizado. Salvando o resultado nos arquivos...')

for inx, amigo in enumerate(amigos):
    file = open('C:\\Users\\Alexandre\\Documents\\AmigoSecreto\\{}.txt'.format(pessoas[inx]), 'w')
    file.write('O amigo secreto de {} eh {}'.format(pessoas[inx], amigo))
    file.close()

print('Enviando os e-mails...')

#Envia os e - mails informando o amigo secreto
for inx, pessoa in enumerate(pessoas):
    nmDestinatario = pessoa
    nmAmigo = amigos[inx]
    assunto = "Amigo Secreto FRIENDS! - ESSE EH O QUE VALE 03!!"
    msg = """Subject: {}\n\nOla {}! ESSE EH O QUE VALE 03!!

                                    Seu amigo secreto eh {}!""".format(assunto, nmDestinatario, nmAmigo)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Acessar https://security.google.com/settings/security/apppasswords para gerar uma senha de app para ser usado aqui
    server.login("asmelo10@gmail.com", "papjtzcgiwduojxj")
    server.sendmail("asmelo10@gmail.com", emails[inx], msg)
    server.quit()

print('Envio Finalizado')