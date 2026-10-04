from typer.testing import CliRunner
from bumpy.commands.job import job_app

runner = CliRunner()

def test_upgrade_version_patch_app():
    result = runner.invoke(job_app, ["up", "meu-cron", "patch"])
    assert result.exit_code == 0

def test_upgrade_version_minor_app():
    result = runner.invoke(job_app, ["up", "meu-cron", "minor"])
    assert result.exit_code == 0

def test_upgrade_version_major_app():
    result = runner.invoke(job_app, ["up", "meu-cron", "major"])
    assert result.exit_code == 0

def test_downgrade_version_patch_app():
    result = runner.invoke(job_app, ["down", "meu-cron", "patch"])
    assert result.exit_code == 0

def test_downgrade_version_minor_app():
    result = runner.invoke(job_app, ["down", "meu-cron", "minor"])
    assert result.exit_code == 0

def test_downgrade_version_major_app():
    result = runner.invoke(job_app, ["down", "meu-cron", "major"])
    assert result.exit_code == 0