import os

if 'RAFIKA_ENV' in os.environ:
	if os.environ['RAFIKA_ENV'] == 'staging':
		from . staging import *
	else:
		from . production import *
else:
	from . local import *
