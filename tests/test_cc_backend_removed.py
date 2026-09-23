"""`chdb.cc_backend` is a tombstone, not a live module.

The clickhouse-connect backend moved into clickhouse-connect (chdb-io/chdb#633).
The module file stays behind only so that code still importing it gets the
migration path instead of a bare "no module named chdb.cc_backend". This test
pins that: the import must fail, and the message must name the replacement.

The module is loaded from its file rather than via `import chdb.cc_backend`, so
the check does not also depend on the compiled engine being importable.
"""

import importlib.util
import os
import unittest

_MODULE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "chdb", "cc_backend.py"
)


class TestCcBackendRemoved(unittest.TestCase):
    def test_import_raises_with_migration_path(self):
        spec = importlib.util.spec_from_file_location("chdb_cc_backend_tombstone", _MODULE_PATH)
        module = importlib.util.module_from_spec(spec)

        with self.assertRaises(ImportError) as ctx:
            spec.loader.exec_module(module)

        message = str(ctx.exception)
        self.assertIn("clickhouse-connect[chdb]", message)
        self.assertIn("interface='chdb'", message)
        self.assertIn("get_client", message)


if __name__ == "__main__":
    unittest.main()
