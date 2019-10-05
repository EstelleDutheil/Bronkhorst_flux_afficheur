import struct

def conversion_1float_4hexaDecimal(dec):
	if dec==0.00:
		valeur=b'00000000'
	else:
		valeur=""
		value=hex(struct.unpack('<I',struct.pack('<f',dec))[0])
		for bla in range(2,10):
      			integer=ord(value[bla])
      			if(integer>=97 and integer<=102):
				a=chr(integer-32)
        			valeur=valeur+a
      			else:
        			valeur=valeur+value[bla]
		valeur=bytes(valeur,'utf-8')
	return(valeur)
