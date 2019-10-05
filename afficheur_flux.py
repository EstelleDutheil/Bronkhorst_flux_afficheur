from tkinter import*
from tkinter.messagebox import*
from creation_serial_port import*
from trames_fonctions import*

numeroDeSerie=''

class instrument:
  def __init__(self):
    self.nom="INSTRUMENT"

  def liste_port(self):
    port_disponible=listing_ports()
    return(port_disponible)

  def cree_port(self):
    monPort=ouverture_de_port()
    return(monPort)

  def laCapacite(self,monPort):
    capacite=Capacity_21('L',0,monPort)
    return(capacite)

  def typeInstrument(self,monPort):
    modeleType=BHT_Model_number_91('L',0,monPort)
    return(modeleType)

  def numeroSerie(self,monPort):
    numeroDeSerie=Serial_number_92('L',0,monPort)
    return(numeroDeSerie)

  def capaciteUnit(self,monPort):
    uniteCapacite=Capacity_unit_129('L',0,monPort)
    return(uniteCapacite)

  def laMesure(self,monPort):
    maMesure=fMeasure_205('L',0,monPort)
    return(maMmesure)

  def laConsigne(self,monPort,consigne):
    fSetpoint_206('E',consigne,monPort)

  def Control_mode(self,monPort,modeControle):
    Control_mode_12('E',modeControle,monPort)

canal1=instrument()
portDisponible=canal1.liste_port()
nbrePort=len(portDisponible)

if nbrePort==0:
  port_actif="Pas d'instrument en ligne"
  instruction="Pour sortir fermer cette fenêtre"
else:
  port_actif="Un instrument en ligne"
  instruction="Pour poursuivre : fermer cette fenêtre"

fenCom=Tk()
fenCom.geometry("400x150+150+50")
fenCom.title("CONFUGURATION")
fenCom['bg']='white'

etiquette_port_actif=Label(fenCom,text=port_actif,bg='white',font="ARIAL 15",fg='red')
etiquette_port_actif.pack()
etiquette_instruction=Label(fenCom,text=instruction,bg='white',font="ARIAL 15",fg='red')
etiquette_instruction.pack()
fenCom.mainloop()

if nbrePort==1:
  portSerie=cree_port_unique()
  canal1.Control_mode(portSerie,0)
  mesure=canal1.laMesure(portSerie)
  capacite=canal1.laCapacite(portSerie)
  unite=canal1.capaciteUnit(portSerie)
  while numeroDeSerie=='':
    numeroDeSerie=canal1.numeroSerie(portSerie)

  def admission_consigne():
    valeur=ent1.get()
    valeur=float(valeur)
    if valeur>capacite:
      message_erreur_cons_max()
    if valeur<(capacite/50)and valeur>0:
      message_erreur_cons_min()
    canal1.laConsigne(portSerie,valeur)

  def message_erreur_cons_max():
    maxi='Consigne maximum = '+str(capacite)
    showerror('Attention ', maxi +''+unite)

  def message_erreur_cons_min():
    miniCapacite=capacite/50
    mini='Consigne minimale = '+str(miniCapacite)
    showerror('Attention ',mini +''+unite)

  counter=0
  def report_mesure(etiquette_mesure_reelle):
    def count():
      global counter
      counter += 1
      valeur_mesure=str(canal1.laMesure(portSerie))
      etiquette_mesure_reelle.config(text=valeur_mesure+" "+unite)
      etiquette_mesure_reelle.after(100, count)
    count()

  fen=Tk()
  fen.geometry("450x150+50+50")
  fen.title("Flow Display")
  fen['bg']='gray95'

  etiquette_serie=Label(fen,text=numeroDeSerie,bg="#88ff88",width=65,font="ARIAL 20",fg='blue')
  etiquette_serie.pack()

  etiquette_mesure=Label(fen,text="MESURE",bg="gray96",fg="green",font="ARIAL 15")
  etiquette_mesure.place(x='40',y='50')

  etiquette_consigne=Label(fen,text="CONSIGNE",bg="gray96",fg="red",font="ARIAL 15")
  etiquette_consigne.place(x='270',y='50')

  etiquette_mesure_reelle=Label(fen,bg="gray96",fg="green",font="ARIAL 30")
  etiquette_mesure_reelle.place(x='35',y='85')
  report_mesure(etiquette_mesure_reelle)
  bouton=Button(fen,text='oK',command=admission_consigne,bg="gray96",fg="blue",bd=5,font="ARIAL 10")
  bouton.place(x='400',y='90')
  ent1=Entry(fen,width=10,font="ARIAL 18",bd=5)
  ent1.place(x='250',y='90')

  fen.mainloop()
