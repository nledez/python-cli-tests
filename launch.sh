#!/bin/bash

MODULES_2_COVER="alice"

function launch_unittest() {
	./install.sh tests
	./virtualenv/bin/nosetests --with-xunit --with-coverage --cover-tests --cover-html --cover-xml --cover-tests --cover-package=${MODULES_2_COVER},tests tests/
}

function launch_functionaltests() {
	./install.sh tests
	./virtualenv/bin/lettuce tests/features
}

function launch_sniffer () {
	./install.sh dev
	sniffer -x--with-xunit -x--with-coverage -x--cover-tests -x--cover-html -x--cover-xml -x--cover-tests -x--cover-package=${MODULES_2_COVER},tests tests/
}

if [ "$1" = "" ]; then
	echo "Please call me with:"
	echo "$0 func|unit|tdd"
fi

for launch_type in $*; do
	if [ "$launch_type" = "func" ]; then
		launch_functionaltests
	elif [ "$launch_type" = "unit" ]; then
		launch_unittest
	elif [ "$launch_type" = "tdd" ]; then
		launch_sniffer
	fi
done
