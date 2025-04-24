from paciente import Paciente
from profesional import Profesional
from turno import Turno

class Consultorio:
  def __init__(self, nombre):
    self.nombre = nombre
    self.pacientes = {}
    self.profesionales = {}
    self.turnos = []
    
  def agregar_paciente(self, paciente):
    if isinstance(paciente, Paciente):
      self.pacientes[paciente.dni] = paciente
      
  def agregar_profesional(self, profesional):
    if isinstance(profesional, Profesional):
      self.profesionales[profesional.registro] = profesional
      
  def asignar_turno(self, registro_prof, dni_pac, dia, hora, minuto):
    prof = self.profesionales.get(registro_prof)
    pac = self.pacientes.get(dni_pac)
    # validar dia
    # validar hora
    if prof and pac and dia and hora and minuto:
      turno = prof.agenda.reservar_agenda(dia, hora, minuto)
    else:
      print("no hallado", prof, pac, dia, hora, minuto)
      turno = None
    if turno:
      self.turnos.append(Turno( prof, pac, dia, hora))
      
  def imprimir_turnos(self):
    for i, turno in enumerate(self.turnos):
      print(i + 1," ", turno)
      