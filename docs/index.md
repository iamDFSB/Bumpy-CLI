![Bumpy CLI](assets/images/logo.png)

# Bumpy CLI

O Bumpy CLI atualiza versões de jobs em arquivos `version` do seu pipeline.
Use-o para incrementar ou decrementar `major`, `minor` ou `patch` de um job
específico ou de todos os jobs de um ambiente.

## Comece aqui

- [Instalação e uso](guia-de-uso.md): instale o comando, prepare seu projeto e
  veja exemplos para atualizar jobs.
- [Regras de versão](regras-de-versionamento.md): consulte o formato esperado e
  os limites das operações.

## Acesso rápido

```bash
bumpy job up meu-cron patch
bumpy all up minor --uat
```

Os comandos devem ser executados a partir da raiz do projeto que contém a pasta
`pipeline`. Por padrão, as operações usam o ambiente `prd-marketplace`; adicione
`--uat` para usar o ambiente UAT.
