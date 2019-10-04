# logrotate

Ansible role to install and setup logrotate service

## Requirements

- Ansible >= 2.7

### Supported platforms

- EL
  - 7
- Ubuntu
  - bionic
  - xenial

## Default role variables

| Name                     | Description                                                                                                |      Type      |            Default             | Required |
| ------------------------ | ---------------------------------------------------------------------------------------------------------- |:--------------:|:------------------------------:|:--------:|
| logtotate__package_state | Installed package state                                                                                    |     string     |           `present`            |   True   |
| logtotate__retention     | Rotation interval `daily` ,`monthly`                                                                       |     string     |            `daily`             |   True   |
| logtotate__rotate        | Log files are rotated count times before being removed                                                     |      int       |              `14`              |   True   |
| logtotate__create        | This rotates the log file and creates a new log file with the specified permissions, owner, and group      | bool or string |             `True`             |   True   |
| logtotate__dateext       | Archive old versions of log files adding a daily extension like YYYYMMDD instead of simply adding a number |      bool      | `{{ logtotate__def_dateext }}` |   True   |
| logtotate__compress      | This is used to compress the rotated log file with gzip.                                                   |      bool      |            `False`             |   True   |
| logtotate__su            | Rotate log files set under this user and group instead of using default user/group                         |     string     |   `{{ logtotate__def_su }}`    |   True   |
| logtotate__d             | list of files in `logrotate.d` with his settings                                                           |      dict      |              `{}`              |   True   |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

This section describes static variables implemented in the role.

### Main variables

| Name                    | Description            |  Type  |   Default   |
| ----------------------- | ---------------------- |:------:|:-----------:|
| logtotate__pacakge_name | installed package name | string | `logrotate` |

**All static main variables are described in [vars/main.yml](vars/main.yml) file.**

### centos variables

| Name                   |                Description                | Type | Default |
| ---------------------- |:-----------------------------------------:|:----:| ------- |
| logtotate__def_su      |   default logrotate su param for centos   | bool | `False` |
| logtotate__def_dateext | default logrotate dateext param for cents | bool | `True`  |

**All static centos variables are described in [vars/centos.yml](vars/centos.yml)**

### ubuntu variables

| Name                   |                Description                 | Type | Default       |
| ---------------------- |:------------------------------------------:|:----:| ------------- |
| logtotate__def_su      |   default logrotate su param for ubuntu    | bool | `root syslog` |
| logtotate__def_dateext | default logrotate dateext param for ubuntu | bool | `False`       |

**All static ubuntu variables are described in [vars/ubuntu.yml](vars/ubuntu.yml)**

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.
