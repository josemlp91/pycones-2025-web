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
Os damos la bienvenida a la PyConES, la conferencia de Python más importante de España.<br><br>
Un evento que reunirá a cientos de entusiastas de Python, una agenda increíble y unas oportunidades de trabajo
maravillosas. <br><br>
También puedes formar parte de nuestros patrocinadores y tener tu espacio dentro del evento.
"""

TWITTER_USERNAME = "pycones"
TWITTER_LINK = f"https://twitter.com/{TWITTER_USERNAME}"
YOUTUBE_LINK = "https://www.youtube.com/PythonEspa%C3%B1aOficial"
GITHUB_LINK = "https://github.com/python-spain"
EMAIL_LINK = "mailto:contacto@2022.es.pycon.org"
TELEGRAM_LINK = "https://t.me/PyConES2022"

TICKETS_LINK = "https://pycones2022.eventbrite.es"
CALL_FOR_PAPERS_LINK = "https://charlas.2022.es.pycon.org/pycones2022/cfp"
SPONSORS_DOSSIER_ES = "/theme/files/dosier_patrocinio_2025_es.pdf"
SPONSORS_DOSSIER_EN = "/theme/files/dosier_patrocinio_2025_en.pdf"

# https://google-map-generator.com/
MAP_IFRAME_LINK = (
    "https://maps.google.com/maps?q=Sevilla&t=&z=17&ie=UTF8&iwloc=&output=embed"
)

# https://cookie-bar.eu/
COOKIES_SCRIPT = "https://cdn.jsdelivr.net/npm/cookie-bar/cookiebar-latest.min.js?forceLang=es&theme=altblack&tracking=1&thirdparty=1&always=1&refreshPage=1&showNoConsent=1"


MAILJET_IFRAME_URL = "#TODO"
MAILJET_TOKEN = "#TODO"

GOOGLE_PHOTOS_URL = "https://photos.app.goo.gl/pw7cdCbHHKwziDDL8"
GOOGLE_PHOTOS_TITLE = "PyCon ES 2025"
GOOGLE_PHOTOS_DESCRIPTION = "PyCon ES 2025"


WALLPAPERS = ["/theme/images/wallpapers/lamparas_arabes.webp"]

SELECTED_WALLPAPER = random.choice(WALLPAPERS)

EVENT_START_DATE_STR = "Del 17 de Octubre"
EVENT_END_DATE_STR = "Al 19 de Octubre"

EVENT_WARNINGS = [
    {
        "message": "En construcción 🛠️",
        "color": "is-danger",  # "is-warning, is-success, is-danger,  is-info"
    }
]
