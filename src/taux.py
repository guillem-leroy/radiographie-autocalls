def facteur_actualisation(r: float, T: float) -> float:
    """
    Facteur d'actualisation DF(T) = 1 / (1 + r)^T.

    r : taux annuel, en décimal (0.02 pour 2 %)
    T : maturité, en années
    """

    return 1/(1+r)**T