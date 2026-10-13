# Regras de versão

Cada job deve ter um arquivo `version` com três números inteiros separados por
ponto:

```text
major.minor.patch
```

Por exemplo, `2.4.9`.

## Segmentos

- `major`: primeira parte da versão;
- `minor`: segunda parte da versão;
- `patch`: terceira parte da versão.

O comando `up` soma 1 ao segmento escolhido, sem alterar os outros. Por exemplo,
incrementar `patch` de `2.4.9` resulta em `2.4.10`.

O comando `down` subtrai 1 do segmento escolhido, sem alterar os outros. Um
segmento que já esteja em `0` não pode ser decrementado.

## Formato e localização

O arquivo precisa chamar-se `version` e estar dentro da pasta do job:

```text
pipeline/
├── prd-marketplace/
│   └── nome-do-job/
│       └── version
└── uat/
    └── nome-do-job/
        └── version
```

Execute os comandos a partir da raiz que contém `pipeline`. O ambiente padrão é
`prd-marketplace`; use `--uat` para selecionar `uat`.
