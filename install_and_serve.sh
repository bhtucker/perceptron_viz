pip install .
cd viz && npm install && npm run build && cd ..
uwsgi --http :9090 --wsgi-file wsgi.py --master --processes 2 --threads 1 --stats 127.0.0.1:9191 --sharedarea 5
