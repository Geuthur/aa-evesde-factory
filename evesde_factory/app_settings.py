"""
App Settings
"""

# Django
from django.conf import settings

# Set Naming on Auth Hook
EVESDE_FACTORY_APP_NAME = getattr(
    settings, "EVESDE_FACTORY_APP_NAME", "AA EVE SDE Factory"
)

# Task Settings
# Global timeout for tasks in seconds to reduce task accumulation during outages.
EVESDE_FACTORY_TASKS_TIME_LIMIT = getattr(
    settings, "EVESDE_FACTORY_TASKS_TIME_LIMIT", 1200
)  # 20 minutes

# Maximum Number of Objects processed per run of DJANGO Batch Method
# Controls how many database records are inserted in a single batch operation.
# If you encounter "Got a packet bigger than 'max_allowed_packet' bytes" errors,
# reduce this value (e.g., to 250 or 100).
# Can be increased for better performance if your MySQL max_allowed_packet setting
# is configured higher (default is usually 16-64MB).
EVESDE_FACTORY_BULK_BATCH_SIZE = getattr(
    settings, "EVESDE_FACTORY_BULK_BATCH_SIZE", 500
)
