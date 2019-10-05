def conversion_1int_1byte(val):
  if val/16<1:
    premier=48
  if val/16>=1 and val/16<2:
    premier=49
  if val/16>=2 and val/16<3:
    premier=50
  if val/16>=3 and val/16<4:
    premier=51
  if val/16>=4 and val/16<5:
    premier=52
  if val/16>=5 and val/16<6:
    premier=53
  if val/16>=6 and val/16<7:
    premier=54
  if val/16>=7 and val/16<8:
    premier=55
  if val/16>=8 and val/16<9:
    premier=56
  if val/16>=9 and val/16<10:
    premier=57
  if val/16>=10 and val/16<11:
    premier=65
  if val/16>=11 and val/16<12:
    premier=66
  if val/16>=12 and val/16<13:
    premier=67
  if val/16>=13 and val/16<14:
    premier=68
  if val/16>=14 and val/16<15:
    premier=69
  if val/16>=15 and val/16<16:
    premier=70
  if val%16==0:
    second=48
  if val%16==1:
    second=49
  if val%16==2:
    second=50
  if val%16==3:
    second=51
  if val%16==4:
    second=52
  if val%16==5:
    second=53
  if val%16==6:
    second=54
  if val%16==7:
    second=55
  if val%16==8:
    second=56
  if val%16==9:
    second=57
  if val%16==10:
    second=65
  if val%16==11:
    second=66
  if val%16==12:
    second=67
  if val%16==13:
    second=68
  if val%16==14:
    second=69
  if val%16==15:
    second=70
  resultat=byte([premier,second])
  return(resultat) 
