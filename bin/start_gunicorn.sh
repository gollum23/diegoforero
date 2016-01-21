#!/bin/sh

NAME="diegoforero"                                  # Name of the application
DIR=""
DJANGODIR=$DIR/diegoforero.xyz             # Django project directory
SOCKFILE=$DIR/diegoforero.xyz/run/gunicorn.sock  # we will communicte using this unix socket
USER=                                        # the user to run as
GROUP=                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=diegoforero.settings.production             # which settings file should Django use
DJANGO_WSGI_MODULE=diegoforero.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
export WORKON_HOME=$DIR/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
workon diegoforero
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export SECRET_KEY_DIEGOFORERO=""
export DATABASE_USER=""
export DATABASE_PASS=""
export DB_DIEGOFORERO=""
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec $DIR/.virtualenvs/diegoforero/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-level=info \
  --bind=unix:$SOCKFILE