Install
=========

This is where you write how to get a new laptop to run this project.

General config
-----
$ vagrant up
$ vagrant ssh
$ cd /vagrant
$ sudo apt-get install libxml2-dev libxslt1-dev python-dev python-software-properties
$ sudo apt-get install libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
$ sudo pip install -r requirement/local.txt (sudo required if no virtualend used)
$ sudo apt-get install npm nodejs
$ sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox

PhantomJS install
------
$ cd /usr/local/share
$ sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2
$ sudo tar xjf phantomjs-1.9.7-linux-x86_64.tar.bz2
$ sudo ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs
$ sudo ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs
$ sudo ln -s /usr/local/share/phantomjs-1.9.7-linux-x86_64/bin/phantomjs /usr/bin/phantomjs
$ cd

NLTK install
-----
(Currently this is also needed:
  $ sudo python
  $ import nltk
  $ nltk.download('punkt', download_dir='/usr/share/nltk_data')
  $ exit()
)

Elasticsearch install (also makes it run automatically on boot. As required!)
-----
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java7-installer
java -version

$ wget -qO - https://packages.elasticsearch.org/GPG-KEY-elasticsearch | sudo apt-key add -
$ sudo nano /etc/apt/sources.list
Add the following to sources.list: "deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main"
$ sudo apt-get update && sudo apt-get install elasticsearch
$ sudo update-rc.d elasticsearch defaults 95 10
$ sudo /etc/init.d/elasticsearch start


Database configuration
---------
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
