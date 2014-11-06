Install
=========

This is where you write how to get a new laptop to run this project.

$ vagrant up
$ vagrant ssh
$ cd /vagrant
$ mkvirtualenv proj
$ pip install -r requirement/local.txt (sudo required if no virtualend used)
(Currently this is also needed:
  $ sudo python
  $ import nltk
  $ nltk.download('punkt', download_dir='/usr/share/nltk_data')
  $ exit()
)

Database configuration
$ sudo su postgres
$ psql
$ CREATE DATABASE lackawanna;
$ ALTER ROLE postgres WITH PASSWORD 'lackawannapass';
$ \q
Press CTRL-D to go back to original user
$ python lackawanna/manage.py syncdb
$ python lackawanna/manage.py migrate

Finally to run
$ python lackawanna/manage.py runserver 0.0.0.0:8000
