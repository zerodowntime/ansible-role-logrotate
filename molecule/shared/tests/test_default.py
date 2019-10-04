import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_is_installed(host):
    pkg = host.package('logrotate')
    assert pkg.is_installed


def test_config_file(host):
    dist = host.system_info.distribution
    f = host.file('/etc/logrotate.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o0644
    assert f.contains('rotate 14')

    if dist == 'centos':
        assert not f.contains('su root')
        assert f.contains('dateext')
    elif dist == 'ubuntu':
        assert f.contains('su root syslog')
        assert not f.contains('dateext')


def test_conf_d_file(host):
    f = host.file('/etc/logrotate.d/example')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o0644

    assert f.contains('/var/log/zdt')
    assert f.contains('/var/log/zerodowntime')
    assert f.contains('missingok')
    assert not f.contains('nocreate')
    assert f.contains('logger zdt-logrotate')
    assert f.contains('notifempty')
    assert f.contains('create')
    assert f.contains('maxsize 30k')
    assert not f.contains(' size')
