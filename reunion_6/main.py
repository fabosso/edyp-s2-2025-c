from consultorio import Consultorio
from paciente import Paciente
from odontologo import Odontologo
from agenda import Agenda


def main():
    carlos = Paciente("123", "Carlos")
    juan = Paciente("345", " Juan")
    prof = Odontologo("100", "Pepe")
    agenda_pepe = Agenda()
    prof.cargar_agenda(agenda_pepe)

    consultorio = Consultorio("Muelita")
    consultorio.agregar_paciente(carlos)
    consultorio.agregar_paciente(juan)
    consultorio.agregar_profesional(prof)
    print("=====PACIENTES=====")
    print(consultorio.pacientes)
    print("=====PROFESIONALES=====")
    print(consultorio.profesionales)
    print("=====DISPONIBILIDAD AGENDA 1 a las 11=====")
    print(prof.agenda.consultar_disponibilidad("1", "11", "00"))
    print("=====DISPONIBILIDAD AGENDA 4 a las 11=====")
    print(prof.agenda.consultar_disponibilidad("4", "11", "00"))
    print("=====RESERVO AGENDA 1 a las 11=====")
    print(prof.agenda.reservar_agenda("1", "11", "00"))
    print("=====DISPONIBILIDAD AGENDA 1 a las 11=====")
    print(prof.agenda.consultar_disponibilidad("1", "11", "00"))
    print("=====ENTREGAR TURNO 1 a las 11=====")
    consultorio.asignar_turno("100", "123", "1", "11", "00")
    consultorio.imprimir_turnos()
    print("=====ENTREGAR TURNO 1 a las 12=====")
    consultorio.asignar_turno("100", "123", "1", "12", "00")
    consultorio.imprimir_turnos()
    print("=====ENTREGAR TURNO 2 a las 10=====")
    consultorio.asignar_turno("100", "345", "2", "10", "00") 
    consultorio.imprimir_turnos()
    print("=====ATENDER TURNO 2=====")
    consultorio.atender_turno("345")
    consultorio.imprimir_turnos()
    print("=====ATENDER TURNO 1=====")
    consultorio.atender_turno("123")
    consultorio.imprimir_turnos()
    print("Fin del programa")


main()
