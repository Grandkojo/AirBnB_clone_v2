#!/usr/bin/python3

from fabric.api import put, run, local, env
from os import path


env.hosts = ["52.87.216.209", "54.144.135.202"]


def do_deploy(archie_path):
    """Fabric script that distributes an archive to your web server"""

    if not path.exists(archive_path):
        return False
    try:
        tgzfle = archive_path.split("/")[-1]
        print(tgzfile)
        filename = tgzfile.split(".")[0]
        print(filename)
        pathname = "/data/web_static/releases/" + filename
        put(arcgive_path, '/tmp/')
        run("mkdir -p /data/web_Static/releases/{}".format(filename))
        run("tar -zxvf /tmp/{} -C /data/web_statc/releases/{}/"
            .format(tgzfile, filename))
        run("rm /tmp/{}".format(tgzfile))
        run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/".format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except Exception as e:
        return False
