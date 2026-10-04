# Bumpy CLI

O Bumpy CLI é uma ferramenta para controlar a versão de jobs em ambientes de pipeline, permitindo aumentar ou reduzir os valores de `major`, `minor` e `patch` em arquivos de versão salvos em pastas específicas.

## O que o projeto resolve

Em projetos que mantêm vários jobs em paralelo, cada ambiente pode ter uma estrutura parecida com esta:

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

Cada arquivo `version` guarda um número como `1.2.3`. O CLI automatiza a alteração desse valor sem exigir edição manual de arquivos.

## Como funciona em poucas palavras

O projeto organiza os comandos em duas camadas:

- `job`: altera um único job por nome;
- `all`: altera todos os jobs de um ambiente de uma vez.

Cada commando aceita `up` ou `down` e o segmento da versão:

- `major`
- `minor`
- `patch`

Além disso, é possível apontar para `uat` com a flag `--uat`.

## Exemplos práticos

```bash
bumpy job up meu-cron patch
bumpy job down meu-cron minor
bumpy job up meu-cron major --uat
bumpy all up patch
bumpy all down major --uat
```

## Regras da aplicação

Antes de rodar qualquer operação, o projeto aplica algumas regras:

- a pasta do pipeline deve existir;
- cada arquivo `version` deve ter 3 segmentos: `major.minor.patch`;
- o valor de qualquer segmento não pode ficar menor que `0` quando executando `down`;
- arquivos vazios ou incompletos geram exceções específicas.

## Estrutura do código

A aplicação principal está em:

- `src/bumpy/main.py`: cria a árvore de comandos do CLI;
- `src/bumpy/commands/job.py`: subcomandos para um job específico;
- `src/bumpy/commands/pipeline.py`: subcomandos para todos os jobs;
- `src/bumpy/file_client.py`: lógica de leitura, validação e atualização de arquivos;
- `src/bumpy/models.py`: enumera os segmentos válidos da versão;
- `src/bumpy/exceptions/file_client_exceptions.py`: exceções do fluxo de validação.

## Próximos passos

- Consulte o guia de uso em [guia-de-uso.md](guia-de-uso.md)
- Entenda as regras de versionamento em [regras-de-versionamento.md](regras-de-versionamento.md)
- Veja a arquitetura do código em [arquitetura.md](arquitetura.md)

## Comandos de documentação

```bash
mkdocs serve
mkdocs build
```
