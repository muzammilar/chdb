"""Removed: the chDB clickhouse-connect backend now lives in clickhouse-connect.

chDB used to ship its own clickhouse-connect execution backend here and
advertise it through the ``clickhouse_connect.backends`` entry point. Since
clickhouse-connect 1.6.0 the backend ships in clickhouse-connect itself, and
the entry-point mechanism this module plugged into is gone, so the two copies
were never going to stay in step. clickhouse-connect is now the single owner.

Importing this module raises :class:`ImportError` with the migration path
rather than failing as a bare "no module named" further down the stack.
See https://github.com/chdb-io/chdb/issues/633.
"""

_MESSAGE = (
    "chdb.cc_backend has been removed. The clickhouse-connect backend for chDB is now "
    "maintained in clickhouse-connect itself (1.6.0 and later).\n"
    "\n"
    "Install:  pip install 'clickhouse-connect[chdb]'\n"
    "Use:      import clickhouse_connect\n"
    "          client = clickhouse_connect.get_client(interface='chdb')\n"
    "          client = clickhouse_connect.get_client('chdb://memory')\n"
    "\n"
    "The chdb[clickhouse-connect] extra and the clickhouse_connect.backends entry point "
    "were removed along with this module."
)

raise ImportError(_MESSAGE)
