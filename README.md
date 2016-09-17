# HashCracker -  Crack a Hash by BruteForce.

ZipCracker est un outil en Python de crack qui utilise le bruteforce avec un dictionnaire.

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

Exemple, Crack un hash sha1: \n
Passphrase: crypto \n
Hash:       44a9713350e53858f058463d4bf7f1e542d9ca4b\n


```
$ nano test.txt
  Voici un petit test.

$ zip --encrypt test.zip test.txt
  Enter password:
  Verify password:
     adding: test.txt (stored 0%)
$ ls
  test.txt  test.zip  zipcracker.py
```

Lancement du crack:

```
$ python zipcracker.py -f test.zip -w word_list
(2994 / 3107) |  96.00%

Password cracked: nirvana

Took 0.562439 seconds to crack the password. That is, 5325 attempts per second.
```

## Deployment

ZipCracker est compatible sur:

- Linux

## Authors

* **AneoPsy** - *Initial work*

## Acknowledgments

* Python
