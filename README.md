# inspersec-gh-aula1

## Instruções

1. Clone o repositório
1. Instale os pacotes necessarios usando o .bat
1. Instale o [AssaultCube](https://assault.cubers.net/)
1. Instale o [Cheat Engine](https://www.cheatengine.org/)


## Walkthrough

### Estrutura do jogo

```
Jogo.exe -> Memoria -> Player -> Instancias do player
```

- O que queremos fazer eh pegar o ponteiro do player e alterar o valor da vida dele, para isso precisamos caminha pela memoria para achar onde o player esta localizado dentro dela

### Passo a passo

Pegue o ponteiro do player e adicione o offset de vida, ou seja `jogo + player + offset de vida`

Com isso, teremos algo desse tipo

```py
ac_client.exe (jogo) -> 0x18AC00 (player) -> 0xEC (offset de vida)
```

Ou seja, quando acessamos aquela area especifica da memoria, temos o valor da vida do player

###