PY?=
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_PAGES_BRANCH=gh-pages
GITHUB_PAGES_COMMIT_MESSAGE=Generate Pelican site

export SITEURL=http://localhost:8000

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site:'
	@echo ' '
	@echo 'Uso:'
	@awk -F':.*?# ' '/^[a-zA-Z0-9_-]+:.*?#/{printf "   \033[1;32mmake %-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo '                                                                          '
	@echo 'Establece la variable DEBUG a 1 para activar el modo debug, ej: make DEBUG=1 html'
	@echo 'Establece la variable RELATIVE a 1 para activar URLs relativas'
	@echo '                                                                          '

html: # (re) generate the web site
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean: # remove the generated files
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate: # regenerate files upon modification
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve : .venv install # serve the site at http://localhost:8000
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global: # serve the site as root to $(SERVER):80
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver: # serve and regenerate together
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver-global: # serve and regenerate together as root to $(SERVER):80
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b 0.0.0.0

publish: # generate using production settings
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

github: publish # upload the web site via gh-pages
	ghp-import -m "$(GITHUB_PAGES_COMMIT_MESSAGE)" -b $(GITHUB_PAGES_BRANCH) "$(OUTPUTDIR)" --no-jekyll
	git push origin $(GITHUB_PAGES_BRANCH)

compose-up: # start the docker container
	docker compose up


.PHONY: html help clean regenerate serve serve-global devserver devserver-global publish github
