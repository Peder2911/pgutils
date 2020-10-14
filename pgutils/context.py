import socket

import docker
import psycopg2

from .util import seekport


class TempPg():
    def __init__(self,initialization):
        port = seekport()
        self._client = docker.from_env()
        self._db = self._client.containers.run("postgres",detach=True,
                environment={"POSTGRES_HOST_AUTH_METHOD":"trust"},
                ports={"5432/tcp":str(port)})
        con = None
        while con is None:
            try:
                con = psycopg2.connect(f"postgres://postgres@0.0.0.0:{port}")
            except:
                pass
        self.con = con
        if initialization:
            self.con.cursor().execute(initialization)

    def __enter__(self):
        pass

    def __exit__(self,type,value,traceback):
        self.con.close()
        self._db.remove(force=True)
        self._client.close()
