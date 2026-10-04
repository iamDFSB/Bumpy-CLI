from enum import Enum
import typer
from rich.console import Console
from bumpy.file_client import FileClient


# Criamos um sub-app dedicado a ações de "job"
job_app = typer.Typer(
    help='📂 Comandos para manipular um único job específico.'
)
console = Console()

class VersionPart(str, Enum):
    major = "major"
    minor = "minor"
    patch = "patch"

@job_app.command('up')
def job_up(
    name: str = typer.Argument(..., help='Nome da pasta do job.'),
    part: VersionPart = typer.Argument(
        VersionPart.patch, help='Parte da versão a atualizar (major, minor, patch)'
    ),
    uat: bool = typer.Option(
        False, '--uat', help='Aplica apenas no ambiente de UAT.'
    ),
):
    """⬆️ Aumenta a versão de um job específico."""
    console.print(
        f"[bold green]Aumentando versão do job '{name}'...[/bold green]"
    )
    ambient = "uat" if uat else "prd-marketplace"
    path_str = f'{ambient}/{name}/version'
    file_client = FileClient(path_str)
    print("Nome: ", part.value)
    file_client.increase(segment=part.value)


@job_app.command('down')
def job_down(
    name: str = typer.Argument(..., help='Nome da pasta do job.'),
    part: VersionPart = typer.Argument(
        VersionPart.patch, help='Parte da versão a atualizar (major, minor, patch)'
    ),
    uat: bool = typer.Option(
        False, "--uat", help='Aplica apenas no ambiente de UAT.'
    ),
):
    """⬇️ Diminui a versão de um job específico."""
    console.print(
        f"[bold yellow]Diminuindo versão do job '{name}'...[/bold yellow]"
    )
    ambient = "uat" if uat else "prd-marketplace"
    path_str = f'{ambient}/{name}/version'
    file_client = FileClient(path_str)
    file_client.decrease(segment=part.value)