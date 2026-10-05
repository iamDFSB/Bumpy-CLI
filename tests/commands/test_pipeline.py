from typer.testing import CliRunner

from bumpy.commands.pipeline import pipeline_app
from bumpy.models import VersionPart

runner = CliRunner()

# PRD


def test_upgrade_all_versions_patch_prd_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'prd-marketplace/meu-cron/version',
        pipeline_workspace / 'prd-marketplace/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.patch) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['up', 'patch'])

    new_versions = [
        get_version_value(path, VersionPart.patch) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new > old for old, new in zip(current_versions, new_versions))


def test_upgrade_all_versions_minor_prd_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'prd-marketplace/meu-cron/version',
        pipeline_workspace / 'prd-marketplace/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.minor) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['up', 'minor'])

    new_versions = [
        get_version_value(path, VersionPart.minor) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new > old for old, new in zip(current_versions, new_versions))


def test_upgrade_all_versions_major_prd_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'prd-marketplace/meu-cron/version',
        pipeline_workspace / 'prd-marketplace/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.major) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['up', 'major'])

    new_versions = [
        get_version_value(path, VersionPart.major) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new > old for old, new in zip(current_versions, new_versions))


def test_downgrade_all_versions_patch_prd_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'prd-marketplace/meu-cron/version',
        pipeline_workspace / 'prd-marketplace/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.patch) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['down', 'patch'])

    new_versions = [
        get_version_value(path, VersionPart.patch) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new < old for old, new in zip(current_versions, new_versions))


def test_downgrade_all_versions_minor_prd_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'prd-marketplace/meu-cron/version',
        pipeline_workspace / 'prd-marketplace/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.minor) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['down', 'minor'])

    new_versions = [
        get_version_value(path, VersionPart.minor) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new < old for old, new in zip(current_versions, new_versions))


def test_downgrade_all_versions_major_prd_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'prd-marketplace/meu-cron/version',
        pipeline_workspace / 'prd-marketplace/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.major) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['down', 'major'])

    new_versions = [
        get_version_value(path, VersionPart.major) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new < old for old, new in zip(current_versions, new_versions))


# UAT


def test_upgrade_all_versions_patch_uat_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'uat/meu-cron/version',
        pipeline_workspace / 'uat/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.patch) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['up', '--uat', 'patch'])

    new_versions = [
        get_version_value(path, VersionPart.patch) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new > old for old, new in zip(current_versions, new_versions))


def test_upgrade_all_versions_minor_uat_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'uat/meu-cron/version',
        pipeline_workspace / 'uat/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.minor) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['up', '--uat', 'minor'])

    new_versions = [
        get_version_value(path, VersionPart.minor) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new > old for old, new in zip(current_versions, new_versions))


def test_upgrade_all_versions_major_uat_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'uat/meu-cron/version',
        pipeline_workspace / 'uat/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.major) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['up', '--uat', 'major'])

    new_versions = [
        get_version_value(path, VersionPart.major) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new > old for old, new in zip(current_versions, new_versions))


def test_downgrade_all_versions_patch_uat_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'uat/meu-cron/version',
        pipeline_workspace / 'uat/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.patch) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['down', '--uat', 'patch'])

    new_versions = [
        get_version_value(path, VersionPart.patch) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new < old for old, new in zip(current_versions, new_versions))


def test_downgrade_all_versions_minor_uat_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'uat/meu-cron/version',
        pipeline_workspace / 'uat/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.minor) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['down', '--uat', 'minor'])

    new_versions = [
        get_version_value(path, VersionPart.minor) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new < old for old, new in zip(current_versions, new_versions))


def test_downgrade_all_versions_major_uat_app(
    pipeline_workspace, get_version_value
):
    paths = [
        pipeline_workspace / 'uat/meu-cron/version',
        pipeline_workspace / 'uat/meu-cron-second/version',
    ]
    current_versions = [
        get_version_value(path, VersionPart.major) for path in paths
    ]

    result = runner.invoke(pipeline_app, ['down', '--uat', 'major'])

    new_versions = [
        get_version_value(path, VersionPart.major) for path in paths
    ]

    assert result.exit_code == 0
    assert all(new < old for old, new in zip(current_versions, new_versions))
