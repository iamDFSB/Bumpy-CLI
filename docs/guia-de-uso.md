# Instalação e uso

## Requisitos

- Python 3.12 ou superior;
- acesso ao projeto de pipeline em que deseja atualizar as versões.

## Instalação

Para instalar o Bumpy CLI de forma isolada, use o [pipx](https://pipx.pypa.io/):

```bash
pipx install bumpy-cli
```

Como alternativa, instale-o no ambiente Python ativo:

```bash
python -m pip install bumpy-cli
```

Confira os comandos disponíveis:

```bash
bumpy --help
```

## Prepare o projeto

Execute o Bumpy a partir da raiz do projeto que contém a pasta `pipeline`.
Cada job deve ter um arquivo chamado `version` com três números inteiros
separados por ponto:

```text
pipeline/
├── prd-marketplace/
│   └── meu-cron/
│       └── version
└── uat/
    └── meu-cron/
        └── version
```

Por exemplo, o conteúdo do arquivo `pipeline/prd-marketplace/meu-cron/version`
pode ser:

```text
1.2.3
```

## Atualize um job

Os comandos `job` atualizam um único job. Sem `--uat`, o ambiente usado é
`prd-marketplace`:

```bash
bumpy job up meu-cron patch
bumpy job up meu-cron minor
bumpy job up meu-cron major
```

Use `down` para decrementar o segmento:

```bash
bumpy job down meu-cron patch
```

Para executar no ambiente `uat`, acrescente `--uat`:

```bash
bumpy job up meu-cron patch --uat
```

## Atualize todos os jobs

Os comandos `all` aplicam a operação a todos os jobs no ambiente escolhido:

```bash
bumpy all up patch
bumpy all down minor
bumpy all up major --uat
```

Cada pasta de job precisa conter um arquivo `version` válido. Antes de
atualizações em lote, confira os arquivos do ambiente para evitar interrupção
por conteúdo inválido ou por um segmento que não possa ser decrementado.

## Ajuda dos comandos

Use `--help` para ver a sintaxe e as opções:

```bash
bumpy --help
bumpy job --help
bumpy all --help
```

## Problemas comuns

- **Job ou ambiente não encontrado:** confira se está executando na raiz correta
  e se os diretórios seguem a estrutura apresentada acima.
- **Arquivo vazio ou versão incompleta:** preencha `version` no formato
  `major.minor.patch`, por exemplo `1.2.3`.
- **Tentativa de decrementar um segmento igual a zero:** `down` não reduz nenhum
  segmento para um valor menor que zero.
