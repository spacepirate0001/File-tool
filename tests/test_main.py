import pytest
from click.testing import CliRunner
from src.main import cli
from pathlib import Path

@pytest.fixture
def runner():
    return CliRunner()

def test_create_command_empty(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(cli, ['create', 'test.txt'])
        assert result.exit_code == 0
        assert Path('test.txt').exists()
        assert Path('test.txt').read_text() == ''

def test_create_command_with_content(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(cli, ['create', 'test.txt', '--content', 'Hello'])
        assert result.exit_code == 0
        assert Path('test.txt').exists()
        assert Path('test.txt').read_text() == 'Hello'

def test_create_command_existing_file(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        Path('test.txt').write_text('existing')
        result = runner.invoke(cli, ['create', 'test.txt'])
        assert result.exit_code != 0
        assert 'Error: File already exists' in result.output

def test_copy_command(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        Path('source.txt').write_text('content')
        result = runner.invoke(cli, ['copy', 'source.txt', 'dest.txt'])
        assert result.exit_code == 0
        assert Path('dest.txt').exists()
        assert Path('dest.txt').read_text() == 'content'

def test_copy_command_nonexistent_source(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(cli, ['copy', 'nonexistent.txt', 'dest.txt'])
        assert result.exit_code != 0
        assert 'Error: Source file not found' in result.output

def test_combine_command(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        Path('first.txt').write_text('first\n')
        Path('second.txt').write_text('second\n')
        result = runner.invoke(cli, ['combine', 'first.txt', 'second.txt', 'output.txt'])
        assert result.exit_code == 0
        assert Path('output.txt').exists()
        assert Path('output.txt').read_text() == 'first\nsecond\n'

def test_combine_command_missing_files(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(cli, ['combine', 'nonexistent1.txt', 'nonexistent2.txt', 'output.txt'])
        assert result.exit_code != 0
        assert 'Error: First file not found' in result.output

def test_delete_command(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        Path('to_delete.txt').write_text('delete me')
        result = runner.invoke(cli, ['delete', 'to_delete.txt'])
        assert result.exit_code == 0
        assert not Path('to_delete.txt').exists()

def test_delete_command_nonexistent(runner, tmp_path):
    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(cli, ['delete', 'nonexistent.txt'])
        assert result.exit_code != 0
        assert 'Error: File not found' in result.output