# -*- coding: utf-8 -*-
from datetime import datetime
import pytz


from pelicanconf_flags import *

AUTHOR = "Python España Org"
SITENAME = "PyConES 2025 Sevilla"
PATH = "content"
THEME = "theme"
PLUGIN_PATHS = ["plugins"]

TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "es"
DEFAULT_DATE_FORMAT = "%d/%M/%Y"
MARKUP = ("md",)
PLUGINS = ["i18n_subsites", "assets"]
STATIC_PATHS = ["images", "extra/manifest.json"]
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n", "extensions.gphotos.GPhotosExtension"],
}


DIRECT_TEMPLATES = [
    "index",
    "blog",
    "keynoters",
    "sponsorship",
    "schedule",
    "gallery",
    "past_editions",
    "organizers",
    "jobs",
]

MENUITEMS_NAVBAR = {
    "La ciudad": {
        "Sevilla": "/pages/sevilla.html",
        "Cómo llegar": "/pages/how-to-arrive.html",
        "UPO": "/pages/upo.html"
    },
    "Organización": {"Equipo": "/organizers.html"},
    "Código de Conducta": "/pages/code-of-conduct.html"
}


if ENABLED_SPEAKERS:
    MENUITEMS_NAVBAR["Ponentes"] = "/keynoters.html"

if ENABLED_SPONSORSHIPS:
    MENUITEMS_NAVBAR["Patrocinios"] = "/sponsorship.html"

if ENABLED_FINANCIAL_AID:
    MENUITEMS_NAVBAR["Becas"] = "/becas.html"

if ENABLED_TIMETABLE:
    MENUITEMS_NAVBAR["Horario"] = "/schedule.html"

if ENABLED_GALLERY:
    MENUITEMS_NAVBAR["La ciudad"]["Galería"] = "/gallery.html"

if ENABLED_PAST_EDITIONS:
    MENUITEMS_NAVBAR["Organización"]["Ediciones pasadas"] = "/past_editions.html"

if ENABLED_JOBS:
    MENUITEMS_NAVBAR["Ofertas de trabajo"] = "/jobs.html"

if ENABLED_BLOG:
    MENUITEMS_NAVBAR["Blog"] = "/blog.html"


NAVBAR_STYLE = "is-primary"
THEME_LOGO = "/theme/images/logos/ICONO_ORIGINAL.png"  # navbar
MAIN_LOGO = "/theme/images/logos/PYCONES_CORTADO.png"  # logo principal
MAIN_LOGO_PNG = "/theme/images/logos/PYCONES_ORIGINAL_AZUL.png"  # logo que se muestra en redes sociales


FOOTER = "Copyright © Python España & PyConES 2025 Org"
THEME_COLOR = "#0E749CFF"
LAST_UPDATE = datetime.now(pytz.timezone(TIMEZONE)).strftime("%B %d, %Y %A, %H:%M:%S")
