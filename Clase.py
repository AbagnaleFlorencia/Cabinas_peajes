class Ticket:
    def __init__(self, codigo, patente, tipo, forma_de_pago, pais_cabina, km_recorridos):
        self.codigo = codigo
        self.patente = patente
        self.tipo = tipo
        self.forma_de_pago = forma_de_pago
        self.pais_cabina = pais_cabina
        self.km_recorridos = km_recorridos
        self.det_patente = self.detectar_pais_por_patente()
        self.total = self.calcular_importe_final()

    def __str__(self):
        tipos_vehiculo = ("Motocicleta", "Automóvil", "Camión")
        formas_pago = ("Manual", "Telepeaje")
        cabinas = ("Argentina", "Bolivia", "Brasil", "Paraguay", "Uruguay")
        return f'|{self.codigo:^12} | {self.patente:^15} | {self.det_patente:^18} | {self.tipo}.' \
               f'{tipos_vehiculo[self.tipo]:<13} | {self.forma_de_pago}.{formas_pago[self.forma_de_pago - 1]:<12} | ' \
               f'{self.pais_cabina}.{cabinas[self.pais_cabina]:<14} | {self.km_recorridos:<10} | ${self.total:<10}|' \
               f'\n{"_"*134}'

    def detectar_pais_por_patente(self):
        pat = self.patente
        lp = len(pat)
        if lp < 6 or lp > 7:
            return "Otro"
        if lp == 6:
            if pat[0:4].isalpha() and pat[4:6].isdigit():
                return "Chile"
            else:
                return "Otro"
        if pat[0:2].isalpha() and pat[2:5].isdigit() and pat[5:7].isalpha():
            return "Argentina"
        if pat[0:2].isalpha() and pat[2:7].isdigit():
            return "Bolivia"
        if pat[0:3].isalpha() and pat[3].isdigit() and pat[4].isalpha() and pat[5:7].isdigit():
            return "Brasil"
        if pat[0:4].isalpha() and pat[4:7].isdigit():
            return "Paraguay"
        if pat[0:3].isalpha() and pat[3:7].isdigit():
            return "Uruguay"
        return "Otro"

    def calcular_importe_final(self):
        if self.pais_cabina == 2:
            importe_base = 400
        elif self.pais_cabina == 1:
            importe_base = 200
        else:
            importe_base = 300
        if self.tipo == 0:
            importe_basico = importe_base * 0.5
        elif self.tipo == 2:
            importe_basico = importe_base * 1.6
        else:
            importe_basico = importe_base
        if self.forma_de_pago == 2:
            importe_final = importe_basico * 0.9
        else:
            importe_final = importe_basico

        return importe_final


def mostrar_encabezado():
    sep = '=' * 134
    cadena = f'| {"Codigo":^10} | {"Patente":^15} | {"País de la Patente":^10} | ' \
             f'{"Tipo de Vehículo":^10} | {"Forma de Pago":^10} | {"País de la Cabina":^10} |{"Kilometros":^5} ' \
             f'| {"Importe":^10}  |\n{sep:<100}'
    titulo = f'{sep:<150}\n|{"TICKET":^132}|\n{sep:<150}\n{cadena:<100}'
    return titulo
