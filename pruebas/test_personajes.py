
import pytest

from personajes import Personaje, Guerrero, Mago, Arquero, Enemigo
from combate import Combate


def test_guerrero_ataca():
    jugador = Guerrero("Arthas", 100, 30)
    enemigo = Enemigo("Orco", 100, 15)

    danio = jugador.atacar(enemigo)

    assert danio == 30
    assert enemigo.vida == 70


def test_mago_tiene_bono_de_ataque():
    mago = Mago("Gandalf", 80, 40)
    enemigo = Enemigo("Orco", 100, 15)

    danio = mago.atacar(enemigo)

    assert danio == 45
    assert enemigo.vida == 55


def test_arquero_tiene_bono_de_ataque():
    arquero = Arquero("Legolas", 80, 40)
    enemigo = Enemigo("Orco", 100, 15)

    danio = arquero.atacar(enemigo)

    assert danio == 42
    assert enemigo.vida == 58


def test_la_vida_no_puede_ser_negativa():
    jugador = Guerrero("Arthas", 100, 30)

    jugador.recibir_danio(150)

    assert jugador.vida == 0
    assert jugador.esta_vivo() is False


def test_curacion_no_supera_vida_maxima():
    jugador = Guerrero("Arthas", 100, 30)

    jugador.recibir_danio(20)
    jugador.curar(50)

    assert jugador.vida == 100


def test_no_se_puede_instanciar_personaje_abstracto():
    with pytest.raises(TypeError):
        Personaje("Personaje", 100, 20)


def test_no_se_puede_usar_pocion_si_no_quedan():
    jugador = Guerrero("Arthas", 100, 30)
    enemigo = Enemigo("Orco", 100, 15)
    combate = Combate(jugador, enemigo)

    combate.pociones = 0

    mensaje = combate.usar_pocion()

    assert mensaje == "No tienes más pociones."
