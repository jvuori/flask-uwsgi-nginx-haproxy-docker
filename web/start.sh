#!/bin/bash
service nginx restart
exec uwsgi --ini app.ini
