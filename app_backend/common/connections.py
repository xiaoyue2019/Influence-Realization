# -*- coding: utf-8 -*-
#
# Author: xiaoyue
# Email: xiaoyue2019@outlook.com
# Created Time: 2021-12-14
from typing import Iterator
from redis import Redis, ConnectionPool

# redis pool
_redis_pool = None


def init_redis(host: str, port=6379, db=0):
    """set redis """
    global _redis_pool
    _redis_pool = ConnectionPool(host=host, port=port, db=db)


def get_redis() -> Iterator[Redis]:
    """get redis operator
    The current connection is closed after each request is processed,
    and different connections are used for different requests.
    """
    r = Redis(connection_pool=_redis_pool, health_check_interval=30)
    try:
        yield r
    finally:
        r.close()


if __name__ == '__main__':
    import sys
    init_redis(sys.argv[1])
    r = get_redis()
    r = next(r)
    print(r)
    r.set('key', 'val', 10)
    assert str(r.get('key'), encoding='utf8') == 'val'
