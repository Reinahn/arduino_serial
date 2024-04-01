import serial
import time
import matplotlib.pyplot as plt

def plotar(amostras_qt):

    with open('teste.txt','r') as ler:
        linhas = ler.readlines()
        led = [linha.split(' ')[0] for linha in linhas]
        potenc = [linha.split(' ')[2] for linha in linhas]


    led = led[-int(amostras_qt):] # pegar as ultimas amostras
    potenc = potenc[-int(amostras_qt):] # pegar as ultimas amostras

    # Led
    ax.clear()
    ax.plot(led, label = 'Led',c='red')

    ax.set_title('Valores obtidos do Led')
    ax.set_xlabel('Amostras')
    ax.set_ylabel('Led')

    # Potenciometro
    ax2.clear()
    ax2.plot(potenc, label = "Potenciometro",c='orange')

    ax2.set_title('Valores obtidos do Potenciometro')
    ax2.set_xlabel('Amostras')
    ax2.set_ylabel('Potenciometro')

    plt.show()

    ler.close()

led = []
potenc = []

fig = plt.figure()
ax = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

time.sleep(2)

arduino = serial.Serial(port="COM6",baudrate=9600, timeout=1)
time.sleep(3)

arquivo = open('teste.txt','a')

amostras = 200

contar = 0

while contar < amostras:

    print(' a -> ligar | b -> desligar | p -> plotar grafico')

    entrada = input("Entre com um dos valores acima: ")

    if entrada == "a":
        # arduino.write(b'a') # Nota: quando o arduino estiver conectado retire o primeiro comentario
        pass
    elif entrada == "b":
        # arduino.write(b'b') # Nota: quando o arduino estiver conectado retire o primeiro comentario
        pass
    elif entrada == "p":
        amostras_entrada = input('Quantidades de amostras para exibir: ')

        plotar(amostras_entrada)

    # valor = arduino.readline().decode('utf-8')

    # arquivo.write(valor)

    contar += 1

arquivo.close()

arduino.close()

# ============================
# Codigo para popular o arquivo teste.txt para fazer o teste sem o arduino
# ============================
# import random

# salvar = open('teste.txt','a')

# amostras = 0

# while amostras < 200:

#     pot = random.randint(100,200)
#     led = random.randint(0,1)

#     salvar.write(str(led))
#     salvar.write('  ')
#     salvar.write(str(pot))
#     salvar.write('\n')

#     amostras += 1

# salvar.close()