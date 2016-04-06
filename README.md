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
./virtualenv/bin/pip install -r requirements.txt
./virtualenv/bin/pip install -r requirements-tests.txt
```

Launch tests:
```
./virtualenv/bin/lettuce tests/features
./virtualenv/bin/nosetests --with-xunit --with-coverage --cover-tests --cover-html --cover-xml --cover-tests --cover-package=alice,tests tests/
```
Launch unit tests with sniffer:
```
[ ! -d virtualenv ] && virtualenv virtualenv
./virtualenv/bin/pip install -r requirements.txt
./virtualenv/bin/pip install -r requirements-tests.txt
./virtualenv/bin/pip install -r requirements-dev.txt
```

```
sniffer -x--with-xunit -x--with-coverage -x--cover-tests -x--cover-html -x--cover-xml -x--cover-tests -x--cover-package=alice,tests tests/
```

## Shell helpers

#### Install
```
./install.sh prod # Install prod environement
./install.sh tests # Install tests environement (prod+tests)
./install.sh dev # Install dev environement (prod+tests+dev)
```

#### Launch
```
./launch.sh func # Launch functionnal tests
./launch.sh unit # Launch testunit
./launch.sh tdd  # Launch testunit in TDD mode
```

You can chain commands:
```
./launch.sh func unit
```
