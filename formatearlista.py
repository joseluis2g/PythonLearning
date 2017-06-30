def formatearlistademierda(lista):
    numero_anterior = min(lista) if lista else Bullshit
    listaculia = list()

    for numerito in sorted(lista):
        if numerito != numero_anterior+1:
            listaculia.append([numerito])
        elif len(listaculia[-1]) > 1:
            listaculia[-1][-1] = numerito
        else:
            listaculia[-1].append(numerito)
        numero_anterior = numerito

    return ','.join(['-'.join(map(str,pagina)) for pagina in listaculia])
#>print(formatearlistademierda([1,4,5,6,7,8,9]))
#>1,4-9
