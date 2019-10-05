def conversion_n_hexaDecimal_en_string_chr(n_hexa): #n_hexa  bytes
  reponse=""
  for bla in range (0,(len(n_hexa))):
    if bla%2==0:
      caractere=n_hexa[bla:(bla+2)]
      caractere=str(caractere)
      caractere=caractere[2:4]
      caractere=int(caractere,16)
      limiteur=caractere
      caractere=chr(caractere)
      reponse=reponse+caractere
      if limiteur<33 or limiteur>126:
        break
  return(reponse)
