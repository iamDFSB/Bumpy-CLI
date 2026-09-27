import typer
from rich.console import Console

# Criamos um sub-app dedicado a ações de "job"
job_app = typer.Typer(help="📂 Comandos para manipular um único job específico.")
console = Console()


@job_app.command("up")
def job_up(
    name: str = typer.Argument(..., help="Nome da pasta do job."),
    uat: bool = typer.Option(False, "--uat", help="Aplica apenas no ambiente de UAT."),
    prd: bool = typer.Option(False, "--prd", help="Aplica apenas no ambiente de PRD.")
):
    """⬆️ Aumenta a versão de um job específico."""
    console.print(f"[bold green]Aumentando versão do job '{name}'...[/bold green]")
    # Aqui entra sua lógica existente de alterar_versao para um único job


@job_app.command("down")
def job_down(
    name: str = typer.Argument(..., help="Nome da pasta do job."),
    uat: bool = typer.Option(False, "--uat", help="Aplica apenas no ambiente de UAT."),
    prd: bool = typer.Option(False, "--prd", help="Aplica apenas no ambiente de PRD.")
):
    """⬇️ Diminui a versão de um job específico."""
    console.print(f"[bold yellow]Diminuindo versão do job '{name}'...[/bold yellow]")
