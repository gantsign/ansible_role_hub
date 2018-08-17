import pytest

import os

import testinfra.utils.ansible_runner

import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('dir_path', [
    '/usr/local/bin',
    '/usr/local/share/man/man1',
    '/usr/local/share/hub',
    '/usr/local/share/hub/zsh',
])
def test_directories(host, dir_path):
    dir = host.file(dir_path)
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'
    assert dir.group == 'root'


@pytest.mark.parametrize('file_path', [
    '/usr/local/bin/hub',
    '/usr/local/share/man/man1/hub-alias.1',
    '/usr/local/share/man/man1/hub-am.1',
    '/usr/local/share/man/man1/hub-apply.1',
    '/usr/local/share/man/man1/hub-browse.1',
    '/usr/local/share/man/man1/hub-checkout.1',
    '/usr/local/share/man/man1/hub-cherry-pick.1',
    '/usr/local/share/man/man1/hub-ci-status.1',
    '/usr/local/share/man/man1/hub-clone.1',
    '/usr/local/share/man/man1/hub-compare.1',
    '/usr/local/share/man/man1/hub-create.1',
    '/usr/local/share/man/man1/hub-delete.1',
    '/usr/local/share/man/man1/hub-fetch.1',
    '/usr/local/share/man/man1/hub-fork.1',
    '/usr/local/share/man/man1/hub-help.1',
    '/usr/local/share/man/man1/hub-init.1',
    '/usr/local/share/man/man1/hub-issue.1',
    '/usr/local/share/man/man1/hub-merge.1',
    '/usr/local/share/man/man1/hub-pr.1',
    '/usr/local/share/man/man1/hub-pull-request.1',
    '/usr/local/share/man/man1/hub-push.1',
    '/usr/local/share/man/man1/hub-release.1',
    '/usr/local/share/man/man1/hub-remote.1',
    '/usr/local/share/man/man1/hub-submodule.1',
    '/usr/local/share/man/man1/hub-sync.1',
    '/usr/local/share/man/man1/hub.1',
    '/usr/local/share/hub/zsh/_hub',
    '/usr/local/share/hub/zsh/hub.plugin.zsh',
])
def test_files(host, file_path):
    installed_file = host.file(file_path)
    assert installed_file.exists
    assert installed_file.is_file
    assert installed_file.user == 'root'
    assert installed_file.group == 'root'


def test_version(host):
    version = host.check_output('hub --version')
    pattern = 'hub version [0-9\\.]+'
    assert re.search(pattern, version)
