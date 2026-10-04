# Guia de uso

Este guia explica como usar o CLI do Bumpy em cenários reais de desenvolvimento e operação.

## 1. Instalação

O projeto usa Poetry e já define o entrypoint do CLI em `pyproject.toml`:

```toml
[tool.poetry.scripts]
bumpy = "bumpy.main:app"
```

Então, na raiz do projeto, rode:

```bash
poetry install
```

Após a instalação, o comando fica disponível como:

```bash
bumpy --help
```

Se preferir executar diretamente pela ferramenta do ambiente, também é possível usar:

```bash
poetry run bumpy --help
```

## 2. Visão geral dos comandos

O CLI principal cria dois grupos de comandos:

- `job`: para manipular um job específico.
- `all`: para manipular todos os jobs de um ambiente.

### Estrutura de chamadas

```bash
bumpy job up <nome-do-job> <major|minor|patch>

bumpy job down <nome-do-job> <major|minor|patch>

bumpy all up <major|minor|patch>

bumpy all down <major|minor|patch>
```

A flag `--uat` alterna o ambiente de operação:

```bash
bumpy job up meu-cron patch --uat
bumpy all down minor --uat
```

## 3. Comandos por ambiente

### Ambiente padrão: prd-marketplace

Se a flag `--uat` não for informada, o projeto usa o ambiente `prd-marketplace`.

```bash
bumpy job up meu-cron patch
bumpy all up minor
```

### Ambiente UAT

Quando o ambiente é `uat`, o caminho pesquisado pelo projeto passa a ser `pipeline/uat/...`.

```bash
bumpy job up meu-cron patch --uat
bumpy all down major --uat
```

## 4. Fluxo de execução real

Ao executar, por exemplo:

```bash
bumpy job up meu-cron patch
```

o sistema:

1. monta o caminho `pipeline/prd-marketplace/meu-cron/version`;
2. valida se esse caminho existe;
3. lê o conteúdo do arquivo, por exemplo `1.2.3`;
4. aumenta o valor do segmento `patch` para `1.2.4`;
5. salva o arquivo novamente.

## 5. Exemplos práticos

### Aumentar apenas o patch de um job

```bash
bumpy job up meu-cron patch
```

### Aumentar o minor de todos os jobs do ambiente UAT

```bash
bumpy all up minor --uat
```

### Diminuir o major de um job específico

```bash
bumpy job down meu-cron major
```

### Diminuir o patch de todos os jobs em produção

```bash
bumpy all down patch
```

## 6. Casos de erro comuns

### Arquivo `version` vazio

Se o arquivo existe, mas não tem conteúdo, o projeto lança um erro de arquivo vazio.

### Arquivo com formato inválido

Se o conteúdo não seguir `major.minor.patch`, o sistema sinaliza que faltam segmentos ou que o valor é inválido.

### Decremento abaixo de zero

Quando o comando `down` tenta reduzir o valor de um segmento para menos que zero, a ferramenta bloqueia a operação e lança `VersionUnderflowError`.

### Caminho inexistente

Se o ambiente ou o nome do job não corresponde às pastas presentes na estrutura do projeto, a aplicação informa que o caminho do pipeline não foi encontrado.

## 7. Boas práticas

- mantenha todos os arquivos `version` com o mesmo padrão;
- use `major` somente para mudanças de compatibilidade ou impactos grandes;
- use `minor` para evoluções de funcionalidade;
- use `patch` para ajustes menores;
- prefira testar em `uat` antes de aplicar alteração em produção.

## 8. Dicas de uso em CI/CD

O CLI pode ser integrado facilmente em scripts de release e deploy, destacando fluxos como:

- levar um job para produção;
- atualizar o número da versão em lote;
- manter a padronização dos pipelines por ambiente.

A ideia é que a operação seja simples, previsível e totalmente baseada em arquivos de controle dentro do projeto.
