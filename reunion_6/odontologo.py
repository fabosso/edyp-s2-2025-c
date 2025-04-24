from profesional import Profesional
from agenda import Agenda


class Odontologo(Profesional):
  def __init__(self,registro, nombre):
    super().__init__(nombre,registro)
  
  def cargar_agenda(self, agenda):
    if isinstance(agenda, Agenda):
      self.agenda = agenda
  
  def __repr__(self):
    return "Odontologo: " + super().__repr__()
    
  def __str__(self):
    return self.__repr__()
    