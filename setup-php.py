#!/usr/bin/env python
git = 'https://github.com/ManhHaHY/setup/archive/master.zip'

modules = [
    'nginx',
    'php',
]

app = {
    'app': 'sample'
}

ftp = {
    'username': 'sample',
    'password': '12345'
}

from os import *

tmp = path.abspath(curdir)

paths = {
    'package': path.realpath(tmp)+'/setup-master',
    'module': path.realpath(tmp)+'/setup-master/modules',
    'config': path.realpath(tmp)+'/setup-master/config',
    'host': '/home',
}


def res(file_name):
    return paths['config'] + '/' + file_name


configs = {
    'php': [
        'cp -r '+res('php.ini') + ' /etc/php.ini',
        'rm -rf /etc/php.d/json.ini'
    ],
    'nginx': [
        'cp -r '+res('nginx.conf') + ' /etc/nginx/nginx.conf',
        'cp -r '+res('nginx_default.conf') + ' /etc/nginx/conf.d/default.conf'
    ]
}


def run(cmd):
    system(cmd)


def load():
    run('cd '+tmp)
    run('yum install -y unzip wget')
    run('wget '+git+' -O setup-master.zip')
    run('rm -rf ./setup-master')
    run('unzip ./setup-master.zip')
    run('rm -rf setup-master.zip')
    run('chmod +x ./setup-master/modules/*')


def main():
    load()
    run('cd '+tmp)

    for module in modules:
        module_path = paths['module'] + '/' + module+'.sh'
        run('sh '+module_path)
        if module in configs.keys():
            for cmd in configs[module]:
                run(cmd)

    run('chmod +x '+paths['package'] + '/service.py')
    run('mv '+paths['package'] + '/service.py /usr/bin/app')
    run('rm -rf '+tmp+'/setup-master')

main()
