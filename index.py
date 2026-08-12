class Ambiente:
    def __init__(self, celulas):
        self.celulas = list(celulas)
        self.position = 0
        self.consumo = 0

    def notion(self):
        return {
            "sujo": self.celulas[self.position],
            "parede_direita": self.position == len(self.celulas) - 1,
            "parede_esquerda": self.position == 0
        }

    def execution(self, acao):
        self.consumo += 1

        if acao == "limpar":
            self.celulas[self.position] = False

        elif acao == "mover_direita":
            if self.position < len(self.celulas) - 1:
                self.position += 1

        elif acao == "mover_esquerda":
            if self.position > 0:
                self.position -= 1

    def desempenho(self):
        limpas = sum(1 for c in self.celulas if not c)
        return limpas * 10 - self.consumo


def agente_simples(percepcao):
    if percepcao["sujo"]:
        return "limpar"

    if percepcao["parede_direita"]:
        return "mover_esquerda"

    return "mover_direita"


if __name__ == "__main__":
    ambiente = Ambiente([True, False, True, True, False])

    for passo in range(20):
        percepcao = ambiente.notion()
        acao = agente_simples(percepcao)

        ambiente.execution(acao)

        print(
            f"Passo {passo}: "
            f"{percepcao}, {acao}, "
            f"{ambiente.desempenho()}"
        )

    print(f"Desempenho final: {ambiente.desempenho()}")
