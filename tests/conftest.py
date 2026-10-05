import pytest
from bumpy.models import VersionPart


@pytest.fixture
def pipeline_workspace(tmp_path, monkeypatch) -> any:
    root = tmp_path / 'pipeline'

    for environment in ['prd-marketplace', 'uat']:
        for job_name in ['meu-cron', 'meu-cron-second']:
            version_file = root / environment / job_name / 'version'
            version_file.parent.mkdir(parents=True, exist_ok=True)
            version_file.write_text('2.2.2', encoding='utf-8')

    monkeypatch.chdir(tmp_path)
    return root


@pytest.fixture
def get_version_value():
    def executor(path: str, part: VersionPart) -> int:
        with open(path) as file:
            result = file.read()
            version = result.split(".")[part.get_index_position()]
            return int(version)
    return executor

