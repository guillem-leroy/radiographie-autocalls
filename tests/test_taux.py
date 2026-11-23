import pytest
from src.taux import facteur_actualisation

def test_maturite_zero():
    # 1 € reçu aujourd'hui vaut 1 € aujourd'hui
    assert facteur_actualisation(0.02, 0) == 1.0
def test_taux_nul():
    # avec un taux nul, attendre ne coûte rien
    assert facteur_actualisation(0, 5) == 1.0
def test_valeur_connue():
    # DF(2) avec r = 2 %, calculé à la main dans l'exercice
    assert facteur_actualisation(0.02,2) == pytest.approx(0.9611, abs=1e-4)