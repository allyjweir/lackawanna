Install
=========

This is where you write how to get a new laptop to run this project.

$ vagrant up
$ vagrant ssh
$ cd /vagrant
$ sudo apt-get install libxml2-dev libxslt1-dev python-dev
$ sudo apt-get install libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
$ sudo pip install -r requirement/local.txt (sudo required if no virtualend used)
$ sudo apt-get install npm nodejs
$
(cd /usr/local/share
sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2
sudo tar xjf phantomjs-1.9.7-linux-x86_64.tar.bz2
sudo ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs
sudo ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
sudo ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/bin/phantomjs
cd)
(Currently this is also needed:
  $ sudo python
  $ import nltk
  $ nltk.download('punkt', download_dir='/usr/share/nltk_data')
  $ exit()
)

Database configuration
$ sudo su postgres
$ psql
$ CREATE DATABASE "lackawanna"
  WITH OWNER "postgres"
  ENCODING 'UTF8'
  LC_COLLATE = 'en_US.UTF-8'
  LC_CTYPE = 'en_US.UTF-8'
  TEMPLATE = template0;
$ ALTER ROLE postgres WITH PASSWORD 'lackawannapass';
$ \q
Press CTRL-D to go back to original user
$ python lackawanna/manage.py syncdb
$ python lackawanna/manage.py migrate

Finally to run
$ python lackawanna/manage.py runserver 0.0.0.0:8000
