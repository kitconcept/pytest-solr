SHELL := /bin/bash
SOLR_VERSION := 6.4.1
CURRENT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

all: bootstrap virtualenv test

bootstrap:
	@echo "Bootstrap"
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
	@if [[ ! -d $(CURRENT_DIR)/.env ]]; then \
		virtualenv $(CURRENT_DIR)/.env; \
		source $(CURRENT_DIR)/.env/bin/activate; \
		pip install -r requirements.txt; \
	else \
		echo "Skip creating virtualenv."; \
	fi

clean:
	@echo "Clean"
	rm -rf .env

test:
	@echo "Run Tests"
	.env/bin/py.test tests

