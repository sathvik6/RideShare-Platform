import os

API_WRITE_URL = '/api/v1/db/write'

API_READ_URL = '/api/v1/db/read'

API_CRASH_MASTER = 'api/v1/crash/master'

API_CRASH_SLAVE = 'api/v1/crash/slave'

API_LIST_NODES = '/api/v1/worker/list'

API_NOTIFY_ORCHES = os.getenv("DBAAS_NOTIFY_URL", "http://flask-orchestrator:5000/api/v1/notify")

DBAAS_NETWORK = os.getenv("DBAAS_NETWORK", "rideshare_dbaas")