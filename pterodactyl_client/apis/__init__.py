
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from pterodactyl_client.api.account_api import AccountApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from pterodactyl_client.api.account_api import AccountApi
from pterodactyl_client.api.client_api import ClientApi
from pterodactyl_client.api.databases_api import DatabasesApi
from pterodactyl_client.api.locations_api import LocationsApi
from pterodactyl_client.api.nests_api import NestsApi
from pterodactyl_client.api.nests_eggs_api import NestsEggsApi
from pterodactyl_client.api.nodes_api import NodesApi
from pterodactyl_client.api.server_api import ServerApi
from pterodactyl_client.api.server_database_api import ServerDatabaseApi
from pterodactyl_client.api.users_api import UsersApi
