from models.boa_Constrictor  import Boa_Constrictor
from models.huron import Huron
 
class Guarderia:
    def __init__(self):
       self.huron1 = Huron("Huron de  colombia ",2.3, 3, 5, "Australia", 17)
       self.huron2 = Huron("Huron de argentina",1.7, 2, 2, "Suiza", 28)
       self.boa1 = Boa_Constrictor("Boa Constrictor de Colombiana ", 38.0, 7, 15, "Brasil", 75.0)
       self.boa2 = Boa_Constrictor("Boa Constrictor de Brasil ", 15.0, 3, 10, "Colombia", 60.0)
 
    def alimentar_boa(self, boa: Boa_Constrictor):
        if boa is None:
            return "¡Esta Boa no existe!"
        
        try:
            boa.comer_ratones()
            return "¡Éxito!"
        except ValueError:
            return "¡La boa está llena!"
 