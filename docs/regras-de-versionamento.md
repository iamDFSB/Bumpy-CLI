# Regras de versionamento

A regra central do projeto é que cada job tenha um arquivo `version` representando uma versão semver simplificada, seguindo o formato:

```text
major.minor.patch
```

Exemplo:

```text
2.4.9
```

## 1. Segmentos válidos

O projeto reconhece somente três segmentos:

- `major`
- `minor`
- `patch`

Esses valores são definidos pelo `Enum` `VersionPart` em `src/bumpy/models.py`.

## 2. Estrutura de arquivos

A estrutura esperada do pipeline é:

```text
pipeline/
├── prd-marketplace/
│   └── meu-cron/
│       └── version
└── uat/
    └── meu-cron/
        └── version
```

Cada folder do job contém um arquivo `version`, e esse arquivo é o ponto de atualização do número.

## 3. Regras de leitura e escrita

A lógica do `FileClient` faz o seguinte:

1. valida se o caminho existe;
2. abre o arquivo `version`;
3. divide o conteúdo por ponto;
4. converte cada parte em número inteiro;
5. altera o segmento solicitado;
6. grava a versão atualizada de volta.

## 4. Comportamento do incremento

Quando o comando é `up`, a operação faz:

```text
X.Y.Z -> X.(Y+1).Z
```

ou

```text
X.Y.Z -> X.Y.(Z+1)
```

conforme o segmento selecionado.

## 5. Comportamento do decremento

Quando o comando é `down`, o projeto reduz o segmento escolhido, mas não permite que o valor fique menor que zero.

Exemplo:

```text
1.2.0 -> 1.1.0
```

Se o segmento atual for `0`, uma exceção é levantada antes da escrita.

## 6. Regras de validação

O projeto trata diversas condições de erro:

- arquivo vazio;
- arquivo incompleto;
- caminho do pipeline inexistente;
- tentativa de decrementar abaixo de zero.

Essas validações estão centralizadas em `src/bumpy/exceptions/file_client_exceptions.py`.

## 7. Semântica do versionamento

Embora o projeto use um formato enxuto, ele se comporta de forma muito próxima ao versionamento semântico tradicional:

- `major`: mudanças maiores, compatibilidade afetada ou mudança de ciclo;
- `minor`: evolução funcional;
- `patch`: correções ou ajustes pequenos.

A regra não é uma validação semântica profunda; ela é funcional e orientada à convenção.

## 8. Observações importantes

- O projeto assume que o diretório de execução atual é a raiz do workspace do pipeline.
- A busca do caminho é feita automaticamente a partir do diretório corrente.
- O uso de `--uat` muda a base de caminho, mas mantém a mesma regra de versionamento.

Em resumo, a regra do projeto é simples e muito objetiva: cada job vive com um número versionado em arquivo e o CLI apenas altera esse número de maneira previsível.
