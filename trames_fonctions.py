from convertisseur_n_hexaDecimal_en_string_chr import*
from convertisseur_string_chr_en_n_hexaDecimal import*
from convertisseur_1int_1byte import*
from convertisseur_1byte_1int import*
from convertisseur_4hexaDecimal_1float import*
from convertisseur_1float_4hexaDecimal import*

def Control_mode_12(commande_12,valeur_12,portSerie_12):
    if commande_12=='L':
      portSerie_12.write(b':06800401040104\r\n')
      reponse_12=portSerie_12.readline()
      reponse_12=conversion_1byte_1int(reponse_12[11:13])
      return(reponse_12)
    elif commande_12=='E':
      valeur_12=conversion_1int_1byte(valeur_12)
      ecrit_12=b':0580020104'+valeur_12+b'\r\n'
      portSerie_12.write(ecrit_12)

def Capacity_21(commande_21,valeur_21,portSerie_21):
    if commande_21=='L':
      portSerie_21.write(b':068004014D014D\r\n')
      reponse_21=portSerie_21.readline()
      reponse_21=conversion_4hexaDecimal_1float(reponse_21[11:19],2)
      return(reponse_21)
    elif commande_21=='E':
      valeur_21=conversion_1float_4hexaDecimal(valeur_21)
      ecrit_21=b':088002014D'+valeur_21+b'\r\n'
      portSerie_21.write(ecrit_21)

def BHT_Model_number_91(commande_91,valeur_91,portSerie_91):
  if commande_91=='L':
    portSerie_91.write(b':06800471627162\r\n')
    reponse_91=portSerie_91.readline()
    reponse_91=conversion_n_hexaDecimal_en_string_chr(reponse_91[13:50])
    return(reponse_91)
  elif commande_91=='E':
    valeur_91=conversion_string_chr_en_n_hexaDecimal(valeur_91)
    longueur_91=len(valeur_91)
    longueur_91=longueur_91+4
    nbre_hexa_trame=conversion_1int_1byte(longueur_91)
    ecrit_91=b':'+nbre_hexa_trame+b'80027162'+valeur_91+b'\r\n'
    portSerie_91.write(ecrit_91)

def Serial_number_92(commande_92,valeur_92,portSerie_92):
  if commande_92=='L':
    portSerie_92.write(b':06800471637163\r\n')
    reponse_92=portSerie_92.readline()
    reponse_92=conversion_n_hexaDecimal_en_string_chr(reponse_92[13:50])
    return(reponse_92)
  elif commande_92=='E':
    valeur_92=conversion_string_chr_en_n_hexaDecimal(valeur_92)
    longueur_92=len(valeur_92)
    longueur_92=longueur_92+4
    nbre_hexa_trame=conversion_1int_1byte(longueur_92)
    ecrit_92=b':'+nbre_hexa_trame+b'80027163'+valeur_92+b'\r\n'
    portSerie_92.write(ecrit_92)

def Capacity_unit_129(commande_129,valeur_129,portSerie_129):
  if commande_129=='L':
    portSerie_129.write(b':08004017F017F07\r\n')
    reponse_129=portSerie_129.readline()
    reponse_129=conversion_n_hexaDecimal_en_string_chr(reponse_129[13:50])
    return(reponse_129)
  elif commande_129=='E':
    valeur_129=conversion_string_chr_en_n_hexaDecimal(valeur_129)
    longueur_129=len(valeur_129)
    longueur_129=longueur_129+4
    nbre_hexa_trame=conversion_1int_1byte(longueur_129)
    ecrit_129=b':'+nbre_hexa_trame+b'8002017F'+valeur_129+b'\r\n'
    portSerie_129.write(ecrit_129)

def fMeasure_205(commande_205,valeur_205,portSerie_205):
  if commande_205=='L':
    portSerie_205.write(b':06800421402140\r\n')
    reponse_205=portSerie_205.readline()
    reponse_205=conversion_4hexaDecimal_1float(reponse_205[11:19],2)
    return(reponse_205)

def fSetpoint_206(commande_206,valeur_206,portSerie_206):
  if commande_206=='L':
    portSerie_206.write(b':06800421432143\r\n')
    reponse_206=portSerie_206.readline()
    reponse_206=conversion_4hexaDecimal_1float(reponse_206[11:19],2)
    return(reponse_206)
  elif commande_206=='E':
    valeur_206=conversion_1float_4hexaDecimal(valeur_206)
    ecrit_206=b':0880022143'+valeur_206+b'\r\n'
    portSerie_206.write(ecrit_206)
