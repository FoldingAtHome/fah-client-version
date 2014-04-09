import os
import inspect


def FAHClientVersion(env):
    path = inspect.getfile(inspect.currentframe())
    path = os.path.dirname(os.path.abspath(path))
    version = open(path + '/../../version.txt', 'r').read().strip()

    env.Replace(PACKAGE_VERSION = version)

    return version


def generate(env):
    env.AddMethod(FAHClientVersion)


def exists(env):
    return 1
