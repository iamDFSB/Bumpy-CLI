import typer

from commands.job import job_app
from commands.pipeline import pipeline_app

# App principal (Raiz da Árvore)
app = typer.Typer(help="💥 Bumpy: Gerenciador de versões para pipelines multi-plataforma.")

# Registrando os galhos/nós na árvore de comandos
app.add_typer(job_app, name="job")
app.add_typer(pipeline_app, name="all")

if __name__ == "__main__":
    app()