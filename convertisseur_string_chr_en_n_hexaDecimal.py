from convertisseur_1int_1byte import conversion_1int_1byte

def conversion_string_chr_en_n_hexaDecimal(chaine_chr):
  hexaDecimal=b''
  for bla in range(0,(len(chaine_chr))):
    caractere=chaine_chr[bla]
    caractere=ord(caractere)
    caractere=conversion_1int_1byte(caractere)
    hexaDecimal=hexaDecimal+caractere
  return(hexaDecimal)
