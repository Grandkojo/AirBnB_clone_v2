#!/usr/bin/env bash
#A bash script that sets up servers for deployment

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

mkdir -p /data/
mkdir -p /dat/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

sudo echo "<html>
	<head>
	</head>
	<body>
		holberton alx
	</body>
	</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_Static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server/a location /hbnb_static {alias /data/web_Static/current/;}' /etc/ngnx/sites-enabled/default

sudo servce ngninx restart 
