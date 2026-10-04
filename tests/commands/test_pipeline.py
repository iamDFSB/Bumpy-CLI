from typer.testing import CliRunner
from bumpy.commands.pipeline import pipeline_app

runner = CliRunner()

# PRD 

def test_upgrade_all_versions_patch_app():
    result = runner.invoke(pipeline_app, ["up", "patch"])
    assert result.exit_code == 0

def test_upgrade_all_versions_minor_app():
    result = runner.invoke(pipeline_app, ["up", "minor"])
    assert result.exit_code == 0

def test_upgrade_all_versions_major_app():
    result = runner.invoke(pipeline_app, ["up", "major"])
    assert result.exit_code == 0


def test_downgrade_all_versions_patch_app():
    result = runner.invoke(pipeline_app, ["down", "patch"])
    assert result.exit_code == 0

def test_downgrade_all_versions_minor_app():
    result = runner.invoke(pipeline_app, ["down", "minor"])
    assert result.exit_code == 0

def test_downgrade_all_versions_major_app():
    result = runner.invoke(pipeline_app, ["down", "major"])
    assert result.exit_code == 0

# UAT

def test_upgrade_all_versions_patch_app():
    result = runner.invoke(pipeline_app, ["up", "--uat", "patch"])
    assert result.exit_code == 0

def test_upgrade_all_versions_minor_app():
    result = runner.invoke(pipeline_app, ["up", "--uat", "minor"])
    assert result.exit_code == 0

def test_upgrade_all_versions_major_app():
    result = runner.invoke(pipeline_app, ["up", "--uat", "major"])
    assert result.exit_code == 0


def test_downgrade_all_versions_patch_app():
    result = runner.invoke(pipeline_app, ["down", "--uat", "patch"])
    assert result.exit_code == 0

def test_downgrade_all_versions_minor_app():
    result = runner.invoke(pipeline_app, ["down", "--uat", "minor"])
    assert result.exit_code == 0

def test_downgrade_all_versions_major_app():
    result = runner.invoke(pipeline_app, ["down", "--uat", "major"])
    assert result.exit_code == 0