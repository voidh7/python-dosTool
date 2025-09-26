
# sherma DoS Tool

<img src="https://i.postimg.cc/sgWK130f/artworks-Hdc5-DRzbx82ci4-LB-EJYn7-A-t1080x1080.jpg" width="150">

Ferramenta para realizar ataques DoS/DDoS.

## Instalação

### Requisitos mínimos:
- Git
- Python3

### comandos

1. #### Clone o repositório:
```bash
git clone https://github.com/voidh7/sherma-ddos-tool && cd sherma
```

1.#### Instale as dependências:

```bash
pip install -e .
```

## Como usar?

Para iniciar um ataque:

```bash
python3 sherma.py <url> -v -t 10
```

#### Opções:

· -v - Modo verboso
· -t - Define o número de threads
