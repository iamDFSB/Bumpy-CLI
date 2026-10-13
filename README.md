![Bumpy CLI](docs/assets/images/logo.png)

# Bumpy CLI

[![Documentação](https://img.shields.io/badge/Documenta%C3%A7%C3%A3o-Read%20the%20Docs-blue?logo=readthedocs)](https://bumpy-cli.readthedocs.io/pt-br/latest/)
[![Codecov](https://codecov.io/gh/iamDFSB/Bumpy-CLI/branch/main/graph/badge.svg)](https://app.codecov.io/github/iamDFSB/Bumpy-CLI)
[![CI](https://github.com/iamDFSB/Bumpy-CLI/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/iamDFSB/Bumpy-CLI/actions)

O Bumpy CLI ajuda a atualizar as versões dos jobs mantidos em arquivos `version`
de um pipeline. Com ele, você pode incrementar ou decrementar `major`, `minor`
ou `patch` de um job específico ou de todos os jobs de um ambiente.

## Requisitos

- Python 3.12 ou superior;
- um projeto com a estrutura de pastas descrita abaixo.

## Instalação

Como o Bumpy é uma ferramenta de linha de comando, recomendamos instalá-lo com
[pipx](https://pipx.pypa.io/), que mantem as dependencias isoladas:

```bash
pipx install bumpy-cli
```

Também é possível instalar no ambiente Python ativo:

```bash
python -m pip install bumpy-cli
```

Confirme a instalacao e veja os comandos disponiveis:

```bash
bumpy --help
```

## Prepare o projeto

Execute os comandos a partir da raiz do projeto que contem a pasta `pipeline`.
Cada job precisa ter um arquivo `version` com tres numeros separados por ponto:

```text
pipeline/
├── prd-marketplace/
│   └── meu-cron/
│       └── version
└── uat/
    └── meu-cron/
        └── version
```

Por exemplo, o arquivo `pipeline/prd-marketplace/meu-cron/version` pode conter:

```text
1.2.3
```

## Uso

### Atualizar um job

Por padrão, os comandos atuam no ambiente `prd-marketplace`:

```bash
bumpy job up meu-cron patch
```

Esse comando altera `1.2.3` para `1.2.4`. Para atualizar outro segmento:

```bash
bumpy job up meu-cron minor
bumpy job up meu-cron major
```

Use `down` para decrementar o segmento. O valor não pode ficar abaixo de zero:

```bash
bumpy job down meu-cron patch
```

Para atuar no ambiente `uat`, adicione `--uat`:

```bash
bumpy job up meu-cron patch --uat
```

### Atualizar todos os jobs de um ambiente

Os comandos `all` atualizam todos os jobs dentro do ambiente selecionado:

```bash
bumpy all up patch
bumpy all down minor
bumpy all up major --uat
```

Cada pasta de job do ambiente precisa conter um arquivo `version` válido.

## Ajuda

Consulte a ajuda geral ou a de um grupo de comandos:

```bash
bumpy --help
bumpy job --help
bumpy all --help
```

## Desenvolvimento

O código-fonte, as instruções para contribuir e a documentação do projeto estão
no [repositorio no GitHub](https://github.com/iamDFSB/Bumpy-CLI).
