class TransporteUrbano:
    def __init__(self, tipo, marca, modelo):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo

    def presentar_informacion(self):
        return f"Tipo: {self.tipo}, Marca: {self.marca}, Modelo: {self.modelo}"
transportes = [
        TransporteUrbano('Bus', 'Mercedes-Benz', 'Citaro'),
        TransporteUrbano('Tranvía', 'Siemens', 'S70'),
        TransporteUrbano('Autobús', 'Volvo', '7900'),
        TransporteUrbano('Tren Ligero', 'Bombardier', 'Flexity Swift'),
        TransporteUrbano('Metro', 'Alstom', 'MP 14'),
        TransporteUrbano('Trolebús', 'Solaris', 'T12'),
        TransporteUrbano('Minibús', 'Ford', 'Transit'),
        TransporteUrbano('Taxi', 'Toyota', 'Prius'),
        TransporteUrbano('Monorraíl', 'Hitachi', 'Monorail 200'),
        TransporteUrbano('Funicular', 'Doppelmayr', 'FGT'),
        TransporteUrbano('Bicicleta Pública', 'Bixi', 'Classic'),
        TransporteUrbano('Scooter Eléctrico', 'Lime', 'S-Scooter'),
        TransporteUrbano('Patineta Eléctrica', 'Boosted', 'Stealth'),
        TransporteUrbano('Bicitaxi', 'Pedicab', 'Cycle Rickshaw'),
        TransporteUrbano('Cablebús', 'Leitner', 'Poma 2000'),
        TransporteUrbano('Autobús Articulado', 'MAN', 'Lions City G'),
        TransporteUrbano('Tren Subterráneo', 'Siemens', 'Inspiro'),
        TransporteUrbano('Camión de Basura', 'Dennis Eagle', 'Elite 2'),
        TransporteUrbano('Barca de Transporte', 'Damen', 'Fast Ferry'),
        TransporteUrbano('Ferrocarril de Cercanías', 'CAF', 'Civia'),
]