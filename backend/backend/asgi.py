# ========================================================================
import os

from django.core.asgi import get_asgi_application

import multiprocessing

# ========================================================================

WORKER_COUNT = (multiprocessing.cpu_count() * 2) + 1
THREAD_COUNT = int(WORKER_COUNT / 2)
# ========================================================================
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

application = get_asgi_application()
