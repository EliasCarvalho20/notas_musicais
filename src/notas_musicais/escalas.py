NOTAS = "C C# D D# E F F# G G# A A# B".split()
ESCALAS = {"maior": (0, 2, 4, 5, 7, 9, 11), "menor": (0, 2, 3, 5, 7, 8, 10)}


def escala(tonica: str, tonalidade: str) -> dict[str, list[str]]:
    """
    Gera uma escala apartir de uma tônica e uma tonalidade.

    Args:
        tonica: Nota que será a tônica da escala
        tonalidade: Tonialidade da escala

    Returns:
        Um dicionário com as notas da escala e os graus.

    Examples:
        >>> escala('C', 'maior')
        {'notas': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> escala('a', 'menor')
        {'notas': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'graus': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    intervalos = ESCALAS[tonalidade]
    tonica_pos = NOTAS.index(tonica)

    temp = [NOTAS[(tonica_pos + i) % 12] for i in intervalos]
    return {"notas": temp, "graus": ["I", "II", "III", "IV", "V", "VI", "VII"]}
