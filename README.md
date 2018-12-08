Ansible Role: Hub
=================

[![Build Status](https://travis-ci.com/gantsign/ansible_role_hub.svg?branch=master)](https://travis-ci.com/gantsign/ansible_role_hub)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.hub-blue.svg)](https://galaxy.ansible.com/gantsign/hub)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible_role_hub/master/LICENSE)

Role to download and install GitHubs's [Hub](https://hub.github.com/) the
command-line wrapper for Git that adds features for GitHub repositories.

Requirements
------------

* Ansible >= 2.5

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 7

        * Fedora

            * 28

    * SUSE Family

        * openSUSE

            * 15.0

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# Hub version number
hub_version: '2.6.0'

# The SHA256 of the Hub redistributable package
hub_redis_sha256sum: '98cad5b7cff4b9b3d31cf29100c6453358dd0e37e28ba57a1c85ec289fe03d3e'

# Directory to store files downloaded for Hub
hub_download_dir: "{{ x_ansible_download_dir | default(ansible_env.HOME + '/.ansible/tmp/downloads') }}"
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.hub
```

Tab Completion & Git Alias for Zsh
------------------------------------

### Using Ansible

The recommended way to enable Zsh support for Hub is to use the
[gantsign.antigen](https://galaxy.ansible.com/gantsign/antigen) role (this must
be configured for each user).


```yaml
- hosts: servers
  roles:
    - role: gantsign.hub

    - role: gantsign.antigen
      users:
        - username: example
          antigen_bundles:
            - name: hub
              url: '/usr/local/share/hub/zsh'
```

### Using Antigen

If you prefer to use [Antigen](https://github.com/zsh-users/antigen) directly
add the following to your Antigen configuration:

```bash
antigen bundle /usr/local/share/hub/zsh
```

### Manual configuration

To manually configure Zsh add the following to your `.zshrc`:

```bash
# Configure Hub alias for Git
source /usr/local/share/hub/zsh/hub.plugin.zsh

# Configure tab completion for Hub
fpath=(/usr/local/share/hub/zsh $fpath)
autoload -U compinit && compinit
```

Tab Completion & Git Alias for Other Shells
---------------------------------------------

Download tab completion support for your shell from
[here](https://github.com/github/hub/tree/master/etc); follow the
instructions for configuring tab completion
[here](https://github.com/github/hub/blob/master/etc/README.md#installation-instructions).

Follow these instructions for setting up the alias
[here](https://github.com/github/hub#aliasing).


More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
