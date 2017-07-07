def rutChequeo(rut):
    if len(rut) == 9:
        rutx = str(rut[0:len(rut)-1])
        digito = str(rut[-1])
        multiplo = 2
        total = 0
        for reverso in reversed(rutx):
            total += int(reverso) * multiplo
            multiplo = (multiplo == 7 and 2 or multiplo + 1)
            verificador = ((11 - (total % 11)) == 10 and "K") or ((11 - (total % 11)) == 11 and "0") or (11 - (total % 11))
        if str(verificador) == str(digito.upper()):
            return True
        else:
            return False
    else:
        return False
