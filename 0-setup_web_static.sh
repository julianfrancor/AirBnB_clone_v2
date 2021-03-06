#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
# Ask if it's intalled otherwise Install Nginx if it not already installed

if ! command -v nginx &> /dev/null; then
    sudo apt-get -y update
    sudo apt-get install -y nginx
    sudo ufw allow "Nginx HTTP"
fi

# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/releases/ if it doesn’t already exist
# Create the folder /data/web_static/shared/ if it doesn’t already exist
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Create a fake HTML file, with simple content, to test your Nginx configuration
printf %s "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
" > /data/web_static/releases/test/index.html

# Create a symbolic link,If the symbolic link already exists, it should be deleted and recreated every time the script is ran.
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Recursively Change the File Ownership
chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '29a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Nginx restart after updating the configuration
sudo service nginx restart
