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
	@echo "  pytests : Build the Python Tests."
	@echo "  assets : Put copy of the asset dir in dist."
	@echo "  scripts: Put copy of each script in dist."
	@echo "  dev-loop: Execute 'clean-dist', 'all' and 'run' targets in order.."
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

.PHONY: all
all: client engine pytests doc assets scripts
	@echo "all target"

.PHONY: engine
engine: pybuild
	cp -r $(BUILD_DIR)/lib/gridrealm $(DIST_DIR)/

.PHONY: pytests
pytests: engine
	cp -r $(BUILD_DIR)/lib/tests $(DIST_DIR)/

.PHONY: client
client : build dist engine static client-dir css js
	mkdir -p dist/gridrealm/templates
	cp src/client/client.html dist/gridrealm/templates/
	cp node_modules/bootstrap/dist/js/bootstrap.min.js \
		dist/gridrealm/static/client/js/
	cp node_modules/jquery/dist/jquery.min.js dist/gridrealm/static/client/js/

.PHONY: assets
assets: dist static
	cp -r _assets dist/gridrealm/static/

.PHONY: scripts
scripts: dist
	cp -r scripts/* $(DIST_DIR)

.PHONY: run
run :
	pushd dist/ ;\
	sudo ../pyvenv/bin/python runGR.py -c ../dev.cfg --public --port 80 --debug;\
	popd

.PHONY: dev-loop
dev-loop: clean-dist all run
	@echo "all target"


# clean targets

.PHONY: clean-build
clean-build :
	rm -rf $(BUILD_DIR)

.PHONY: clean-dist
clean-dist :
	sudo rm -rf $(DIST_DIR)

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

.PHONY: static
static : engine
	mkdir -p $(DIST_DIR)/gridrealm/static

.PHONY: client-dir
client-dir : static
	mkdir -p $(DIST_DIR)/gridrealm/static/client/js
	mkdir -p $(DIST_DIR)/gridrealm/static/client/css


# install targets

.PHONY: install
install : install-dev
	$(PYVENV)/bin/python setup.py install

.PHONY: install-dev
install-dev : install-npm install-py
	@echo "install-dev target"

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
	npx node-sass --include-path node_modules/bootstrap/scss/ \
		src/client/css/gridrealm.scss -o build/client/css/

.PHONY: css-prefix
css-prefix :
	npx postcss --use autoprefixer --dir dist/gridrealm/static/client/css/ \
		build/client/css/

.PHONY: css
css : css-compile css-prefix
	@echo "css target"


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

.PHONY: pybuild
pybuild :
	source $(PYVENV)/bin/activate;\
	$(PYTHON) setup.py build;\
	deactivate


# js targets

.PHONY: js
js :
	npx rollup -c --no-interop --no-treeshake


# Documentation Targets

.PHONY: docbuild
docbuild : build
	cp -r src/docs $(BUILD_DIR)

.PHONY: doc-uml
doc-uml : docbuild
	source $(PYVENV)/bin/activate;\
	find $(BUILD_DIR)/docs -iname "*.puml" \
		-exec ./bin/puml.py --verbose '{}' ';' ;\
	deactivate

.PHONY: doc-html
doc-html : docbuild
	./bin/buildDocs.sh

.PHONY: doc
doc : doc-uml doc-html dist
	mkdir -p $(DIST_DIR)/gridrealm/static/docs ;\
		cp -r $(BUILD_DIR)/docs/* $(DIST_DIR)/gridrealm/static/docs/

.PHONY: docs
docs : doc
	@echo
