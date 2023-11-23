import re
from datetime import datetime

year_actual = datetime.now().year

# Representación de auditorios en un diccionario.
auditorios={
    'A': ['Gumersindo Cantú Hinojosa', 1000],
    'B': ['Víctor Gómez', 200],
    'C': ['Casas Alatriste', 150]
}

# CONFERENCIAS
# fecha y hora, nombre de conferencia, presentador, letra de auditorio, n asistentes registrados
conferencias={
    1:['04/11/2023 15:00','Inteligencia Artificial en los Negocios',
      'Dr. Alvaro Francisco Salazar', 'A', 0],
    2:['05/11/2023 09:00','Uso de la nube para gestión de procesos',
      'Dr. Manuel Leos','B',0],
    3:['05/11/2023 14:00','Industria 4.0 retos y oportunidades',
      'Dra. Monica Hernández','C',20],
    4:['05/11/2023 19:00','Machine Learning for a better world',
      'Dr. Janick Jameson','C',0],
    5:['06/11/2023 15:00','Retos de la Banca Electrónica en México',
      'Ing. Clara Benavides','A',0]
}

# Carreras
carreras={
    'LTI':'LICENCIADO EN TECNOLOGÍA DE LA INFORMACIÓN',
    'LA':'LICENCIADO EN ADMINISTRACIÓN',
    'CP':'CONTADOR PÚBLICO',
    'LNI':'LICENCIADO EN NEGOCIOS INTERNACIONALES',
    'LGRS':'LICENCIADO EN GESTIÓN DE RESPONSABILIDAD SOCIAL'
}

def elegir_letra(prompt:str='Dame una letra: ',
                opciones_validas:str='12345'):
        while True:
            opcion=input(prompt)
            opcion=opcion.upper()
            if (opcion==''):
                print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo')
                continue
            if not bool(re.match(f'^[{opciones_validas}]$',opcion)):
                print('Error en captura. Opción no reconocida. Inténtelo de nuevo')
                continue
            # Si todo fue bien, se sale.
            break
        return opcion
        
# print(elegir_letra('Select a letter: ', 'ABCDE'))

def mostrar_menu(
    opciones:dict,
    titulo:str='OPCIONES DISPONIBLES'):

    print(titulo)
    opciones_validas=''
    for k,v in opciones.items():
        print(f'[{k}] {v}')
        opciones_validas=f'{opciones_validas}{k}'
        # opciones_validas += k

    opc=elegir_letra('¿Qué opción deseas?: ', opciones_validas).upper()
    return opc
  
# print(mostrar_menu({'A':'Hola', 'B':'Adios'}))

# ------------ VALIDACIONES ASISTENTES ----------------------

def matricula_validacion(prompt:int='Ingresa la matrícula\n'):
    while True:
      _matricula = input(prompt)
      if _matricula == (''):
        print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo.')
        continue
      try:
        matricula = int(_matricula)
      except:
        print('Error en captura. Matrícula debe contener solo dígitos. Inténtelo de nuevo.')
        continue
      return _matricula    

def nombres_validacion(prompt:str='Ingresa un nombre\n'):
    while True:
      nombre = input(prompt)  # Se agarra el input que nosotros ingresamos al llamar la funcion
      if nombre == (''):
        print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo.')
        continue
      if not bool(re.match(r'^\D+$', nombre)):
        print('Error en captura. Solo se aceptan letras. Inténtelo de nuevo.')
        continue
      nombre = nombre.capitalize()
      return nombre
    
def nacimiento_validacion(prompt:str='Ingresa la fecha de nacimiento. DD/MM/YYYY\n'):
    while True:
      fecha = input(prompt)
      if fecha == (''):
        print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo.')
        continue
      if fecha in range(len(fecha)-1) not in '1234567890/':
        print('Error en captura. No se aceptan más que digitos y "/". Intenta de nuevo.')
      # if not bool(re.match(r'^(([0][1-9]|[1-2][0-9]|[3][01])/[\d]{2}/[\d]{4})$', fecha)):
      try:
        datetime.strptime(fecha, '%d/%m/%Y')  # Método para comprobar la estructura proporcionada
      except:
        print('Error en captura. La fecha no cumple con la estructura. Inténtelo de nuevo.')
        continue
      año_nacimiento = int(fecha[6::])
      if (year_actual - año_nacimiento) <= 14:
        print('Error. Año nacimiento no válido. Intenta de nuevo.')
        continue
      return fecha
      
def carrera_validacion(prompt:str='Ingresa las siglas de la carrera. LTI, LA, CP, LNI, LGRS\n'):
    while True:
      carrera = input(prompt)
      carrera = carrera.upper()
      if carrera == (''):
        print('Error en captura. Opción no se puede omitir. Inténtelo de nuevo.')
        continue
      if not bool(re.match(r'^(\D+)$', carrera)):
        print('Error en captura. Solo se aceptan letras. Inténtelo de nuevo.')
        continue
      if carrera not in carreras:
        print('Error. Carrera no válida. Inténtalo de nuevo.')
        continue
      return carrera

contador_asistentes = 1
asistentes = {'2080014':['2080014', 'Juan', 'P', 'M', '06/02/2002', 'LTI']}


# --------------------------- CRUD ASISTENTES ---------------------------------
# Agregar asistentes
def agregar_asistente():
    # global contador_asistentes
    # global asistentes
    while True:
      matricula = matricula_validacion()
      if matricula in asistentes:
        print('Error. Matrícula ya registrada. Intenta con una nueva matrícula.')
        continue    
      break
    nombre = nombres_validacion('Ingresa el nombre\n')
    apellido1 = nombres_validacion('Ingresa el primer apellido\n')
    apellido2 = nombres_validacion('Ingresa el segundo apellido\n')
    fech_nac = nacimiento_validacion()
    carrera = carrera_validacion()
    # asistencias = 0
    
    asistente = [matricula, nombre, apellido1, apellido2, fech_nac, carrera]
    
    # asistentes[contador_asistentes]=asistente
    asistentes[matricula] = [matricula, nombre, apellido1, apellido2, fech_nac, carrera]   
    # contador_asistentes += 1
    return asistente
  
# asistente_nuevo = agregar_asistente()
# print(f'Asistente agregado: {asistente_nuevo}')


def eliminar_asistente(prompt:int='\nIngresa la matrícula del asistente que deseas eliminar\n'):
    while True:
      matricula = matricula_validacion(prompt)
      if matricula not in asistentes:
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
            asistentes.pop(matricula)
            print('\nAsistente eliminado con éxito.')
            return
          elif confirmacion == 'N':
            print('\nNo se eliminó ningún asistente.')
            return
          else:
            continue
          
def modificar_asistente(prompt:int='Ingresa la matrícula del asistente que deseas modificar\n'):
    while True:
      matricula = matricula_validacion(prompt)
      if matricula not in asistentes:
        print('Error. Matrícula no existe.')
        op1 = input('¿Deseas intentarlo con otra matrícula? S/N\n').upper()
        if op1 == 'N':
          print('No se modificó ningún asistente')
          break
        continue
      else:
        # Podriamos preguntar cuales datos quiere modificar
        asistente = asistentes[matricula]
        print(f'Datos actuales: {(", ").join(asistente)}')
        nombre = nombres_validacion('Ingresa el nombre\n')
        apellido1 = nombres_validacion('Ingresa el primer apellido\n')
        apellido2 = nombres_validacion('Ingresa el segundo apellido\n')
        fech_nac = nacimiento_validacion()
        carrera = carrera_validacion()
        # asistencias = asistente[0][6]  # may be unnecessary
        asistentes.update({matricula:[matricula, nombre, apellido1, apellido2, fech_nac, carrera]})
        print(f'\nAsistente exitosamente modificado.')
        break

      
def consultar_asistente(prompt:int='Ingresa la matrícula del asistente a buscar\n'):
    while True:
      matricula = matricula_validacion(prompt)
      if matricula not in asistentes:
        print('Error. Matrícula no existe.')
        op1 = input('¿Deseas intentarlo con otra matrícula? S/N\n').upper()
        if op1 == 'N':
          print('No se hizo ninguna consulta')
          break
        continue
      else:
        asistente = asistentes.get(matricula)
        print(f'\n{"*"*40}')
        print('Datos del asistente\n')
        print(f'Matrícula:              {asistente[0]}')
        print(f'Nombre:                 {asistente[1]}')
        print(f'Apellido paterno:       {asistente[2]}')
        print(f'Apellido materno:       {asistente[3]}')
        print(f'Fecha de nacimiento:    {asistente[4]}')
        print(f'Carrera:                {asistente[5]}')
        # print(f'Asistencias eventos:    {asistente[6]}')
        print(f'\n{"*"*40}')
        return asistente


# Menus
opciones_menu_principal={
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

opciones_menu_asistentes={
    'A':'Agregar un asistente',
    'B':'Eliminar asistente',
    'C':'Actualizar datos del asistente',
    'D':'Consultar asistente',
    'X':'Regresar al menú principal\n'
}


# --------------------------- CRUD CONFERENCIAS ---------------------------------

registros = {}
asistencias = {}

contador_registros = 1
contador_asistencias = 1

# VALIDACION
# Se valida que se haya ingresado una conferencia valida
def conferencia_validacion(prompt:int='Ingresa la conferencia\n'):
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
        if not (conferencia in conferencias):
            print('Error. Esa conferencia no existe. Intenta de nuevo')
            continue
        return conferencia


# DISPONIBILIDAD DE CONFERENCIA
# Después se evalúa si existen asientos disponibles
def info_disponibilidad(conferencia_deseada:int='Ingresa la conferencia\n'):
    conferencia_deseada = conferencia_validacion(conferencia_deseada) # Regresa el valor después de la validación, VALIDA SI EXISTE
    datos_conferencia=conferencias.get(conferencia_deseada,'') # Obtienes los datos de la conferencia deseada, REGRESA LISTA
    nombre_auditorio=auditorios.get(datos_conferencia[3],'')[0]
    capacidad_auditorio=auditorios.get(datos_conferencia[3],'')[1]
    lugares_disponibles=capacidad_auditorio-datos_conferencia[4]
    print(f'\n{"*"*40}')
    print('Datos de la conferencia')
    print(f'\nConferencia: {datos_conferencia[1]}')
    print(f'Expositor: {datos_conferencia[2]}')
    print(f'Fecha: {datos_conferencia[0]}')
    print(f'Auditorio: {nombre_auditorio}')
    print(f'Lugares disponibles: {lugares_disponibles:,}')
    print(f'\n{"*"*40}')
    return lugares_disponibles

# INSCRIPCIÓN
# Se procede con la inscripción si la conferencia es válida y hay lugares disponibles
def inscribir(prompt:int='Ingresa la conferencia a inscribir\n', prompt2:int='\nIngresa la matrícula del asistente\n'):
    global contador_registros
    while True:
        conferencia_destino = conferencia_validacion(prompt)
        asistente = matricula_validacion(prompt2)
        if asistente not in asistentes:
            print('Error. No existe el asistente en la lista de asistentes.')
            op1 = input('¿Deseas intentarlo con otro asistente? S/N\n').upper()
            if op1 == 'N':
              print('No se registro ningún asistencia.\n')
              return
            else:
              continue
        duplicado = False
        for registro in registros.values():
            if registro[0] == asistente and registro[1] == conferencia_destino:
                print('Asistente ya registrado a esta conferencia.') 
                duplicado = True
        if duplicado:
            break
        
        # Agregado
        ocupados = conferencias.get(conferencia_destino)
        ocupados[4] += 1
        registros[contador_registros] = [asistente, conferencia_destino]
        contador_registros+=1

        print(f'Asistente {asistente} registrado a la conferencia {conferencia_destino}')
        return conferencia_destino


def confirmar_asistencia(prompt:int='Ingresa la conferencia\n', prompt2:int='Ingresa la matrícula del asistente\n'):
    global contador_asistencias
    while True:
        conferencia = conferencia_validacion(prompt)
        asistente = matricula_validacion(prompt2)
        if asistente not in asistentes:
            print('Error. No existe el asistente en la lista de asistentes.')
            op1 = input('¿Deseas intentarlo de nuevo? S/N\n').upper()
            if op1 == 'N':
              print('No se registro ningún asistencia.\n')
              return 
            else:
              continue
        duplicado = False
        # Valida que haya un registro previo
        if not registros:
            print('La asistencia no se puede realizar porque no hay un registro previo a la conferencia.')
            return
        for registro in registros.values():
          if asistente == registro[0]:
            break
          else:
            print('No existe registro previo con esa matrícula.')
            return            
        for asistencia in asistencias.values():
            if asistencia[0] == asistente and asistencia[1] == conferencia:
                print('Asistencia ya registrada a esta conferencia.') 
                duplicado = True
        if duplicado:
            break
        
        # Agregado
        asistencias[contador_asistencias] = [asistente, conferencia]
        contador_asistencias+=1
        print(f'Asistencia registrada a la conferencia {conferencia}')
        return conferencia
      

def eliminar_registro_conferencia(prompt:int='Ingresa la conferencia\n', prompt2:int='\nIngresa la matrícula del asistente\n'):
    while True:
          conferencia = conferencia_validacion(prompt)
          asistente = matricula_validacion(prompt2)
          for key, value in registros.items():
            if value[0] == asistente and value[1] == conferencia:
                print('Registro encontrado.')
                while True:
                  confirmacion = input('¿Deseas proseguir con la eliminación? S/N \n').upper()
                  if confirmacion == 'S': 
                    registros.pop(key)
                    print('\nRegistro eliminado con éxito.')
                    return
                  elif confirmacion == 'N':
                    print('\nNo se eliminó ningún asistente.')
                    return
                  else:
                    continue  
          print('\nRegistro no encontrado.')
          break
            
# ----   GENERALES  ----------------#
def asientos_disponibles(conferencia_deseada:int='Ingresa la conferencia\n'):
    conferencia_deseada = conferencia_validacion(conferencia_deseada) # Regresa el valor después de la validación, VALIDA SI EXISTE
    datos_conferencia=conferencias.get(conferencia_deseada,'') # Obtienes los datos de la conferencia deseada, REGRESA LISTA
    capacidad_auditorio=auditorios.get(datos_conferencia[3],'')[1]
    lugares_disponibles=capacidad_auditorio-datos_conferencia[4]
    return lugares_disponibles


def conferencias_registradas_asistente(prompt:int='Ingresa la matrícula:\n'):
    while True:
          asistente = matricula_validacion(prompt)
          if not registros:
            print('No hay ninguna conferencia registrada en registros.')
            break
          coincidencias = False
          # Revisa coincidencias con matrícula
          for registro in registros.values():
            if registro[0] == asistente:
              # Obtiene la información de la conferencia
              conferencia_num = registro[1]
              print(f'\nConferencia {conferencia_num}')
              print(f'{conferencias[conferencia_num]}')
              coincidencias = True
          if coincidencias:
            break
          print('No hay ningún registro para este asistente.')
          break
          # accedes al diccionario de registro de la conferencia, agarras la matricula y muestras los datos de los asistentes registrados en un for


def asistentes_registrados(prompt:int='Ingresa la conferencia\n'):
    contador_asistentes_registrados = 1
    while True:
          conferencia = conferencia_validacion(prompt)
          if not registros:
            print('No hay ningún asistente registrado a registros.')
            break
          coincidencias = False
          for registro in registros.values():
            if registro[1] == conferencia:
              asistente = asistentes[registro[0]]
              print(f'Asistente {contador_asistentes_registrados}: {(", ").join(asistente)}')
              contador_asistentes_registrados += 1
              coincidencias = True
          if coincidencias:
            break
          print('No hay ningún registro para esta conferencia.')
          break
          # accedes al diccionario de registro de la conferencia, agarras la matricula y muestras los datos de los asistentes registrados en un for

def constancia(asistente:int='\nIngresa la matrícula del asistente\n'):
    # while True:
        asistente = matricula_validacion(asistente)
        contador_conferencias = 0
        for asistencia in asistencias.values():
          if asistencia[0] == asistente:
              contador_conferencias += 1
        if contador_conferencias == 3:
          print('Constancia de participación generada')
        else:
          print('No se generó la constancia de participación porque no cumple con 3 o más asistencias')



# EJECUCIÓN PRINCIPAL

while True: # Menú principal
    opcion_elegida=mostrar_menu(opciones_menu_principal, '\n** MENÚ PRINCIPAL\n')
    match opcion_elegida:
        case 'A': #'A':'Registrar un asistente'
            while True:
                opcion_elegida_asistente=mostrar_menu(opciones_menu_asistentes, '\n** MENÚ ASISTENTES\n')
                match opcion_elegida_asistente:
                    case 'A':
                        asistente_nuevo = agregar_asistente()
                        print(f'Asistente agregado: {asistente_nuevo}')
                    case 'B':
                        eliminar_asistente()
                    case 'C':
                        modificar_asistente()
                    case 'D':
                        consultar_asistente()
                    case 'X':
                        print('Regresando al menú principal...')
                        break
                    case _:
                        print('Opción no reconocida.')
                        continue
        case 'B': #    'B':'Registrar asistente a un evento',
            # inscribir() # = asistente, conferencia 
            inscribir() 
            print(f'Registros actuales:{registros}')
        case 'C': #    'C':'Registrar asistencia al evento',
            confirmar_asistencia()
            print(f'Asistencias actuales:{asistencias}')
        case 'D': #    'D':'Ver eventos del alumno',
            conferencias_registradas_asistente()
        case 'E': #    'E':'Ver cantidad de asientos disponible',
            disponibles = asientos_disponibles()
            print(f'Asientos disponibles: {disponibles}')
        case 'F': #    'F':'Eliminar registro de asistente a evento',
            eliminar_registro_conferencia()
        case 'G': # Consultar información conferencia
            info_disponibilidad()
        case 'H':
            constancia()
        case 'I':
            asistentes_registrados()
        case 'X':
            print('Gracias por usar el sistema.')
            break
        case _:
            print('Opción no reconocida.')
            continue