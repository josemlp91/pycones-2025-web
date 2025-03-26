# -*- coding: utf-8 -*-
import json
import random


def load_json_from_data(filename):
    with open(f"./data/{filename}", "r", encoding="utf-8") as file:
        return json.load(file)


JOBS = load_json_from_data("jobs.json")
TEAM = load_json_from_data("team.json")
VOLUNTEERS = load_json_from_data("volunteers.json")
PAST_EDITIONS = load_json_from_data("past_editions.json")
SPONSORS = load_json_from_data("sponsors.json")
KEYNOTERS = load_json_from_data("keynoters.json")


EVENT_TITLE = "PyConES 2025"
EVENT_SUBTITLE = "Sevilla"
EVENT_DESCRIPTION_MINI = "PyConES, la conferencia de Python más importante de España"
EVENT_DESCRIPTION = """
¡Bienvenidos a PyConES, la conferencia de Python más importante de España! <br><br>
Únete a cientos de apasionados de Python en un evento único, con una agenda increíble, oportunidades profesionales excepcionales y un ambiente inmejorable. <br><br>
Si quieres llevar tu empresa al siguiente nivel, conviértete en patrocinador y consigue visibilidad exclusiva dentro del evento. ¡Te esperamos!
"""

TWITTER_LINK = "https://x.com/PyConEs"
YOUTUBE_LINK = "https://www.youtube.com/PythonEspa%C3%B1aOficial"
GITHUB_LINK = "https://github.com/python-spain"
EMAIL_LINK = "mailto:contacto@2025.es.pycon.org"
LINKEND_LINK = "https://es.linkedin.com/company/python-espa%C3%B1a?trk=public_post_feed-actor-name"
TELEGRAM_LINK = None
INSTAGRAM_LINK = "https://www.instagram.com/pycon_es/"
BLUESKY_LINK = "https://web-cdn.bsky.app/profile/did:plc:irbbd7hhbmqhoklzmlfx2sju"
# MASTODON_LINK = "https://fosstodon.org/@pycones"

TICKETS_LINK = "https://pycones2025.eventbrite.es"
CALL_FOR_PAPERS_LINK = "https://charlas.2025.es.pycon.org/pycones2022/cfp"
SPONSORS_DOSSIER_ES = "/theme/files/dosier_patrocinio_2025_es.pdf"
SPONSORS_DOSSIER_EN = "/theme/files/dosier_patrocinio_2025_en.pdf"

# https://google-map-generator.com/
MAP_IFRAME_LINK = (
    "https://maps.google.com/maps?q=Sevilla&t=&z=17&ie=UTF8&iwloc=&output=embed"
)

# https://cookie-bar.eu/
COOKIES_SCRIPT = None


MAILJET_IFRAME_URL = None
MAILJET_TOKEN = None

GOOGLE_PHOTOS_URL = "https://photos.app.goo.gl/pw7cdCbHHKwziDDL8"
GOOGLE_PHOTOS_TITLE = "PyCon ES 2025"
GOOGLE_PHOTOS_DESCRIPTION = "PyCon ES 2025"


WALLPAPERS = [
    "/theme/images/assets/fondo_oscuro.png",
]

SELECTED_WALLPAPER = random.choice(WALLPAPERS)

EVENT_START_DATE_STR = "Del 17 de Octubre"
EVENT_END_DATE_STR = "el 19 de Octubre"

EVENT_WARNINGS = [
    # {
    #     "message": "En construcción 🛠️",
    #     "color": "is-danger",  # "is-warning, is-success, is-danger,  is-info"
    # }
]
