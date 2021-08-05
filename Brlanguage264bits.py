import sys
import time

print('a linguagem br é uma linguagem feita para aprendizado ela não é apropriado para projetos grandes')

start = ''

#INT
IntValor = 0
nameInt = '&'

#STRING
nameString = '&'
StringValor = 0

#STRING REP
nameString2 = '&'
stringvalorrep = '&'
rep1 = '&'
rep2 = '&'

#FLOAT
nameFloat = '&'
valorFloat = 0

#BOOL
nameLogica = '&'
valorLogica = False

#LOOP
qvloop = 1
ConsoleLoop = '&'

#ESCREVER
escname = '&'
escnome = '&'
escv = '&'
escsla = ''

while True:
    Console = input('>>> ')
    if 'imprimir ' in Console:
        if Console[9:] == nameInt:
            start = start + str(IntValor) + '\n'
        elif Console[9:] == nameString:
            start = start + StringValor + '\n'
        elif Console[9:] == nameString2:
            start = start + stringvalorrep + '\n'
        elif Console[9:] == nameFloat:
            start = start + str(valorFloat) + '\n'
        elif Console[9:] == nameLogica:
            start = start + str(valorLogica) + '\n'
        else:
            start = start + Console[9:] + '\n'
    elif '<Calculo type="+">' in Console:
        a = input('>>;')
        b = input('>>;')
        if nameInt in a:
            a = IntValor
        elif nameInt in b:
            b = IntValor
            c = a + b
            start = start + str(c) + '\n'
        a = int(a)
        b = int(b)
        c = a + b
        start = start + str(c) + '\n'
    elif '<Calculo>' in Console:
        a = input('>>;')
        b = input('>>;')
        if nameInt in a:
            a = IntValor
        elif nameInt in b:
            b = IntValor
            c = a + b
            start = start + str(c) + '\n'
        a = int(a)
        b = int(b)
        c = a + b
        start = start + str(c) + '\n'
    elif '<Calculo type="-">' in Console:
        a = input('>>;')
        b = input('>>;')
        if a == nameInt:
            a = IntValor
        elif b == nameInt:
            b = IntValor
            c = a - b
            start = start + str(c) + '\n'
        a = int(a)
        b = int(b)
        c = a - b
        start = start + str(c) + '\n'
    elif '<Calculo type="/">' in Console:
        a = input('>>;')
        b = input('>>;')
        if a == nameInt:
            a = IntValor
        elif b == nameInt:
            b = IntValor
            c = a / b
            start = start + str(c) + '\n'
        a = int(a)
        b = int(b)
        c = a / b
        start = start + str(c) + '\n'
    elif '<Calculo type="x">' in Console:
        a = input('>>;')
        b = input('>>;')
        if a == nameInt:
            a = IntValor
        elif b == nameInt:
            b = IntValor
            c = a * b
            start = start + str(c) + '\n'
        a = int(a)
        b = int(b)
        c = a * b
        start = start + str(c) + '\n'
    elif '<int>' in Console:
        nameInt = Console[6:]
        IntValor = input('>>;')
        IntValor = int(IntValor)
    elif '<string>' in Console:
        nameString = Console[9:]
        StringValor = input('>>;')
        StringValor = str(StringValor)
    elif '<string type="Rep">' in Console:
        nameString2 = Console[20:]
        StringValor = input('>>;')
        StringValor = str(StringValor)
        rep1 = input('>>;')
        rep1 = str(rep1)
        rep2 = input('>>;')
        rep2 = str(rep2)
        stringvalorrep = StringValor.replace(rep1, rep2)
    elif '<Reais>' in Console:
        nameFloat = Console[8:]
        valorFloat = input('>>;')
        valorFloat = float(valorFloat)
    elif '<Logica>' in Console:
        nameLogica = Console[9:]
        valorLogica = input('>>;')
        if valorLogica == "True":
            valorLogica = True
        elif valorLogica == "False":
            valorLogica = False
        elif valorLogica == "1":
            valorLogica = True
        elif valorLogica == "0":
            valorLogica = False
        else:
            valorLogica = bool(valorLogica)
    elif 'Start' in Console:
        print(start)
    elif '<loop> ' in Console:#EM DESENVOLVIMENTO
        qvloop = Console[7:]
        ConsoleLoop = input('>>;')
        ConsoleLoop = str(ConsoleLoop)
        qvloop = int(qvloop)
        for i in range(qvloop):
            start = start + ConsoleLoop + '\n'
    elif '<Se type=">">' in Console:#EM DESENVOLVIMENTO
        IfCond = input('>>;')
        IfCond = int(IfCond)
        IfCond2 = input('>>;')
        IfCond2 = int(IfCond2)
        if IfCond > IfCond2:
            while True:
                Console = input('>>> ')
                if 'imprimir ' in Console:
                    if Console[9:] == nameInt:
                        print(IntValor)
                    elif Console[9:] == nameString:
                        print(StringValor)
                    elif Console[9:] == nameString2:
                        print(stringvalorrep)
                    elif Console[9:] == nameFloat:
                        print(valorFloat)
                    elif Console[9:] == nameLogica:
                        print(valorLogica)
                    else:
                        print(Console[9:])
                elif 'break' in Console:
                    break
        else:
            while True:
                Console = input('>>> ')
                if 'imprimir ' in Console:
                    if Console[9:] == nameInt:
                        print(IntValor)
                    elif Console[9:] == nameString:
                        print(StringValor)
                    elif Console[9:] == nameString2:
                        print(stringvalorrep)
                    elif Console[9:] == nameFloat:
                        print(valorFloat)
                    elif Console[9:] == nameLogica:
                        print(valorLogica)
                    else:
                        print(Console[9:])
                elif 'break' in Console:
                    break












