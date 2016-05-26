from fabric.api import env, run, put
# the user to use for the remote commands
env.user = 'aclabs'
# the servers where the commands are executed
env.hosts = ['labs.andrei-coman.com']
REPO_TO_CLONE = "https://github.com/comandrei/DLP/"

def provision():
    deps = ["nginx", "postgresql", "python-dev"]
    run("sudo apt-get update")
    run("sudo apt-get install {} --assume-yes".format(" ".join(deps)))

def configure():
    put("nginx.conf", "/tmp/dlp.nginx.conf")
    put("gunicorn.conf", "/tmp/gunicorn.conf")
    run("sudo mv /tmp/gunicorn.conf /etc/init/gunicorn.conf")
    run("sudo mv /tmp/dlp.nginx.conf /etc/nginx/sites-enabled/dlp.conf")
    run("sudo service nginx restart")

def deploy():
    run("cd DLP; git pull")
    run("deployed/bin/pip install -r DLP/dlp/requirements.txt")
    run("deployed/bin/python DLP/dlp/manage.py migrate")
    run("sudo service gunicorn restart")

def first_deploy():
    run("rm -rf deployed")
    run("rm -rf DLP")
    run("git clone {}".format(REPO_TO_CLONE))
    run("virtualenv deployed --python=$(which python3)")
    deploy()
