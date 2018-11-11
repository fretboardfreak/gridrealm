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
	@echo "  run : Run a development instance of gridrealm."
	@echo "  drun : Run a development instance of gridrealm with debug enabled."
	@echo "  initdb : Initialize the development database."
	@echo "  removedb : Remove the development database."
	@echo ""
	@echo "Component Build Targets:"
	@echo "  all : Build and compile all project components."
	@echo "  rebuild : Clean, Build and compile all project components."
	@echo "  engine : Build the API Engine component."
	@echo "  client : Build the Client component."
	@echo "  pytests : Build the Python Tests."
	@echo "  assets : Put copy of the asset dir in dist."
	@echo "  scripts: Put copy of each script in dist."
	@echo "  dev-loop: Execute 'clean-dist', 'all' and 'run' targets in order.."
	@echo "  ipy: Run ipython for manual debugging."
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
	@echo "  static : Make static dir inside dist dir."
	@echo "  client-dir : Make client dir inside the static dir."
	@echo ""
	@echo "Install Targets:"
	@echo "  install-dev : install required pkgs for development."
	@echo "  install-py : install python packages with pip."
	@echo "  install-npm : install NPM packages."
	@echo "  install : install gridrealm in the pyvenv."
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
	@echo "  pystyle : execute all three python style tools."
	@echo "  pybuild : Build the python packages into build dir."
	@echo ""
	@echo "Javascript Targets:"
	@echo "  js : use rollup and babel to compile javascript sources."
	@echo ""
	@echo "Documentation Targets:"
	@echo "  doc: Compile the documentation into the dist dir."
	@echo "  docs: alias for doc target"
	@echo "  docbuild: Copy documentation sources into build dir."
	@echo "  doc-html: Build all RST files into HTML files in build dir."
	@echo "  doc-uml: Build all PlantUML descriptions into images in build dir."


# Component build targets

all: client engine pytests doc assets scripts
	date > all

.PHONY: rebuild
rebuild: clean all
	@echo "rebuild target"

engine: pybuild
	cp -r $(BUILD_DIR)/lib/gridrealm $(DIST_DIR)/
	date > engine

pytests: engine
	cp -r $(BUILD_DIR)/lib/tests $(DIST_DIR)/
	date > pytests

client : dist engine static client-dir css js
	mkdir -p dist/gridrealm/templates dist/gridrealm/static/client
	cp src/client/*.html dist/gridrealm/templates/
	cp node_modules/bootstrap/dist/js/bootstrap.min.js \
		dist/gridrealm/static/client/js/
	cp node_modules/jquery/dist/jquery.min.js dist/gridrealm/static/client/js/
	date > client

assets: dist static
	cp -r _assets dist/gridrealm/static/
	date > assets

scripts: dist
	cp -r src/scripts/* $(DIST_DIR)
	date > scripts

.PHONY: run
run :
	pushd dist/ ;\
	sudo ../pyvenv/bin/python gr.py -c ../dev.cfg --public --port 80;\
	popd

.PHONY: drun
drun :
	pushd dist/ ;\
	sudo ../pyvenv/bin/python gr.py -c ../dev.cfg --public --port 80 --debug;\
	popd

.PHONY: initdb
initdb :
	pushd dist/ ;\
	../pyvenv/bin/python gr.py -c ../dev.cfg --initdb --debug;\
	popd

.PHONE: removedb
removedb :
	pushd dist/ ;\
	../pyvenv/bin/python gr.py -c ../dev.cfg --removedb --debug;\
	popd

.PHONY: dev-loop
dev-loop : all drun
	@echo "all target"

.PHONY: ipy
ipy : dist pyvenv
	pushd dist/ ;\
	../pyvenv/bin/ipython ;\
	popd

.PHONY: lot
lot :
	git ls-files | \
		sed -e 's/pylintrc//g' \
				-e 's/gridrealm.postman_collection.json//g' \
				-e 's/package.*json//g' | xargs wc -l

# clean targets

.PHONY: clean-build
clean-build :
	rm -rf $(BUILD_DIR) pybuild pytests engine docbuild doc-uml doc-html \
		css-compile css-prefix css doc all docbuild

.PHONY: clean-dist
clean-dist :
	sudo rm -rf $(DIST_DIR) engine pytests scripts client assets css-prefix \
		doc css static client-dir all js

.PHONY: clean-client
clean-client :
	rm -rf $(DIST_DIR)/gridrealm/templates $(DIST_DIR)/gridrelam/static/client \
		client all client-dir js css css-prefix css-compile

.PHONY: clean-engine
clean-engine : clean-pyc
	rm -rf $(DIST_DIR)/gridrealm client assets css-prefix doc css static \
		client-dir all engine js pybuild

.PHONY: clean-pyc
clean-pyc :
	sudo find dist -name "__pycache__" -exec rm -rf '{}' '+'
	sudo find dist -name "*.pyc" -or -name "*.pyo" -exec rm -rf '{}' '+'

.PHONY: clean-pytests
clean-pytests:
	rm -rf $(DIST_DIR)/tests pytests

.PHONY: clean-doc
clean-doc:
	rm -rf $(DIST_DIR)/gridrealm/static/docs $(BUILD_DIR)/docs \
		doc all doc-html doc-uml docbuild

.PHONY: clean-docs
clean-docs: clean-doc
	@echo ""

.PHONY: clean-assets
clean-assets:
	rm -rf $(DIST_DIR)/gridrealm/static/_assets assets

.PHONY: clean-scripts
clean-scripts:
	# TODO: be smarter than wildcard rm here
	rm -rf $(DIST_DIR)/*.py scripts

.PHONY: clean-pyvenv
clean-pyvenv :
	rm -rf $(PYVENV) install-py install-dev

.PHONY: clean-npm
clean-npm :
	rm -rf node_modules install-npm install-dev

.PHONY: clean
clean : clean-build clean-dist
	@echo "clean target"

.PHONY: clean-all
clean-all : clean clean-pyvenv clean-npm
	rm -rf src/gridrealm.egg-info
	@echo "clean-all target"


# misc targets

build :
	mkdir $(BUILD_DIR)

dist :
	mkdir $(DIST_DIR)

static : engine
	mkdir -p $(DIST_DIR)/gridrealm/static
	date > static

client-dir : static
	mkdir -p $(DIST_DIR)/gridrealm/static/client/js
	mkdir -p $(DIST_DIR)/gridrealm/static/client/css
	date > client-dir


# install targets

.PHONY: install
install : install-dev
	$(PYVENV)/bin/python setup.py install

install-dev : install-npm install-py
	date > install-dev

install-py : pyvenv
	$(PYVENV)/bin/pip install -U pip
	$(PYVENV)/bin/pip install -r dev_requirements.txt -r requirements.txt
	date > install-py

install-npm :
	npm install
	date > install-npm


# css targets

.PHONY: css-lint
css-lint :
	@echo "css-lint target: Not Implemented"

css-compile :
	npx node-sass --include-path node_modules/bootstrap/scss/ \
		src/client/css/gridrealm.scss -o build/client/css/
	date > css-compile

css-prefix :
	npx postcss --use autoprefixer --dir dist/gridrealm/static/client/css/ \
		build/client/css/
	date > css-prefix

css : css-compile css-prefix
	date > css


# python targets

pyvenv :
	python3 -m venv --prompt gr pyvenv

.PHONY: pylint
pylint :
	source $(PYVENV)/bin/activate;\
	$(PYTHON) setup.py pylint;\
	deactivate

.PHONY: pep257
pep257 :
	source $(PYVENV)/bin/activate;\
	$(PYTHON) setup.py pep257;\
	deactivate

.PHONY: pycodestyle
pycodestyle :
	source $(PYVENV)/bin/activate;\
	$(PYTHON) setup.py pycodestyle;\
	deactivate

.PHONY: pystyle
pystyle : pycodestyle pep257 pylint
	@echo "pystyle target"

pybuild :
	source $(PYVENV)/bin/activate;\
	$(PYTHON) setup.py build;\
	deactivate
	date > pybuild


# js targets

js :
	npx rollup -c --no-interop --no-treeshake
	date > js


# Documentation Targets

docbuild : build
	cp -r src/docs $(BUILD_DIR)
	date > docbuild

doc-uml : docbuild
	source $(PYVENV)/bin/activate;\
	find $(BUILD_DIR)/docs -iname "*.puml" \
		-exec ./bin/puml.py --verbose '{}' ';' ;\
	deactivate
	date > doc-uml

doc-html : docbuild
	./bin/buildDocs.sh
	date > doc-html

doc : doc-uml doc-html dist
	mkdir -p $(DIST_DIR)/gridrealm/static/docs ;\
		cp -r $(BUILD_DIR)/docs/* $(DIST_DIR)/gridrealm/static/docs/
	date > doc

.PHONY: docs
docs : doc
	@echo
