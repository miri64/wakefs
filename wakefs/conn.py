import os
import struct
import socket

def connection_factory():
    connection_type = {
            'local': LocalConnection,
        }
    args = {'path': './test_path'}
    the_class = connection_type['local']
    return the_class(args)

class Connection(object):
    def __new__(type, *args):
        if not '_the_connection' in type.__dict__:
            type._the_connection = object.__new__(type)
        return type._the_connection

    def __init__(self):
        if not '_connected' in dir(self):
            self._connected = True

    def open(self, filename, mode="r", buffering=None):
        raise NotImplemented

class LocalConnection(Connection):
    def __init__(self, path):
        super(LocalConnection, self).__init__()
        self.path = path

    def open(self, filename, mode="r", buffering=None):
        if buffering:
            return open(os.path.join(self.path, filename, mode, buffering))
        else:
            return open(os.path.join(self.path, filename, mode))

    def update(self, model_object):
        # TODO
        print 'Update:', repr(model_object)
