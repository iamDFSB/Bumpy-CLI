# Arquitetura

A estrutura do projeto foi pensada para separar responsabilidades de forma simples e direta:

- camada de entrada do CLI;
- camada de organização dos comandos;
- camada de manipulação de arquivos e versões;
- camada de tratamento de exceções.

## 1. Estrutura principal

```text
src/
├── bumpy/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── file_client.py
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── job.py
│   │   └── pipeline.py
│   └── exceptions/
│       ├── __init__.py
│       └── file_client_exceptions.py
└── tests/
    └── commands/
        ├── test_job.py
        └── test_pipeline.py
```

## 2. `main.py`

O arquivo `src/bumpy/main.py` é o ponto de entrada da aplicação. Ele cria o Typer principal e registra os grupos de comandos:

```python
app = typer.Typer(...)
app.add_typer(job_app, name='job')
app.add_typer(pipeline_app, name='all')
```

Com isso, a CLI se organiza em uma árvore de comandos, facilitando a extensão.

## 3. `commands/job.py`

Este módulo implementa os comandos do grupo `job`.

### Comandos disponíveis

- `job up <job-name> <segment>`
- `job down <job-name> <segment>`

Ele usa `typer.Argument` para receber o nome do job e o segmento da versão, além da flag `--uat`.

A lógica de atualização delega para `FileClient`.

## 4. `commands/pipeline.py`

Este módulo implementação o grupo `all`.

### Comandos disponíveis

- `all up <segment>`
- `all down <segment>`

Esse fluxo percorre todos os diretórios dentro do ambiente selecionado e atualiza os arquivos `version` de cada job.

## 5. `file_client.py`

Este é o coração do projeto. A classe `FileClient` possui a lógica de:

- validação de caminho;
- leitura da versão atual;
- incremento/decremento do segmento;
- gravação no arquivo;
- atualização em lote para o ambiente inteiro.

### Métodos principais

- `increase()`
- `decrease()`
- `increase_all()`
- `decrease_all()`

O comportamento é linear e direto: o cliente não persiste estado fora do arquivo.

## 6. `models.py`

O módulo define o enum `VersionPart` para limitar os valores permitidos:

```python
class VersionPart(str, Enum):
    major = 'major'
    minor = 'minor'
    patch = 'patch'
```

Isso garante que a CLI aceite apenas os segmentos esperados.

## 7. `exceptions/file_client_exceptions.py`

As exceções definem os erros esperados quando a operação falha:

- `EmptyFileException`
- `MissingSegmentsException`
- `NotFoundPipelinePathException`
- `VersionUnderflowError`

Esse conjunto de exceções torna a aplicação mais previsível em cenários de uso real.

## 8. Testes

Os testes ficam em `tests/commands/` e validam o comportamento principal dos comandos:

- `test_job.py`: comandos por job;
- `test_pipeline.py`: comandos em lote.

Esses testes cobrem ambos os ambientes e os três segmentos de versão.

## 9. Fluxo principal da execução

```text
CLI -> Typer command -> FileClient -> arquivo version -> nova versão salva
```

Essa arquitetura é simples, mas adequada ao objetivo do projeto: automatizar a manutenção de versões em pipelines com poucos componentes e baixa complexidade.
