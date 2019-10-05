def conversion_4hexaDecimal_1float(hexaDecimal,ptVirgule):
  a=hexaDecimal
  b=int(a,16)
  binaire=format(b,'0>32b')
  if(binaire=="00000000000000000000000000000000"):
    valeur=0.00
  else:
    sbit,ebit,mbit=binaire[:1],binaire[1:9],binaire[9:]
    ebit=int(ebit,2)
    exposant=int(ebit)-127
    mbit=int(mbit,2)
    mantise=1+mbit/(1<<23)
    valeur=mantise*2**exposant
  return(round(valeur,ptVirgule))
