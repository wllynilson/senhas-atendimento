# senhas-atendimento

Sistema para organizar senhas de filas de atendimento: emissão, chamada e painel de acompanhamento.

## Como executar

```bash
python senhas_atendimento.py
```

Comandos no terminal interativo:

- `emitir [TIPO]`: emite uma senha (ex.: `emitir P`)
- `chamar`: chama a próxima senha da fila
- `painel`: mostra última senha chamada e as senhas aguardando
- `sair`: encerra o sistema

## Testes

```bash
python -m unittest discover -s tests
```
