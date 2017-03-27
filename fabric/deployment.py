from fabric.api import task, run, cd, hosts, sudo

HOST = "mediacoins@174.138.92.53"

@task
@hosts(HOST)
def deploy():
	with cd('/home/mediacoins/media_coin/'):
		run('git pull')
		run('venv/bin/pip install -r requirements.txt')

	with cd('/home/mediacoins/media_coin/web_app/'):
		run('../venv/bin/python manage.py migrate')
		run('../venv/bin/python manage.py makemigrations')

	sudo('service nginx restart')
