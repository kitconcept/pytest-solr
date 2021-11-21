SHELL := /bin/bash
SOLR_VERSION := 7.7.3
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: download-solr virtualenv test

download-solr:
	@echo "Download Solr"
	@if [[ ! -f $(CURRENT_DIR)/downloads/solr-$(SOLR_VERSION).tgz  ]]; then \
		wget -P $(CURRENT_DIR)/downloads http://archive.apache.org/dist/lucene/solr/$(SOLR_VERSION)/solr-$(SOLR_VERSION).tgz; \
	else \
		echo "Skip downloading Solr."; \
	fi;
	@if [[ ! -d $(CURRENT_DIR)/downloads/solr-$(SOLR_VERSION)  ]]; then \
		tar xfz $(CURRENT_DIR)/downloads/solr-$(SOLR_VERSION).tgz -C $(CURRENT_DIR)/downloads; \
	else \
		echo "Skip extracting Solr."; \
	fi

virtualenv:
	@echo "Create Virtual Python Environment"
	python3 -m venv .
	bin/pip install -r requirements.txt
	bin/python setup.py develop

clean:
	@echo "Clean"
	rm -rf bin/ lib/ pyvenv.cfg
	find . -name "*.pyc" -exec rm -rf {} \;
	find . -name "__pycache__" -exec rm -rf {} \;

test:
	@echo "Run Tests"
	bin/py.test tests
