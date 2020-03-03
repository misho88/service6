__all__ = [ 'available', 'read', 'show' ]

from pkg_resources import resource_stream, resource_listdir
from os.path import join
from os import environ
from subprocess import run
from natsort import natsorted, ns

available = natsorted(resource_listdir(__name__, 'doc'), alg=ns.IGNORECASE)

def read(name, as_bytes=False):
    with resource_stream(__name__, join('doc', name)) as file:
        data = file.read()
        return data if as_bytes else data.decode()


def show(*names):
    pager = environ.get('PAGER', 'less')
    run(pager, input=show.spacer.join(read(name, True) for name in names))
show.spacer = f"\n{'':#>80}\n".encode()
