Follow https://ruddra.com/posts/install-mysqlclient-macos/

+ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

+ brew install mysql

+ mysql_secure_installation

+ brew services start mysql | mysql.server start

+ brew install mysql-connector-c `you may brew unlink mysql if got any error, jsut follow the instructions to fix`

Open `/usr/local/bin/mysql_config` and 

change

```
# on macOS, on or about line 112:
# Create options
libs="-L$pkglibdir"
libs="$libs -l "
```

to 

```bash
# Create options
libs="-L$pkglibdir"
libs="$libs -lmysqlclient -lssl -lcrypto"
```

+ xcode-select --install

+ brew install openssl

+ export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/

+ brew unlink mysql

+ brew link --overwrite mysql-connector-c



> but I could not succeed and I fixed as follows. This https://stackoverflow.com/questions/14087598/python-3-importerror-no-module-named-configparser also did not work.
> 
> Later I got `brew info openssl` from https://pypi.org/project/mysqlclient/#downloads and followed what it suggested.


+ brew unlink mysql-connector-c

+ brew link --overwrite mysql

+ pip install mysqlclient



```bash
(venv3.6.7) ➜  mb git:(master) ✗ pip install mysqlclient
Collecting mysqlclient
  Using cached https://files.pythonhosted.org/packages/f4/f1/3bb6f64ca7a429729413e6556b7ba5976df06019a5245a43d36032f1061e/mysqlclient-1.4.2.post1.tar.gz
Building wheels for collected packages: mysqlclient
  Building wheel for mysqlclient (setup.py) ... error
  ERROR: Complete output from command /Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/MB-SUITE-PROJ/venv3.6.7/bin/python3 -u -c 'import setuptools, tokenize;__file__='"'"'/private/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/pip-install-blegkvde/mysqlclient/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/pip-wheel-w7x59j6a --python-tag cp36:
  ERROR: running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.9-x86_64-3.6
  creating build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  copying MySQLdb/__init__.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  copying MySQLdb/_exceptions.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  copying MySQLdb/compat.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  copying MySQLdb/connections.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  copying MySQLdb/converters.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  copying MySQLdb/cursors.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  copying MySQLdb/release.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  copying MySQLdb/times.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
  creating build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
  copying MySQLdb/constants/__init__.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
  copying MySQLdb/constants/CLIENT.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
  copying MySQLdb/constants/CR.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
  copying MySQLdb/constants/ER.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
  copying MySQLdb/constants/FIELD_TYPE.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
  copying MySQLdb/constants/FLAG.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
  running build_ext
  building 'MySQLdb._mysql' extension
  creating build/temp.macosx-10.9-x86_64-3.6
  creating build/temp.macosx-10.9-x86_64-3.6/MySQLdb
  gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g -Dversion_info=(1,4,2,'post',1) -D__version__=1.4.2.post1 -I/usr/local/Cellar/mysql-connector-c/6.1.11/include -I/Library/Frameworks/Python.framework/Versions/3.6/include/python3.6m -c MySQLdb/_mysql.c -o build/temp.macosx-10.9-x86_64-3.6/MySQLdb/_mysql.o
  gcc -bundle -undefined dynamic_lookup -arch x86_64 -g build/temp.macosx-10.9-x86_64-3.6/MySQLdb/_mysql.o -L/usr/local/Cellar/mysql-connector-c/6.1.11/lib -lmysqlclient -lssl -lcrypto -o build/lib.macosx-10.9-x86_64-3.6/MySQLdb/_mysql.cpython-36m-darwin.so
  ld: library not found for -lssl
  clang: error: linker command failed with exit code 1 (use -v to see invocation)
  error: command 'gcc' failed with exit status 1
  ----------------------------------------
  ERROR: Failed building wheel for mysqlclient
  Running setup.py clean for mysqlclient
Failed to build mysqlclient
Installing collected packages: mysqlclient
  Running setup.py install for mysqlclient ... error
    ERROR: Complete output from command /Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/MB-SUITE-PROJ/venv3.6.7/bin/python3 -u -c 'import setuptools, tokenize;__file__='"'"'/private/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/pip-install-blegkvde/mysqlclient/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/pip-record-rl9xojmp/install-record.txt --single-version-externally-managed --compile --install-headers /Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/MB-SUITE-PROJ/venv3.6.7/bin/../include/site/python3.6/mysqlclient:
    ERROR: running install
    running build
    running build_py
    creating build
    creating build/lib.macosx-10.9-x86_64-3.6
    creating build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    copying MySQLdb/__init__.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    copying MySQLdb/_exceptions.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    copying MySQLdb/compat.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    copying MySQLdb/connections.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    copying MySQLdb/converters.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    copying MySQLdb/cursors.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    copying MySQLdb/release.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    copying MySQLdb/times.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb
    creating build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
    copying MySQLdb/constants/__init__.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
    copying MySQLdb/constants/CLIENT.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
    copying MySQLdb/constants/CR.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
    copying MySQLdb/constants/ER.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
    copying MySQLdb/constants/FIELD_TYPE.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
    copying MySQLdb/constants/FLAG.py -> build/lib.macosx-10.9-x86_64-3.6/MySQLdb/constants
    running build_ext
    building 'MySQLdb._mysql' extension
    creating build/temp.macosx-10.9-x86_64-3.6
    creating build/temp.macosx-10.9-x86_64-3.6/MySQLdb
    gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -fno-common -dynamic -DNDEBUG -g -fwrapv -O3 -Wall -arch x86_64 -g -Dversion_info=(1,4,2,'post',1) -D__version__=1.4.2.post1 -I/usr/local/Cellar/mysql-connector-c/6.1.11/include -I/Library/Frameworks/Python.framework/Versions/3.6/include/python3.6m -c MySQLdb/_mysql.c -o build/temp.macosx-10.9-x86_64-3.6/MySQLdb/_mysql.o
    gcc -bundle -undefined dynamic_lookup -arch x86_64 -g build/temp.macosx-10.9-x86_64-3.6/MySQLdb/_mysql.o -L/usr/local/Cellar/mysql-connector-c/6.1.11/lib -lmysqlclient -lssl -lcrypto -o build/lib.macosx-10.9-x86_64-3.6/MySQLdb/_mysql.cpython-36m-darwin.so
    ld: library not found for -lssl
    clang: error: linker command failed with exit code 1 (use -v to see invocation)
    error: command 'gcc' failed with exit status 1
    ----------------------------------------
ERROR: Command "/Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/MB-SUITE-PROJ/venv3.6.7/bin/python3 -u -c 'import setuptools, tokenize;__file__='"'"'/private/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/pip-install-blegkvde/mysqlclient/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/pip-record-rl9xojmp/install-record.txt --single-version-externally-managed --compile --install-headers /Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/MB-SUITE-PROJ/venv3.6.7/bin/../include/site/python3.6/mysqlclient" failed with error code 1 in /private/var/folders/_h/d17s0sg11q74f68sxqnvg1nm0000gn/T/pip-install-blegkvde/mysqlclient/
(venv3.6.7) ➜  mb git:(master) ✗ pip install python3-devel
Collecting python3-devel
  ERROR: Could not find a version that satisfies the requirement python3-devel (from versions: none)
ERROR: No matching distribution found for python3-devel
```

# Finally

```bash
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"
```


```bash
(venv3.6.7) ➜  mb git:(master) ✗ brew info openssl
openssl: stable 1.0.2s (bottled) [keg-only]
SSL/TLS cryptography library
https://openssl.org/
/usr/local/Cellar/openssl/1.0.2q (1,794 files, 12.1MB)
  Poured from bottle on 2019-01-22 at 12:59:50
/usr/local/Cellar/openssl/1.0.2s (1,795 files, 12.0MB)
  Poured from bottle on 2019-06-27 at 18:33:32
From: https://github.com/Homebrew/homebrew-core/blob/master/Formula/openssl.rb
==> Caveats
A CA file has been bootstrapped using certificates from the SystemRoots
keychain. To add additional certificates (e.g. the certificates added in
the System keychain), place .pem files in
  /usr/local/etc/openssl/certs

and run
  /usr/local/opt/openssl/bin/c_rehash

openssl is keg-only, which means it was not symlinked into /usr/local,
because Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries.

If you need to have openssl first in your PATH run:
  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.zshrc

For compilers to find openssl you may need to set:
  export LDFLAGS="-L/usr/local/opt/openssl/lib"
  export CPPFLAGS="-I/usr/local/opt/openssl/include"

For pkg-config to find openssl you may need to set:
  export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"

==> Analytics
install: 740,860 (30 days), 1,802,428 (90 days), 6,611,021 (365 days)
install_on_request: 113,237 (30 days), 239,424 (90 days), 908,039 (365 days)
build_error: 0 (30 days)
```


# Succeeded

```bash
(venv3.6.7) ➜  mb git:(master) ✗ pip install mysqlclient  
Collecting mysqlclient
  Using cached https://files.pythonhosted.org/packages/f4/f1/3bb6f64ca7a429729413e6556b7ba5976df06019a5245a43d36032f1061e/mysqlclient-1.4.2.post1.tar.gz
Building wheels for collected packages: mysqlclient
  Building wheel for mysqlclient (setup.py) ... done
  Stored in directory: /Users/hygull/Library/Caches/pip/wheels/30/91/e0/2ee952bce05b1247807405c6710c6130e49468a5240ae27134
Successfully built mysqlclient
Installing collected packages: mysqlclient
Successfully installed mysqlclient-1.4.2.post1
(venv3.6.7) ➜  mb git:(master) ✗ 
```


```bash
(venv3.6.7) ➜  mb git:(master) ✗ brew unlink mysql-connector-c
Unlinking /usr/local/Cellar/mysql-connector-c/6.1.11... 48 symlinks removed
```

```bash
(venv3.6.7) ➜  mb git:(master) ✗ brew link --overwrite mysql
Linking /usr/local/Cellar/mysql/8.0.13... 87 symlinks created
```

### Random list of commands

```bash
 9990  pip install mysqlclient
 9991  pip install mysqldb
 9992  brew service list
 9993  brew services list
 9994  brew install mysql-connector-c
 9995  brew link mysql-connector-c
 9996  brew services list
 9997  mysql_config
 9998  open /usr/local/bin/
 9999  open /usr/local/bin/mysql_config
10000  /usr/local/Cellar/mysql-connector-c/6.1.11/bin/mysql_config ; exit;
10001  vim /usr/local/bin/mysql_config
10002  sudo vim /usr/local/bin/mysql_config
10003  cat /usr/local/bin/mysql_config
10004  brew install openssl
10005  echo $LIBRARY_PATH
10006  export LIBRARY_PATH=$LIBRARY_PATH:/usr/local/opt/openssl/lib/
10007  echo $LIBRARY_PATH
10008  pip install mysqlclient
10009  xcode-select --install
10010  xcode-select 
10011  xcode-select --install
10012  brew services list
10013  ls
10014  l
10015  ll mb
10016  cat mb/settings.py
10017  ./manage.py runserver
10018  python manage.py migrate
10019  python manage.py runserver
10020  python manage.py createsuperuser
10021  ./manage.py runserver
10022  source ../../venv3.6.7/bin/activate
10023  ls
10024  pip install MySQL-Python
10025  pip install mysqlclient
10026  pip install python3-devel
10027  pip install python3-dev
10028  brew info openssl
10029  echo LDFLAGS
10030  echo $LDFLAGS
10031  echo 'export PATH="/usr/local/opt/openssl/bin:$PATH"' >> ~/.zshrc
10032  export LDFLAGS="-L/usr/local/opt/openssl/lib"
10033  export CPPFLAGS="-I/usr/local/opt/openssl/include"
10034  export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig"
10035  echo $LDFLAGS
10036  echo $CPPLAGS
10037  export CPPFLAGS="-I/usr/local/opt/openssl/include"
10038  echo $CPPLAGS
10039  echo $CPPFLAGS
10040  echo $PKG_CONFIG_PATH
10041  pip install mysqlclient
10042  brew unlink mysql-connector-c
10043  brew link --overwrite mysql
```

