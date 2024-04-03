from Clase import *
import os.path
import pickle


def validar_rango(men, may, msj):
    num = int(input(msj))
    if num < men or num > may:
        print(f'Debe ingresar un número en el rango de [{men},{may}]')
        num = input(msj)
    return num


def crear_archivo_auto(tf, bf):
    if os.path.exists(tf):
        mt = open(tf, "rt")
        mt.readline()
        mt.readline()
        mb = open(bf, "wb")
        while True:
            ln = mt.readline()
            if ln == "":
                break
            tokens = ln.split(",")
            cod = int(tokens[0])
            pat = tokens[1]
            tiv = int(tokens[2])
            fop = int(tokens[3])
            pic = int(tokens[4])
            dis = int(tokens[5])
            tik = Ticket(cod, pat, tiv, fop, pic, dis)
            pickle.dump(tik, mb)
        mt.close()
        mb.close()
        print("\n...El archivo se ha cargado con exito...")
    else:
        print("El archivo", tf, "no existe...")


def crear_registro():
    codigo = validar_rango(0, 100000000, "Ingresar el código del ticket: ")
    patente = input("Ingresar la patente del vehículo: ").upper().strip()
    tipo = validar_rango(0, 2, "Ingresar el tipo de vehiculo (0, 1, 2) : ")
    forma_de_pago = validar_rango(1, 2, "Ingresar la forma de pago (1 o 2): ")
    pais_cabina = validar_rango(0, 4, "Ingresar el pais de la cabina (entre 0 y 4): ")
    km_recorridos = validar_rango(0, 1000, "Ingresar la cantidad de kilometros recorridos: ")
    return Ticket(codigo, patente, tipo, forma_de_pago, pais_cabina, km_recorridos)


def carga_manual_archivo(bf):
    if not os.path.exists(bf):
        archivo_binario = open(bf, "wb")
        ticket = crear_registro()
        pickle.dump(ticket, archivo_binario)
        archivo_binario.close()
        print("\nTiket agregado correctamente")
    else:
        ticket = crear_registro()
        mb = open(bf, "ab")
        pickle.dump(ticket, mb)
        mb.close()
        print("\nTiket agregado correctamente")


def mostrar_archivo(bf):
    if os.path.exists(bf):
        archivo = open(bf, "rb")
        tam = os.path.getsize(bf)
        print(mostrar_encabezado())
        while archivo.tell() < tam:
            r = pickle.load(archivo)
            print(r)
        archivo.close()
    else:
        print('El archivo', bf, 'no existe, use otra opción para grabar tickets.')
        print()


def filtrar_patentes(bf, m, p):
    contador = 0
    if not os.path.exists(bf):
        print('El archivo', bf, 'no existe, use otra opción para grabar tickets.')
        print()
        return
    tbm = os.path.getsize(bf)
    print('\nLISTADO DE TICKETS CORRESPONDIENTES A LA PATENTE: ' + str(p))
    while m.tell() < tbm:
        ticket = pickle.load(m)
        if ticket.patente == p:
            contador += 1
            print(f'{"_"*134}')
            print(ticket)
    print("La catidad de registros mostrados es: ", contador)
    print()
    m.close()


def buscar_codigo(bf, m, c):
    t = os.path.getsize(bf)
    while m.tell() < t:
        ticket = pickle.load(m)
        if ticket.codigo == c:
            m.close()
            return ticket
    m.close()


def matriz_conteo(bf):
    tipos_v, p_cabinas = 3, 5
    m_conteo = [[0] * p_cabinas for _ in range(tipos_v)]
    t = os.path.getsize(bf)
    m = open(bf, "rb")
    while m.tell() < t:
        ticket = pickle.load(m)
        tipo = ticket.tipo
        cabina = ticket.pais_cabina
        m_conteo[tipo][cabina] += 1
    m.close()
    return m_conteo


def mostrar_matriz_conteo(bf):
    m_conteo = matriz_conteo(bf)
    tipos_vehiculo = ("Motocicleta", "Automóvil", "Camión")
    cabinas = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay")
    for tipo in range(3):
        for cabina in range(5):
            if m_conteo[tipo][cabina] != 0:
                print(f'{tipo}.{tipos_vehiculo[tipo]:<20} | {cabina}.{cabinas[cabina]:<20} | '
                      f'{m_conteo[tipo][cabina]:^20}\n{"-"*70:<70}')


def totalizar_cabinas_tipo(bf):
    tipos_vehiculo = ("Motocicleta", "Automóvil", "Camión")
    cabinas = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay")
    m_conteo = matriz_conteo(bf)
    total_tipos = [0] * 3
    total_cabinas = [0] * 5
    for i in range(3):
        for j in range(5):
            total_tipos[i] += m_conteo[i][j]
    for j in range(5):
        for i in range(3):
            total_cabinas[j] += m_conteo[i][j]
    print('\nTOTAL TICKETS POR TIPO DE VEHICULO:')
    for tipo in range(3):
        print(f'{tipo}.{tipos_vehiculo[tipo]}: {total_tipos[tipo]}')
    print('\nTOTAL DE TICKETS POR PAÍS DE CABINA:')
    for cabina in range(5):
        print(f'{cabina}.{cabinas[cabina]}: {total_cabinas[cabina]}')


def calcular_promedio_distancias(fd):
    total_distancia = 0
    num_registros = 0
    mb = open(fd, "rb")
    while True:
        ticket = pickle.load(mb)
        total_distancia += ticket.km_recorridos
        num_registros += 1
        position = mb.tell()
        next_byte = mb.read(1)
        if not next_byte:
            break
        mb.seek(position)
    mb.close()
    promedio = total_distancia / num_registros
    return promedio


def crear_vector_mayores_promedio(fd):
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        return
    x = calcular_promedio_distancias(fd)
    m = open(fd, 'rb')
    v = []
    t = os.path.getsize(fd)
    while m.tell() < t:
        ticket = pickle.load(m)
        if ticket.km_recorridos > x:
            v.append(ticket)
    m.close()
    return v


def shell_sort(v):
    n = len(v)
    h = 1
    while h <= n // 9:
        h = 3*h + 1
    while h > 0:
        for j in range(h, n):
            y = v[j]
            k = j - h
            while k >= 0 and v[k].km_recorridos > y.km_recorridos:
                v[k+h] = v[k]
                k -= h
            v[k+h] = y
        h //= 3
