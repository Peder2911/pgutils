from contextlib import contextmanager
import socket

import docker
import psycopg2

from .util import seekport

@contextmanager
def tempPg(*args,**kwargs):
    port = seekport() 

    client = docker.from_env()
    db = client.containers.run("postgres",detach=True,
            environment={"POSTGRES_HOST_AUTH_METHOD":"trust"},
            ports={"5432/tcp":str(port)})
    con = None
    while con is None:
        try:
            con = psycopg2.connect(f"postgres://postgres@0.0.0.0:{port}")
        except:
            pass
    try:
        yield con
    finally:
        con.close()
        db.remove(force=True)
        client.close()
