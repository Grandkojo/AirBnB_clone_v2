#!/usr/bin/python3
""" A script to create an archive using fabric """

from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """A function script to generate archive"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -csvf versions/web_static_{}.tgz web_Static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Excepton as e:
        return None
