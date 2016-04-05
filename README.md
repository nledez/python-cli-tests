Installation
============

```
[ ! -d virtualenv ] && virtualenv virtualenv
./virtualenv/bin/pip install -r requirements.txt
```

Developpment installation
============

```
[ ! -d virtualenv ] && virtualenv virtualenv
./virtualenv/bin/pip install -r requirements-tests.txt
```

Launch tests:
```
./virtualenv/bin/lettuce tests/features
./virtualenv/bin/nosetests --with-xunit --with-coverage --cover-tests --cover-html --cover-xml --cover-tests --cover-package=alice,tests tests/
```
Launch unit tests with sniffer:
```
sniffer -x--with-xunit -x--with-coverage -x--cover-tests -x--cover-html -x--cover-xml -x--cover-tests -x--cover-package=alice,tests tests/
```
