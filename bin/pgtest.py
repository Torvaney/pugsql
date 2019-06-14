#!/usr/bin/env python

# Here to test postgres-specific stuff until I figure out how to factor that
# with the test suite (if ever)

import pugsql
from getpass import getuser

m = pugsql.module('tests/sql/postgres')
m.connect('postgresql+pg8000://%s@127.0.0.1' % getuser())

print(m.insert_returning(foo='foo'))
print(m.insert_returning_star(foo='foo'))