Deploy
========

Deployment is completed using Heroku and AWS S3 for storage.

*TODO:* Add details about making accounts for these, configuring S3 suitably and making sure that everything is secure on the developers end.


Run these commands to deploy the project to Heroku:

.. code-block:: bash

    heroku create --buildpack https://github.com/ddollar/heroku-buildpack-multi
    heroku addons:add heroku-postgresql:dev
    heroku addons:add pgbackups:auto-month
    heroku addons:add sendgrid:starter
    heroku addons:add memcachier:dev
    heroku addons:add bonsai
    heroku addons:add papertrail
    heroku pg:promote DATABASE_URL
    heroku config:set DJANGO_CONFIGURATION=Production
    heroku config:set DJANGO_SECRET_KEY=RANDOM_SECRET_KEY_HERE
    heroku config:set DJANGO_AWS_ACCESS_KEY_ID=YOUR_AWS_ID_HERE
    heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY_HERE
    heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=YOUR_AWS_S3_BUCKET_NAME_HERE
    heroku config:set LACKAWANNA_ELASTICSEARCH_INSTANCE=BONSAI_URL_HERE (not working yet)
    git push heroku master
    heroku run python lackawanna/manage.py migrate
    heroku run python lackawanna/manage.py createsuperuser
    heroku open
