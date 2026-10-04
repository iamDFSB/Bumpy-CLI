import typer
from rich.console import Console
from bumpy.models import VersionPart
from bumpy.file_client import FileClient


# Criamos um sub-app dedicado a ações de "job"
job_app = typer.Typer(
    help='📂 Comandos para manipular um único job específico.'
)
console = Console()


@job_app.command('up')
def job_up(
    name: str = typer.Argument(..., help='Nome da pasta do job.'),
    part: VersionPart = typer.Argument(
        VersionPart.patch,
        help='Parte da versão a atualizar (major, minor, patch)',
    ),
    uat: bool = typer.Option(
        False, '--uat', help='Aplica no ambiente de UAT.'
    ),
):
    """⬆️ Aumenta a versão de um job específico."""
    console.print(
        f"[bold green]Aumentando versão do job '{name}'...[/bold green]"
    )
    ambient = 'uat' if uat else 'prd-marketplace'
    path_str = f'{ambient}/{name}/version'
    FileClient().increase(segment=part.value, pipeline_path=path_str)


@job_app.command('down')
def job_down(
    name: str = typer.Argument(..., help='Nome da pasta do job.'),
    part: VersionPart = typer.Argument(
        VersionPart.patch,
        help='Parte da versão a atualizar (major, minor, patch)',
    ),
    uat: bool = typer.Option(
        False, '--uat', help='Aplica no ambiente de UAT.'
    ),
):
    """⬇️ Diminui a versão de um job específico."""
    console.print(
        f"[bold yellow]Diminuindo versão do job '{name}'...[/bold yellow]"
    )
    ambient = 'uat' if uat else 'prd-marketplace'
    path_str = f'{ambient}/{name}/version'
    FileClient().decrease(segment=part.value, pipeline_path=path_str)
