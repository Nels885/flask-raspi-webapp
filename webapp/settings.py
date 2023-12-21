import os

SOFTWARE = "WebApp"

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(32)])
SECRET_KEY = 'q2sb*vqltbpi59f#l2c&mak*%h&xzv1)i^#e0_as^cmx^-9)8x'

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Constance module configuration
CONSTANCE_CONFIG = {
    # Config global
    "JIG_NAME": ("WebApp", "Nom du JIG"),
    "CLOCK_DOWN": (1445, "Heure d'extinction"),
    "TIMER": (15, "Delais avant extinction"),
    "SHUTDOWN": (1, "Status extinction"),

    # Config Network
    "API_URL": ("", "Url API"),
    "API_TOKEN": ("", "Token API"),
    "NTP_SERVER": ("fr.pool.ntp.org", "Serveur NTP"),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'GLOBAL': (
        'JIG_NAME', 'CLOCK_DOWN', 'TIMER', 'SHUTDOWN'
    ),
    'NETWORK': (
        'API_URL', 'API_TOKEN', 'NTP_SERVER'
    )
}
