##
#
#  Makefile for Gridrealm
#
#  (c) Copyright 2018 - Curtis Sand, Dennison Gaetz - All Rights Reserved
#
###

BUILD_DIR = build
DIST_DIR = dist
PYVENV = pyvenv
PYTHON = pyvenv/bin/python

.PHONY: help
help :
	@echo "Gridrealm Makefile Targets:"
	@echo "  help : Print this message"
	@echo ""
	@echo "Component Build Targets:"
	@echo "  all : Build and compile all project components."
	@echo "  engine : Build the API Engine component."
	@echo "  client : Build the Client component."
	@echo "  pytests: Build the Python Tests."
	@echo ""
	@echo "Clean Targets:"
	@echo "  clean : Clean all built files."
	@echo "  clean-all : Clean all files, including installed packages."
	@echo "  clean-build : Remove the build dir."
	@echo "  clean-dist: Remove the dist dir."
	@echo "  clean-pyvenv: Remove the pyvenv."
	@echo "  clean-node: Remove the local installed node modules."
	@echo ""
	@echo "Misc Targets:"
	@echo "  dist : Make dist dir."
	@echo "  build : Make build dir."
	@echo ""
	@echo "Install Targets:"
	@echo "  install : install required pkgs for development."
	@echo "  install-py : install python packages with pip."
	@echo "  install-npm: install NPM packages."
	@echo ""
	@echo "CSS Targets:"
	@echo "  css : Run both css-compile and css-prefix."
	@echo "  css-lint : run a linter on the CSS stylesheets."
	@echo "  css-compile : compile from SCSS to CSS using SASS."
	@echo "  css-prefix : prefix the CSS sheet using postcss autoprefixer."
	@echo ""
	@echo "Python Targets:"
	@echo "  pyvenv : build a virtualenv for the python install."
	@echo "  pylint : execute the python pylint tool."
	@echo "  pep257 : execute the python pep257 tool."
	@echo "  pycodestyle : execute the python pycodestyle tool."
	@echo "  pybuild : Build the python packages into build dir."
	@echo ""
	@echo "Javascript Targets:"
	@echo "  js : use rollup and babel to compile javascript sources."


# Component build targets

.PHONY: all
all: client engine pytests
	@echo "all target"

.PHONY: engine
engine: pybuild
	cp -r $(BUILD_DIR)/lib/engine $(DIST_DIR)/

.PHONY: pytests
pytests: engine
	cp -r $(BUILD_DIR)/lib/tests $(DIST_DIR)/

.PHONY: client
client : build dist css js
	cp src/client/client.html dist/client/


# clean targets

.PHONY: clean-build
clean-build :
	rm -rf $(BUILD_DIR)

.PHONY: clean-dist
clean-dist :
	rm -rf $(DIST_DIR)

.PHONY: clean-pyvenv
clean-pyvenv :
	rm -rf $(PYVENV)

.PHONY: clean-node
clean-node :
	rm -rf node_modules

.PHONY: clean
clean : clean-build clean-dist
	@echo "clean target"

.PHONY: clean-all
clean-all : clean clean-pyvenv clean-node
	rm -rf src/gridrealm.egg-info
	@echo "clean-all target"


# misc targets

build :
	mkdir $(BUILD_DIR)

dist :
	mkdir $(DIST_DIR)


# install targets

.PHONY: install
install : install-npm install-py
	@echo "install target"

.PHONY: install-py
install-py : pyvenv
	$(PYVENV)/bin/pip install -U pip
	$(PYVENV)/bin/pip install -r dev_requirements.txt -r requirements.txt

.PHONY: install-npm
install-npm :
	npm install


# css targets

.PHONY: css-lint
css-lint :
	@echo "css-lint target"

.PHONY: css-compile
css-compile :
	npx node-sass --include-path node_modules/bootstrap/scss/ src/client/css/gridrealm.scss -o build/client/css/

.PHONY: css-prefix
css-prefix :
	npx postcss --use autoprefixer --dir dist/client/css/ build/client/css/

.PHONY: css
css : css-compile css-prefix
	@echo "css target"


# python targets

pyvenv :
	python3 -m venv --prompt gr pyvenv

.PHONY: pylint
pylint :
	source $(PYVENV)/bin/activate; $(PYTHON) setup.py pylint; deactivate

.PHONY: pep257
pep257 :
	source $(PYVENV)/bin/activate; $(PYTHON) setup.py pep257; deactivate

.PHONY: pycodestyle
pycodestyle :
	source $(PYVENV)/bin/activate; $(PYTHON) setup.py pycodestyle; deactivate

.PHONY: pybuild
pybuild :
	source $(PYVENV)/bin/activate; $(PYTHON) setup.py build; deactivate


# js targets

.PHONY: js
js :
	npx rollup -c
