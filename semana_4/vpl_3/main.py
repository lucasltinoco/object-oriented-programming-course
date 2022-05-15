from cachorro import Cachorro
from gato import Gato
from canarinho import Canarinho

cao = Cachorro()
print(cao.mover())
print(cao.produzir_som())
print(cao.latir())

gato = Gato()
print(gato.mover())
print(gato.produzir_som())
print(gato.miar())

canarinho = Canarinho(2, 3)
print(canarinho.mover())
print(canarinho.produzir_som())
print(canarinho.cantar())
