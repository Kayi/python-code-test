from fabric.api import local


def run_manage(command):
    local('/home/ubuntu/.virtualenvs/code-test/bin/python /vagrant/testsite/manage.py %s' % command)


def web():
    run_manage('runserver 0.0.0.0:8888')


def migrate():
    run_manage('migrate')


def make_migrations():
    run_manage('makemigrations')


def requirements():
    local('/home/ubuntu/.virtualenvs/code-test/bin/pip install -r requirements.txt ')


def restore_database():
    local('/home/ubuntu/.virtualenvs/code-test/bin/python /vagrant/testsite/manage.py flush')
    local('/home/ubuntu/.virtualenvs/code-test/bin/python /vagrant/testsite/manage.py loaddata fixtures.json')