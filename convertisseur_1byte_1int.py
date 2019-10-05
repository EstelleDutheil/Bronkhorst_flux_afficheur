def conversion_1byte_1int(hexa):#hexa<class'bytes'>
  unit=hexa[1]
  diz=hexa[0]
  if unit==48:
    val_unit=0
  if unit==49:
    val_unit=1
  if unit==50:
    val_unit=2
  if unit==51:
    val_unit=3
  if unit==52:
    val_unit=4
  if unit==53:
    val_unit=5
  if unit==54:
    val_unit=6
  if unit==55:
    val_unit=7
  if unit==56:
    val_unit=8
  if unit==57:
    val_unit=9
  if unit==65:
    val_unit=10
  if unit==66:
    val_unit=11
  if unit==67:
    val_unit=12
  if unit==68:
    val_unit=13
  if unit==69:
    val_unit=14
  if unit==70:
    val_unit=15
  if diz==48:
    val_diz=0
  if diz==49:
    val_diz=16
  if diz==50:
    val_diz=32
  if diz==51:
    val_diz=48
  if diz==52:
    val_diz=64
  if diz==53:
    val_diz=80
  if diz==54:
    val_diz=96
  if diz==55:
    val_diz=112
  if diz==56:
    val_diz=128
  if diz==57:
    val_diz=144
  if diz==65:
    val_diz=160
  if diz==66:
    val_diz=176
  if diz==67:
    val_diz=192
  if diz==68:
    val_diz=208
  if diz==69:
    val_diz=224
  if diz==70:
    val_diz=240
  val=val_diz+val_unit
  return(val)
