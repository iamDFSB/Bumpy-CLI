from typer.testing import CliRunner
from bumpy.commands.job import job_app
from bumpy.models import VersionPart

runner = CliRunner()

# PRD


def test_upgrade_version_patch_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'prd-marketplace/meu-cron/version'
    current_version = get_version_value(path, VersionPart.patch)

    result = runner.invoke(job_app, ['up', 'meu-cron', 'patch'])

    new_version = get_version_value(path, VersionPart.patch)

    assert result.exit_code == 0
    assert new_version > current_version


def test_upgrade_version_minor_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'prd-marketplace/meu-cron/version'
    current_version = get_version_value(path, VersionPart.minor)

    result = runner.invoke(job_app, ['up', 'meu-cron', 'minor'])

    new_version = get_version_value(path, VersionPart.minor)

    assert result.exit_code == 0
    assert new_version > current_version


def test_upgrade_version_major_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'prd-marketplace/meu-cron/version'
    current_version = get_version_value(path, VersionPart.major)

    result = runner.invoke(job_app, ['up', 'meu-cron', 'major'])

    new_version = get_version_value(path, VersionPart.major)

    assert result.exit_code == 0
    assert new_version > current_version


def test_downgrade_version_patch_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'prd-marketplace/meu-cron/version'
    current_version = get_version_value(path, VersionPart.patch)

    result = runner.invoke(job_app, ['down', 'meu-cron', 'patch'])

    new_version = get_version_value(path, VersionPart.patch)

    assert result.exit_code == 0
    assert new_version < current_version


def test_downgrade_version_minor_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'prd-marketplace/meu-cron/version'
    current_version = get_version_value(path, VersionPart.minor)

    result = runner.invoke(job_app, ['down', 'meu-cron', 'minor'])

    new_version = get_version_value(path, VersionPart.minor)

    assert result.exit_code == 0
    assert new_version < current_version


def test_downgrade_version_major_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'prd-marketplace/meu-cron/version'
    current_version = get_version_value(path, VersionPart.major)

    result = runner.invoke(job_app, ['down', 'meu-cron', 'major'])

    new_version = get_version_value(path, VersionPart.major)

    assert result.exit_code == 0
    assert new_version < current_version


# UAT


def test_upgrade_version_uat_patch_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'uat/meu-cron/version'
    current_version = get_version_value(path, VersionPart.patch)

    result = runner.invoke(job_app, ['up', '--uat', 'meu-cron', 'patch'])

    new_version = get_version_value(path, VersionPart.patch)

    assert result.exit_code == 0
    assert new_version > current_version


def test_upgrade_version_uat_minor_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'uat/meu-cron/version'
    current_version = get_version_value(path, VersionPart.minor)

    result = runner.invoke(job_app, ['up', '--uat', 'meu-cron', 'minor'])

    new_version = get_version_value(path, VersionPart.minor)

    assert result.exit_code == 0
    assert new_version > current_version


def test_upgrade_version_uat_major_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'uat/meu-cron/version'
    current_version = get_version_value(path, VersionPart.major)

    result = runner.invoke(job_app, ['up', '--uat', 'meu-cron', 'major'])

    new_version = get_version_value(path, VersionPart.major)

    assert result.exit_code == 0
    assert new_version > current_version


def test_downgrade_version_uat_patch_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'uat/meu-cron/version'
    current_version = get_version_value(path, VersionPart.patch)

    result = runner.invoke(job_app, ['down', '--uat', 'meu-cron', 'patch'])

    new_version = get_version_value(path, VersionPart.patch)

    assert result.exit_code == 0
    assert new_version < current_version


def test_downgrade_version_uat_minor_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'uat/meu-cron/version'
    current_version = get_version_value(path, VersionPart.minor)

    result = runner.invoke(job_app, ['down', '--uat', 'meu-cron', 'minor'])

    new_version = get_version_value(path, VersionPart.minor)

    assert result.exit_code == 0
    assert new_version < current_version


def test_downgrade_version_uat_major_app(pipeline_workspace, get_version_value):
    path = pipeline_workspace / 'uat/meu-cron/version'
    current_version = get_version_value(path, VersionPart.major)

    result = runner.invoke(job_app, ['down', '--uat', 'meu-cron', 'major'])

    new_version = get_version_value(path, VersionPart.major)

    assert result.exit_code == 0
    assert new_version < current_version
