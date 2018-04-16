# To start the Control Flask App
ENV/bin/uwsgi --socket 127.0.0.1:5001 --protocol=http -w wsgi:app