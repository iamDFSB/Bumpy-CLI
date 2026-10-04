# Bumpy CLI

Bumpy CLI é um utilitário em Python para gerenciar versões de jobs em pipelines, incrementando ou decrementando os segmentos de uma versão (`major`, `minor` ou `patch`) em arquivos de controle localizados dentro de pastas de ambiente.

## Objetivo

O projeto foi pensado para facilitar a manutenção de versões em ambientes como:

- `pipeline/prd-marketplace/`
- `pipeline/uat/`

Cada job possui um arquivo `version` com conteúdo no formato:

```text
1.2.3
```

O CLI lê esse valor, altera o segmento solicitado e salva a nova versão de volta no arquivo.

## Estrutura esperada

```text
pipeline/
├── prd-marketplace/
│   ├── meu-cron/
│   │   └── version
│   └── meu-cron-second/
│       └── version
└── uat/
    ├── meu-cron/
    │   └── version
    └── meu-cron-second/
        └── version
```

## Regras do projeto

- O nome do arquivo precisa ser `version`.
- O conteúdo deve seguir o padrão `major.minor.patch`.
- A aplicação aceita apenas `major`, `minor` e `patch` como segmentos.
- O comando de decremento não permite que qualquer parte da versão fique abaixo de `0`.
- Se o diretório do job ou do ambiente não existir, a ferramenta lança exceção de caminho não encontrado.
- Se o arquivo estiver vazio ou não tiver 3 partes, a execução falha com uma exceção específica.

## Como instalar

Com Poetry:

```bash
poetry install
```

O entrypoint do CLI já está configurado em `pyproject.toml`:

```toml
[tool.poetry.scripts]
bumpy = "bumpy.main:app"
```

## Exemplos de uso

### Job específico

```bash
bumpy job up meu-cron patch
bumpy job up meu-cron minor
bumpy job up meu-cron major

bumpy job down meu-cron patch
bumpy job down meu-cron minor
bumpy job down meu-cron major
```

### Ambiente UAT

```bash
bumpy job up meu-cron patch --uat
bumpy job down meu-cron minor --uat
```

### Pipeline completo

```bash
bumpy all up patch
bumpy all up minor --uat
bumpy all down major
bumpy all down patch --uat
```

## Fluxo interno

A lógica principal fica em `FileClient`, que:

1. valida o caminho do pipeline;
2. lê o arquivo `version`;
3. converte os segmentos em inteiros;
4. incrementa ou decrementa o segmento solicitado;
5. escreve a versão de volta no arquivo.

## Testes

Os testes automáticos validam os comandos de `job` e `all` para ambos os ambientes (`prd-marketplace` e `uat`).

```bash
pytest
```

## Stack principal

- Python 3.12+
- Typer
- Rich
- pytest
- MkDocs + Material

## Objetivo prático

O projeto ajuda a automatizar a gestão de versões em pipelines multiambiente, permitindo ajustar rapidamente a versão de um job individual ou de todos os jobs do ambiente de forma padronizada.
