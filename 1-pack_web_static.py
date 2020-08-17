#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


def do_pack():
    """
    Method that generates a .tgz archive from the contents of the web_static
    """

    time = datetime.now()

    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    minute = time.minute
    second = time.second

    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(year, month,
                                                             day, hour,
                                                             minute, second)

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(filename))

    if result.succeeded:
        return filename
