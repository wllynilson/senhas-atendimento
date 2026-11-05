from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Senha:
    codigo: str
    tipo: str
    numero: int


class SistemaSenhas:
    """Sistema em memória para emissão e chamada de senhas."""

    def __init__(self) -> None:
        self._proximo_numero = 1
        self._aguardando: list[Senha] = []
        self._ultima_chamada: Senha | None = None

    def emitir_senha(self, tipo: str = "A") -> Senha:
        senha = Senha(codigo=f"{tipo}{self._proximo_numero:03d}", tipo=tipo, numero=self._proximo_numero)
        self._proximo_numero += 1
        self._aguardando.append(senha)
        return senha

    def chamar_proxima(self) -> Senha | None:
        if not self._aguardando:
            return None

        senha = self._aguardando.pop(0)
        self._ultima_chamada = senha
        return senha

    def painel(self) -> dict[str, object]:
        return {
            "ultima_chamada": self._ultima_chamada.codigo if self._ultima_chamada else None,
            "aguardando": [senha.codigo for senha in self._aguardando],
            "total_aguardando": len(self._aguardando),
        }


def _mostrar_ajuda() -> None:
    print("Comandos disponíveis: emitir [TIPO], chamar, painel, sair")


def main() -> None:
    sistema = SistemaSenhas()
    print("Sistema de senhas iniciado.")
    _mostrar_ajuda()

    while True:
        try:
            entrada = input("> ").strip()
        except EOFError:
            print()
            break

        if not entrada:
            continue

        partes = entrada.split()
        comando = partes[0].lower()

        if comando == "sair":
            break

        if comando == "emitir":
            tipo = partes[1].upper() if len(partes) > 1 else "A"
            senha = sistema.emitir_senha(tipo)
            print(f"Senha emitida: {senha.codigo}")
            continue

        if comando == "chamar":
            senha = sistema.chamar_proxima()
            if senha is None:
                print("Nenhuma senha aguardando chamada.")
            else:
                print(f"Chamando senha: {senha.codigo}")
            continue

        if comando == "painel":
            painel = sistema.painel()
            ultima_chamada = painel["ultima_chamada"] or "-"
            aguardando = ", ".join(painel["aguardando"]) or "-"
            print(f"Última chamada: {ultima_chamada}")
            print(f"Aguardando ({painel['total_aguardando']}): {aguardando}")
            continue

        _mostrar_ajuda()


if __name__ == "__main__":
    main()
