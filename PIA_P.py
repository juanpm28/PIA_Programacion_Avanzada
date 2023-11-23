import re
from datetime import datetime
import os
import pickle


year_actual = datetime.now().year

class archivos:
    objeto = ''
    archivo = 'default.txt'

    def init(self, objeto='', archivo=''):
        self.objeto = objeto
        self.archivo = archivo

    def guardarAr(self, objeto='', archivo=''):
        respaldar = False
        try:
            with open(archivo, 'a') as f:
                for clave, valores in objeto.items():
                    linea = f"{clave}: {', '.join(valores)}\n"
                    f.write(linea)
            f.close()
            #Serializacion
            with open(archivo, 'r') as txt:
              contenido = txt.read()

            lista_contenido = contenido.split('\n')
            nomPickle = archivo.split('.')[0] + '.pickle'
            # Guardar la lista en un archivo .pickle
            with open(nomPickle, 'wb') as pickF:
                pickle.dump(lista_contenido, pickF)


        except Exception as e:
            return f"Error a la hora de registrar en el archivo: {e}"

    def leer(self, archivo):
        with open(archivo, "r") as f:
            datos_recuperados = f.read()
        f.close()
        lineas = datos_recuperados.split('\n')
        diccionario = {}

        for linea in lineas:
            if linea:
                partes = linea.split(':')
                clave = partes[0].strip()
                valores = partes[1].split(',')
                valores = [valor.strip() for valor in valores]
                diccionario[clave] = valores
        return diccionario

    def eliminar(self,nomAr, diccionario):
      with open(nomAr, "w+") as f:
        for clave, valores in diccionario.items():
          linea = f"{clave}: {', '.join(valores)}\n"
          f.write(linea)
      
    def modificar(self, nomAr, diccionario):
      with open(nomAr, "w+") as f:
        for clave, valores in diccionario.items():
          linea = f"{clave}: {', '.join(valores)}\n"
          f.write(linea)
          
          
class Acciones():
  
  def __init__(self):
        self.year_actual = datetime.now().year
        # self.contador_asistentes = 1
        # self.contador_registros = 1
        self.diccAsistentes = {}
        self.diccRegistros = {}
        self.diccAsistencias = {}
        self.fecha = None
        self.carrera = None
        
        # Menus
        self.opciones_menu_principal={
            'A':'Acciones datos del asistente',
            'B':'Registrar asistente a un evento',
            'C':'Registrar asistencia al evento',
            'D':'Ver conferencias asistente',
            'E':'Ver cantidad de asientos disponibles',
            'F':'Eliminar registro de asistente a evento',
            'G':'Consultar información conferencia',
            'H':'Generar constancia de participación',
            'I':'Mostrar registros a eventos',
            'X':'Salir\n'
        }

        self.opciones_menu_asistentes={
            'A':'Agregar un asistente',
            'B':'Eliminar asistente',
            'C':'Actualizar datos del asistente',
            'D':'Consultar asistente',
            'X':'Regresar al menú principal\n'
        }
        
        # Representación de auditorios en un diccionario.
        self.auditorios = {
            'A': ['Gumersindo Cantú Hinojosa', 1000],
            'B': ['Víctor Gómez', 200],
            'C': ['Casas Alatriste', 150]
        }

        # CONFERENCIAS
        # fecha y hora, nombre de conferencia, presentador, letra de auditorio, n asistentes registrados
        self.conferencias = {
            1: ['04/11/2023 15:00', 'Inteligencia Artificial en los Negocios',
                'Dr. Alvaro Francisco Salazar', 'A', 0],
            2: ['05/11/2023 09:00', 'Uso de la nube para gestión de procesos',
                'Dr. Manuel Leos', 'B', 0],
            3:['05/11/2023 14:00','Industria 4.0 retos y oportunidades',
                'Dra. Monica Hernández','C', 20],
            4:['05/11/2023 19:00','Machine Learning for a better world',
                'Dr. Janick Jameson','C', 0], 
            5:['06/11/2023 15:00','Retos de la Banca Electrónica en México',
                'Ing. Clara Benavides','A', 0]
        }

        # Carreras
        self.carreras = {
            'LTI': 'LICENCIADO EN TECNOLOGÍA DE LA INFORMACIÓN',
            'LA': 'LICENCIADO EN ADMINISTRACIÓN',
            'CP': 'CONTADOR PÚBLICO',
            'LNI': 'LICENCIADO EN NEGOCIOS INTERNACIONALES',
            'LGRS': 'LICENCIADO EN GESTIÓN DE RESPONSABILIDAD SOCIAL'
        }
        
        with open('asistentes.txt', 'a'):
            pass
        self.a = archivos()
        self.diccAsistentes = self.a.leer('asistentes.txt')
        self.asistentes = {}
        # self.contador_asistentes = 1    
        
  def elegir_letra(self, prompt='Dame una letra: ', opciones_validas='12345'):
      while True:
          opcion = input(prompt)
          opcion = opcion.upper()
          if opcion == '':
              print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo')
              continue
          if not bool(re.match(f'^[{opciones_validas}]$', opcion)):
              print('Error en captura. Opción no reconocida. Inténtelo de nuevo')
              continue
          # If everything went well, exit the loop
          break
      return opcion
  # print(elegir_letra('Select a letter: ', 'ABCDE'))

  def mostrar_menu(self,
      opciones:dict,
      titulo:str='OPCIONES DISPONIBLES'):

      print(titulo)
      opciones_validas=''
      for k,v in opciones.items():
          print(f'[{k}] {v}')
          opciones_validas=f'{opciones_validas}{k}'
          # opciones_validas += k

      opc=self.elegir_letra('¿Qué opción deseas?: ', opciones_validas).upper()
      return opc
    
  # print(mostrar_menu({'A':'Hola', 'B':'Adios'}))

  #---------------- VALIDACIONES ASISTENTES -----------------#

  def matricula_validacion(self, prompt:int='Ingresa la matrícula\n'):
      while True:
        self._matricula = input(prompt)
        if self._matricula == (''):
          print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo.')
          continue
        try:
          self.matricula = int(self._matricula)
        except:
          print('Error en captura. Matrícula debe contener solo dígitos. Inténtelo de nuevo.')
          continue
        return self._matricula

  def nombres_validacion(self, prompt:str='Ingresa un nombre'):
    while True:
        self.nombre = input(prompt)
        if self.nombre == (''):
            print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo.')
            continue
        if not self.nombre.isalpha():
            print('Error en captura. El nombre solo contiene letras. Inténtelo de nuevo.')
            continue
        self.nombre = self.nombre.capitalize()
        return self.nombre


  def nacimiento_validacion(self, prompt='Ingresa la fecha de nacimiento. DD/MM/YYYY\n'):
      while True:
          self.fecha = input(prompt)
          if self.fecha == (''):
              print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo.')
              continue
          if not self.fecha.replace('/', '').isdigit():
              print('Error en captura. No se aceptan más que dígitos y "/". Intenta de nuevo.')
              continue
          try:
              datetime.strptime(self.fecha, '%d/%m/%Y')  # Método para comprobar la estructura proporcionada
          except:
              print('Error en captura. La fecha no cumple con la estructura. Inténtelo de nuevo.')
              continue
          año_nacimiento = int(self.fecha[6:])
          if (year_actual - año_nacimiento) <= 14:
              print('Error. Año de nacimiento no válido. Inténtelo de nuevo.')
              continue
          return self.fecha

  def carrera_validacion(self, prompt='Ingresa las siglas de la carrera. LTI, LA, CP, LNI, LGRS\n'):
      while True:
          self.carrera = input(prompt)
          self.carrera = self.carrera.upper()
          if self.carrera == '':
              print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo.')
              continue
          if not bool(self.carrera.isalpha()):
              print('Error en captura. Solo se aceptan letras. Inténtelo de nuevo.')
              continue
          if self.carrera not in self.carreras:
              print('Error. Carrera no válida. Inténtalo de nuevo.')
              continue
          return self.carrera

  # contador_asistentes = 1
  # with open('asistentes.txt', 'a'):
  #     # No necesitas realizar ninguna operación dentro del bloque
  #     pass
  # a = archivos()

  # diccAsistentes = a.leer('asistentes.txt')
  # asistentes = {}


  def agregar_asistente(self):
        while True:
            matricula = self.matricula_validacion()
            if matricula in self.diccAsistentes:
                print('Error. Matrícula ya registrada. Intenta con una nueva matrícula.')
                continue    
            break
        nombre = self.nombres_validacion('Ingresa el nombre\n')
        apellido1 = self.nombres_validacion('Ingresa el primer apellido\n')
        apellido2 = self.nombres_validacion('Ingresa el segundo apellido\n')
        fech_nac = self.nacimiento_validacion()
        carrera = self.carrera_validacion()
        
        asistente = [matricula, nombre, apellido1, apellido2, fech_nac, carrera]
        
        self.asistentes[matricula] = [matricula, nombre, apellido1, apellido2, fech_nac, carrera]  
        
        a = archivos()
        a.guardarAr(self.asistentes, 'asistentes.txt') 
        return asistente
    

  def consultar_asistente(self, prompt:str='Ingresa la matrícula del asistente a buscar: '):
      while True:
          matricula = self.matricula_validacion(prompt) 

          if matricula not in self.diccAsistentes:
              print(f'Error. No se encontró ningún asistente con la matrícula {matricula}. Intenta con otra matrícula.')
              continue
          else:
              return ", ".join(map(str, self.diccAsistentes[matricula]))


  def eliminar_asistente(self, prompt: str = '\nIngresa la matrícula del asistente que deseas eliminar\n'):
        while True:
            matricula = self.matricula_validacion(prompt)  # Assuming matricula_validacion is a method of the class
            if matricula not in self.diccAsistentes:
                print('Error. Matrícula no existe.')
                op1 = input('¿Deseas intentarlo con otra matrícula? S/N\n').upper()
                if op1 == 'N':
                    break
                continue
            else:
                print('\nAsistente encontrado')
                while True:
                    confirmacion = input('¿Deseas proseguir con la eliminación? S/N \n').upper()
                    if confirmacion == 'S': 
                        self.diccAsistentes.pop(matricula)
                        a = archivos()
                        a.eliminar('asistentes.txt', self.diccAsistentes)
                        print('\nAsistente eliminado con éxito.')
                        return
                    elif confirmacion == 'N':
                        print('\nNo se eliminó ningún asistente.')
                        return
                    else:
                        continue

  def modificar_asistente(self, prompt: str = 'Ingresa la matrícula del asistente que deseas modificar\n'):
    while True:
        matricula = self.matricula_validacion(prompt)  # Assuming matricula_validacion is a method of the class
        if matricula not in self.diccAsistentes:
            print('Error. Matrícula no existe.')
            op1 = input('¿Deseas intentarlo con otra matrícula? S/N\n').upper()
            if op1 == 'N':
                print('No se modificó ningún asistente')
                break
            continue
        else:
            # Podriamos preguntar cuales datos quiere modificar
            asistente = self.diccAsistentes[matricula]
            print(f'Datos actuales: {(", ").join(asistente)}')
            nombre = self.nombres_validacion('Ingresa el nombre\n')  # Assuming nombres_validacion is a method of the class
            apellido1 = self.nombres_validacion('Ingresa el primer apellido\n')
            apellido2 = self.nombres_validacion('Ingresa el segundo apellido\n')
            fech_nac = self.nacimiento_validacion()
            carrera = self.carrera_validacion()
            # asistencias = asistente[0][6]  # may be unnecessary
            self.diccAsistentes.update({matricula: [matricula, nombre, apellido1, apellido2, fech_nac, carrera]})
            a = archivos()
            a.modificar('asistentes.txt', self.diccAsistentes)
            print(f'\nAsistente exitosamente modificado.')
            break

  # --------------------------- CRUD CONFERENCIAS ---------------------------------
  # with open('registros.txt', 'a'):
  #     # No necesitas realizar ninguna operación dentro del bloque
  #     pass
  # r = archivos()

  # diccRegistros = r.leer('registros.txt')

  # with open('asistencias.txt', 'a'):
  #     # No necesitas realizar ninguna operación dentro del bloque
  #     pass
  # asis = archivos()
  # diccAsistencias = asis.leer('registros.txt')

  registros = {}
  asistencias = {}

  # VALIDACION
  # Se valida que se haya ingresado una conferencia valida

  def conferencia_validacion(self, prompt:int='Ingresa la conferencia\n'):
      while True:
          _conferencia=input(prompt)
          # Validar que no se omita
          if (_conferencia==''):
              print('Error. Se debe especificar una conferencia válida. Intenta de nuevo')
              continue
          # Validar que sea entero.
          try:
              conferencia=int(_conferencia)
          except:
              print('Error. Debe ser entero. Intenta de nuevo')
              continue
          # Validar que la conferencia exista
          if not (conferencia in self.conferencias):
              print('Error. Esa conferencia no existe. Intenta de nuevo')
              continue
          return conferencia


  # DISPONIBILIDAD DE CONFERENCIA
  # Después se evalúa si existen asientos disponibles
  def info_disponibilidad(self, conferencia_deseada: int = 'Ingresa la conferencia\n'):
      conferencia_deseada = self.conferencia_validacion(conferencia_deseada)  # Regresa el valor después de la validación, VALIDA SI EXISTE
      datos_conferencia = self.conferencias.get(conferencia_deseada, '')  # Obtienes los datos de la conferencia deseada, REGRESA LISTA
      nombre_auditorio = self.auditorios.get(datos_conferencia[3], '')[0]
      capacidad_auditorio = self.auditorios.get(datos_conferencia[3], '')[1]
      lugares_disponibles = capacidad_auditorio - datos_conferencia[4]
      print(f'\n{"*"*40}')
      print('Datos de la conferencia')
      print(f'\nConferencia: {datos_conferencia[1]}')
      print(f'Expositor: {datos_conferencia[2]}')
      print(f'Fecha: {datos_conferencia[0]}')
      print(f'Auditorio: {nombre_auditorio}')
      print(f'Lugares disponibles: {lugares_disponibles:,}')
      print(f'\n{"*"*40}')
      return lugares_disponibles
    
  contador_registros = 1

  # INSCRIPCIÓN
  # Se procede con la inscripción si la conferencia es válida y hay lugares disponibles
  def inscribir(self, prompt='Ingresa la conferencia a inscribir\n', prompt2='\nIngresa la matrícula del asistente\n'):
        with open('registros.txt', 'a'):
            # No necesitas realizar ninguna operación dentro del bloque
            pass
        r = archivos()

        diccRegistros = r.leer('registros.txt')

        with open('asistencias.txt', 'a'):
            # No necesitas realizar ninguna operación dentro del bloque
            pass
        asis = archivos()
        diccAsistencias = asis.leer('registros.txt')

        diccAsistentes = self.a.leer('asistentes.txt')  # assuming 'a' is an instance attribute of type 'archivos'
        while True:
            conferencia_destino = self.conferencia_validacion(prompt)
            asistente = self.matricula_validacion(prompt2)
            if asistente not in diccAsistentes:
                print('Error. No existe el asistente en la lista de asistentes.')
                op1 = input('¿Deseas intentarlo con otro asistente? S/N\n').upper()
                if op1 == 'N':
                    print('No se registro ningún asistencia.\n')
                    return
                else:
                    continue
            duplicado = False
            for registro in self.diccRegistros.values():
                if registro[0] == asistente and registro[1] == conferencia_destino:
                    print('Asistente ya registrado a esta conferencia.')
                    duplicado = True
            if duplicado:
                break

            ocupados = self.conferencias.get(conferencia_destino)
            ocupados[4] += 1

            self.diccRegistros[str(Acciones.contador_registros)] = [asistente, str(conferencia_destino)]
            Acciones.contador_registros += 1
            self.a.guardarAr(self.diccRegistros, 'registros.txt')
            print(f'Asistente {asistente} registrado a la conferencia {conferencia_destino}')
            print(self.diccRegistros)
            return conferencia_destino
  
  contador_asistencias = 1

  def confirmar_asistencia(self, prompt='Ingresa la conferencia\n', prompt2='Ingresa la matrícula del asistente\n'):
      while True:
          conferencia = self.conferencia_validacion(prompt)
          asistente = self.matricula_validacion(prompt2)
          if asistente not in self.diccAsistentes:
              print('Error. No existe el asistente en la lista de asistentes.')
              op1 = input('¿Deseas intentarlo de nuevo? S/N\n').upper()
              if op1 == 'N':
                  print('No se registro ningún asistencia.\n')
                  return
              else:
                  continue
          duplicado = False
          if not self.diccRegistros:
              print('La asistencia no se puede realizar porque no hay un registro previo a la conferencia.')
              return
          if not any(asistente == lista[0] for lista in self.diccRegistros.values()):
              print('No existe registro previo con esa matrícula.')
              return
          for asistencia in self.diccAsistencias.values():
              if asistencia[0] == asistente and asistencia[1] == conferencia:
                  print('Asistencia ya registrada a esta conferencia.')
                  duplicado = True
          if duplicado:
              break

          self.diccAsistencias[Acciones.contador_asistencias] = [asistente, str(conferencia)]
          self.asis.guardarAr(self.diccAsistencias, 'asistencias.txt')
          Acciones.contador_asistencias += 1
          print(f'Asistencia registrada a la conferencia {conferencia}')
          return conferencia
        

  def eliminar_registro_conferencia(self, prompt='Ingresa la conferencia\n', prompt2='\nIngresa la matrícula del asistente\n'):
      while True:
          conferencia = self.conferencia_validacion(prompt)
          asistente = self.matricula_validacion(prompt2)
          registros = self.diccRegistros
          for key, value in self.diccRegistros.items():
              if value[0] == str(asistente) and value[1] == str(conferencia):
                  print('Registro encontrado.')
                  while True:
                      confirmacion = input('¿Deseas proseguir con la eliminación? S/N \n').upper()
                      if confirmacion == 'S':
                          registros.pop(key)
                          self.r.eliminar('registros.txt', registros)
                          print('\nRegistro eliminado con éxito.')
                          return
                      elif confirmacion == 'N':
                          print('\nNo se eliminó ningún asistente.')
                          return
                      else:
                          continue
          print('\nRegistro no encontrado.')
          break
              

class Generales():

  def asientos_disponibles(self, conferencia_deseada: str = 'Ingresa la conferencia\n'):
        acciones = Acciones()  # Assuming Acciones is the name of the other class
        conferencia_deseada = acciones.conferencia_validacion(conferencia_deseada)
        datos_conferencia = acciones.conferencias.get(conferencia_deseada, '')
        capacidad_auditorio = acciones.auditorios.get(datos_conferencia[3], '')[1]
        lugares_disponibles = capacidad_auditorio - len(acciones.diccRegistros)
        return lugares_disponibles


  def conferencias_registradas_asistente(self, prompt: str = 'Ingresa la matrícula:\n'):
      while True:
          acciones = Acciones()  # Assuming Acciones is the name of the other class
          asistente = acciones.matricula_validacion(prompt)
          if not acciones.diccRegistros:
              print('No hay ninguna conferencia registrada en registros.')
              break
          coincidencias = False
          # Revisa coincidencias con matrícula
          for registro in acciones.diccRegistros.values():
              if registro[0] == asistente:
                  # Obtiene la información de la conferencia
                  conferencia_num = registro[1]
                  print(f'\nConferencia {conferencia_num}')
                  print(f'{acciones.conferencias[int(conferencia_num)]}')
                  coincidencias = True
          if coincidencias:
              break
          print('No hay ningún registro para este asistente.')
          break
          # accedes al diccionario de registro de la conferencia, agarras la matricula y muestras los datos de los asistentes registrados en un for

  def asistentes_registrados(self, prompt: str = 'Ingresa la conferencia\n'):
      contador_asistentes_registrados = 1
      while True:
          acciones = Acciones()  # Assuming Acciones is the name of the other class
          conferencia = acciones.conferencia_validacion(prompt)
          if not acciones.diccRegistros:
              print('No hay ningún asistente registrado a registro.')
              break
          coincidencias = False
          for registro in acciones.diccRegistros.values():
              if registro[1] == str(conferencia):
                  asistente = acciones.diccAsistentes[registro[0]]
                  print(f'Asistente {contador_asistentes_registrados}: {(", ").join(asistente)}')
                  contador_asistentes_registrados += 1
                  coincidencias = True
          if coincidencias:
              break
          print('No hay ningún registro para esta conferencia.')
          break
          # accedes al diccionario de registro de la conferencia, agarras la matricula y muestras los datos de los asistentes registrados en un for

  def constancia(self, asistente: str = '\nIngresa la matrícula del asistente\n'):
      acciones = Acciones()  # Assuming Acciones is the name of the other class
      # while True:
      asistente = acciones.matricula_validacion(asistente)
      contador_conferencias = 0
      for registro in acciones.diccRegistros.values():
          if registro[0] == asistente:
              contador_conferencias += 1
      if contador_conferencias == 3:
          print('Constancia de participación generada')
      else:
          print('No se generó la constancia de participación porque no cumple con 3 o más asistencias')

# EJECUCIÓN PRINCIPAL

accion = Acciones()
general = Generales()

while True: # Menú principal
    opcion_elegida=accion.mostrar_menu(accion.opciones_menu_principal, '\n** MENÚ PRINCIPAL\n')
    match opcion_elegida:
        case 'A': #'A':'Registrar un asistente'
            while True:
                opcion_elegida_asistente=accion.mostrar_menu(accion.opciones_menu_asistentes, '\n** MENÚ ASISTENTES\n')
                match opcion_elegida_asistente:
                    case 'A':
                        asistente_nuevo = accion.agregar_asistente()
                        print(f'Asistente agregado: {asistente_nuevo}')
                    case 'B':
                        accion.eliminar_asistente()
                    case 'C':
                        accion.modificar_asistente()
                    case 'D':
                        accion.consultar_asistente()
                    case 'X':
                        print('Regresando al menú principal...')
                        break
                    case _:
                        print('Opción no reconocida.')
                        continue
        case 'B': #    'B':'Registrar asistente a un evento',
            accion.inscribir() 
            print(f'Registros actuales:{accion.registros}')
        case 'C': #    'C':'Registrar asistencia al evento',
            accion.confirmar_asistencia()
            print(f'Asistencias actuales:{accion.asistencias}')
        case 'D': #    'D':'Ver eventos del alumno',
            general.conferencias_registradas_asistente()
        case 'E': #    'E':'Ver cantidad de asientos disponible',

            disponibles = general.asientos_disponibles()
            print(f'Asientos disponibles: {disponibles}')
        case 'F': #    'F':'Eliminar registro de asistente a evento',
            accion.eliminar_registro_conferencia()
        case 'G': # Consultar información conferencia
            accion.info_disponibilidad()
        case 'H':
            general.constancia()
        case 'I':
            general.asistentes_registrados()
        case 'X':
            print('Gracias por usar el sistema.')
            break
        case _:
            print('Opción no reconocida.')
            continue