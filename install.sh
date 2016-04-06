#!/bin/bash

function install_prod() {
	if [ ! -f requirements.txt ]; then
		echo "Missing requirements.txt"
		exit 1
	fi
	[ ! -d virtualenv ] && virtualenv virtualenv
	if [ requirements.txt -nt .requirements.txt.install ]; then
		./virtualenv/bin/pip install -r requirements.txt && \
		touch .requirements.txt.install
	else
		echo "Prod virtualenv uptodate"
	fi
}

function install_tests() {
	if [ ! -f requirements-tests.txt ]; then
		echo "Missing requirements-tests.txt"
		exit 1
	fi
	install_prod
	if [ requirements-tests.txt -nt .requirements-tests.txt.install ]; then
		./virtualenv/bin/pip install -r requirements-tests.txt && \
		touch .requirements-tests.txt.install
	else
		echo "Tests virtualenv uptodate"
	fi
}

function install_dev() {
	if [ ! -f requirements-dev.txt ]; then
		echo "Missing requirements-dev.txt"
		exit 1
	fi
	install_tests
	if [ requirements-dev.txt -nt .requirements-dev.txt.install ]; then
		./virtualenv/bin/pip install -r requirements-dev.txt && \
		touch .requirements-dev.txt.install
	else
		echo "Dev virtualenv uptodate"
	fi
}

if [ "$1" = "prod" ]; then
	install_prod
elif [ "$1" = "tests" ]; then
	install_tests
elif [ "$1" = "dev" ]; then
	install_dev
else
	echo "Call me with:"
	echo "$0 <prod|tests|dev>"
fi
