SHELL:=/usr/bin/env bash
OPENAPI_GENERATOR_CLI_VERSION?=v4.3.1
OPENAPI_CLIENT?=python

.PHONY: all
all:\
 $(addprefix openapi-client/,$(addsuffix /.openapi-generator-ignore,$(OPENAPI_CLIENT)))\

.PHONY: clean
clean:
	rm -rf\
 openapi-client\
 ;

.venv:
	poetry install

openapi-client/% :openapi.yaml
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli:$(OPENAPI_GENERATOR_CLI_VERSION) generate -i /local/$< -g $(shell basename $$(dirname $@)) -o /local/$(shell dirname $@)
	touch $@
