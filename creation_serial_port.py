import serial
#import serial.tools.list_ports

def listing_ports():
  portSerieListe=[]*10
  for i in range(0,10):
    try:
      portS='/dev/ttyUSB'+str(i)
      s=serial.Serial(portS,baudrate=38400,timeout=1)
      portSerieListe.append(s)
      s.close()
    except serial.SerialException:
      pass
  return(portSerieListe)

def ouverture_de_port():
  trameTest=b':0780047163716309\r\n'
  for bla in range(0,10):
    try:
      portS='/dev/ttyUSB'+str(bla)
      portComTest=serial.Serial(portS,38400,timeout=1)
      portComTest.write(trameTest)
      portComReponse=portComTest.readline()
      portComTest.close()
      if(portComReponse[0:11]==b':0E80027163'):
        portComActif=serial.Serial(portS,38400)
        portComTest.close()
    except serial.SerialException:
      pass
  return(portComActif)
