#!/bin/bash
service nginx start
exec uwsgi --ini app.ini
