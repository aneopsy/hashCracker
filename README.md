# HashCracker -  Crack a Hash by BruteForce.

HashCracker est un outil en Python qui utilise le bruteforce pour craker un hashage.

### Prerequisities

* Python2.7
* Crypto
```
pip install Crypto
```

## Getting Started

```
$ python hashcracker.py
usage: hashcracker.py [-h] [-c] [-k KEY] [-m MSGDGST] [-t] [-p PASSPHRASE]
                      [-v] [-V]

```

Exemple, Cracker un hash sha1: <br />
* Passphrase: test <br />
* Hash:       a94a8fe5ccb19ba61c4c0873d391e987982fbbd3 <br />


```
$ python hashcracker.py -c -k "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3" -m sha1

  Password is:      test
  Hash is:          a94a8fe5ccb19ba61c4c0873d391e987982fbbd3


```
## Running the tests

Il est possible de faire des tests, exemple avec un hash md5:

```
$ python hashcracker.py -t -p "foo" -m md5                                 
  Testing password: foo
  With hash:        acbd18db4cc2f85cedef654fccc4a4d8

  Password is:      foo
  Hash is:          acbd18db4cc2f85cedef654fccc4a4d8
```


## Deployment

HashCracker est compatible sur:

- Linux

## Authors

* **AneoPsy** - *Initial work*

## Acknowledgments

* Cryptographie
* Python
