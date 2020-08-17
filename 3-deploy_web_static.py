#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os.path


env.hosts = ['34.75.190.131', '104.196.128.209']


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

    else:
        return False


def do_deploy(archive_path):
    """Function that distributes an archive to your web servers"""

    if os.path.exists(archive_path) is False:
        return False

    status = True

    upload = put(archive_path, '/tmp/')
    if upload.failed:
        status = False

    archive_name = archive_path.replace("versions/", "")
    directory_name = archive_name.replace(".tgz", "")

    folder = '/data/web_static/releases/{}/'.format(directory_name)

    directory = run("mkdir -p {}".format(folder))
    if directory.failed:
        status = False

    unpack_cmd = 'tar -xzf /tmp/{} -C {}'.format(archive_name, folder)
    unpack = run(unpack_cmd)
    if unpack.failed:
        status = False

    remove = run('rm /tmp/{}'.format(archive_name))
    if remove.failed:
        status = False

    move = run('mv {}web_static/* {}'.format(folder, folder))
    if move.failed:
        status = False

    remove = run('rm -rf {}web_static'.format(folder))
    if remove.failed:
        status = False

    remove = run('rm -rf /data/web_static/current')
    if remove.failed:
        status = False

    link = run('ln -s {} /data/web_static/current'.format(folder))
    if link.failed:
        status = False

    return status


def deploy():
    """Function that creates and distributes an archive to your web servers"""

    path = do_pack()

    if path is False:
        return False

    return do_deploy(path)
