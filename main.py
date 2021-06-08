class Rujbin:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def funk(self):
    print(self.x + self.y)
    
  def falls(self):
    if self.x < self.y:
      print("5 ist kleiner als 10")
    else:
      print("5 ist größer als 10")
      
  def Funktion(self):
    self.Liste = ["Rujbin", "Nassereslam"]
    self.Liste[0:2] = ["Lol","Rujbinn"]
    print(self.Liste)
    
  def WenninListe(self):  
    if "Rujbinn" in self.Liste:
      print("Rujbinn ist in Liste")
    else:
      print("Rujbinn ist nicht in Liste")
Rb = Rujbin(5,10)
Rb.funk()
Rb.falls()
Rb.Funktion()
Rb.WenninListe()
