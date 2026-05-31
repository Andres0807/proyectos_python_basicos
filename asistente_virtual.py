import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#opciones de voz / idioma
id1 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-MX_SABINA_11.0"
id2 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
id3 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0"
id4 = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0"


#Escuchar nuestro microfono y devolver el audio como texto
def tranformar_audio_en_texto():

    #Alamcenar recognizer en variable
    r = sr.Recognizer()

    #Configurar el microfono
    with sr.Microphone() as origen:

        #Tiempo de espera
        r.pause_threshold = 0.8

        #Informar que comenzo la grabacion
        print("Ya puedes hablar")

        #Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #Buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            #prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            #Devolver pedido
            return pedido

        #En caso de que no comprenda el audio
        except sr.UnknownValueError:

            #Prueba de que no comprendió el audio
            print("Ups... No entendí")

            #Devolver error
            return "Sigo esperando"

        #En caso de no resolver el pedido
        except sr.RequestError:

            # Prueba de que no comprendió el audio
            print("Ups... No hay servicio")

            # Devolver error
            return "Sigo esperando"

        #Error inesperado
        except:

            # Prueba de que no comprendió el audio
            print("Ups... Algo ha salido mal")

            # Devolver error
            return "Sigo esperando"


#Funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    #Encender el motor pyttsx3
    engine = pyttsx3.init()
    engine.setProperty(
        "voice",
        id3)

    #Pronunaciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#Informar el dia de la semana
def pedir_dia():

    #Crear la variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    #Crear una variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    #Diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    #Decir el día de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

#Informar que hora es
def pedir_hora():

    #Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos.'
    print(hora)

    #Decir la hora
    hablar(hora)

#Funcion saludo inicial
def saludo_inicial():

    #Crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'buenas noches'
    elif 6 <= hora.hour <= 13:
        momento = 'buen día'
    else:
        momento = 'buenas noches'

    #decir el saludo
    hablar(f'Hola Juan, {momento} , soy tu asistente virtual. Por favor dime en que te puedo ayudar.')

#Funcion central del asistente
def pedir_cosas():

    #Activar saludo inicial
    saludo_inicial()

    #Variable de corte
    comenzar = True

    #loop central
    while comenzar:

        #Activar el micro y guardar el pedido en un string
        pedido = tranformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo YouTube')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'abrir el navegador' in pedido:
            hablar('Con gusto, estoy abriendo Navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Con gusto, estoy buscando en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Con gusto, estoy buscando en internet')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Ya estoy reproduciendo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke(language='es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL',
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['RegularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


pedir_cosas()