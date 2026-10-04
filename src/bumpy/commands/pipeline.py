import typer
from rich.console import Console

# Criamos um sub-app dedicado a ações do "pipeline" em lote
pipeline_app = typer.Typer(
    help='🚀 Comandos para manipular todos os jobs do pipeline.'
)
console = Console()


@pipeline_app.command('up')
def pipeline_up(
    uat: bool = typer.Option(False, '--uat', help='Aplica a todos os de UAT.'),
    prd: bool = typer.Option(False, '--prd', help='Aplica a todos os de PRD.'),
):
    """⬆️ Aumenta a versão de TODOS os jobs do pipeline de uma vez."""
    console.print(
        '[bold green]Subindo a versão de todos os jobs no ambiente selecionado...[/bold green]'
    )


@pipeline_app.command('down')
def pipeline_down(
    uat: bool = typer.Option(False, '--uat', help='Aplica a todos os de UAT.'),
    prd: bool = typer.Option(False, '--prd', help='Aplica a todos os de PRD.'),
):
    """⬇️ Diminui a versão de TODOS os jobs do pipeline de uma vez."""
    console.print(
        '[bold yellow]Diminuindo a versão de todos os jobs no ambiente selecionado...[/bold yellow]'
    )
