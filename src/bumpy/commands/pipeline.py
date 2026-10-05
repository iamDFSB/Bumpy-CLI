import typer
from rich.console import Console

from bumpy.file_client import FileClient
from bumpy.models import VersionPart

# Criamos um sub-app dedicado a ações do "pipeline" em lote
pipeline_app = typer.Typer(
    help='Comandos para manipular todos os jobs do pipeline.'
)
console = Console()


@pipeline_app.command('up')
def pipeline_up(
    part: VersionPart = typer.Argument(
        VersionPart.patch,
        help='Parte da versão a atualizar (major, minor, patch)',
    ),
    uat: bool = typer.Option(
        False, '--uat', help='Aplica no ambiente de UAT.'
    ),
):
    """Aumenta a versao de TODOS os jobs do pipeline de uma vez."""
    console.print(
        '[bold green]Subindo a versão de todos os jobs no ambiente selecionado...[/bold green]'
    )
    ambient = 'uat' if uat else 'prd-marketplace'
    path_str = f'pipeline/{ambient}'
    FileClient().increase_all(segment=part.value, pipeline_path=path_str)


@pipeline_app.command('down')
def pipeline_down(
    part: VersionPart = typer.Argument(
        VersionPart.patch,
        help='Parte da versão a atualizar (major, minor, patch)',
    ),
    uat: bool = typer.Option(
        False, '--uat', help='Aplica no ambiente de UAT.'
    ),
):
    """Diminui a versao de TODOS os jobs do pipeline de uma vez."""
    console.print(
        '[bold yellow]Diminuindo a versão de todos os jobs no ambiente selecionado...[/bold yellow]'
    )
    ambient = 'uat' if uat else 'prd-marketplace'
    path_str = f'pipeline/{ambient}'
    FileClient().decrease_all(segment=part.value, pipeline_path=path_str)
