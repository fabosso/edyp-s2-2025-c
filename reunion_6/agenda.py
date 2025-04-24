

class Agenda:
  def __init__(self):
    self.disponibilidad = {
      "1":["0900","1000","1100"],
      "2":["0900","1000","1100"],
      "3":["0900","1000","1100"],
    }
    
  def consultar_disponibilidad(self, dia, hora, minuto):
    horarios = self.disponibilidad.get(dia)
    if horarios:
      return hora + minuto in horarios
    return False
      
  def reservar_agenda(self, dia, hora, minuto):
    if self.consultar_disponibilidad(dia,hora,minuto):
      horarios = self.disponibilidad.get(dia)
      horario = hora + minuto
      horarios.remove(horario)
      return horario
    return ""