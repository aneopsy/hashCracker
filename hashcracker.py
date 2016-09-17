#!/usr/bin/python

import sys
import os
import hashlib
import argparse


VERSION = '1.0'
AUTHOR = 'AneoPsy'

chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
max = 35
guessing = [-1]


def add2list():

    length = len(guessing)
    guessing[-1] += 1

    if guessing[-1] > max:
        guessing[-1] = 0
        if length > 1:
            guessing[-2] += 1
        else:
            guessing.insert(0, 0)

    if length > 1 and guessing[-2] > max:
        guessing[-2] = 0
        if length > 2:
            guessing[-3] += 1
        else:
            guessing.insert(0, 0)

    if length > 2 and guessing[-3] > max:
        guessing[-3] = 0
        if length > 3:
            guessing[-4] += 1
        else:
            guessing.insert(0, 0)

    if length > 3 and guessing[-4] > max:
        guessing[-4] = 0
        if length > 4:
            guessing[-5] += 1
        else:
            guessing.insert(0, 0)

    if length > 4 and guessing[-5] > max:
        guessing[-5] = 0
        if length > 5:
            guessing[-6] += 1
        else:
            guessing.insert(0, 0)

    if length > 5 and guessing[-6] > max:
        if length > 5:
            guessing[-7] += 1
        else:
            guessing.insert(0, 0)
    return (guessing)


def _runtest(args):

    guessedhash = ''
    mdf = getattr(__import__('hashlib', fromlist=[args.msgdgst]), args.msgdgst)
    if args.passphrase is None:
        password = getpass('Passphrase: ')
    else:
        password = args.passphrase
    hash = mdf(password).hexdigest()
    print ('Testing password: %s \nWith hash:        %s' % (password, hash))
    while guessedhash != hash:
        add2list()
        guessed = ''
        guessedhash = ''
        for each in guessing:
            guessed += chars[each]
            guessedhash = mdf(guessed).hexdigest()
            if args.verbose:
                output = "%*s -> %s\r" % (max, guessed, guessedhash)
                sys.stdout.write(output)
                sys.stdout.flush()

    trueword = ''
    for each in guessing:
        trueword += chars[each]
    print '\nPassword is:      %s \nHash is:          %s' % (trueword,

                                                             guessedhash)


def _runcrack(args):

    guessedhash = ''
    mdf = getattr(__import__('hashlib', fromlist=[args.msgdgst]), args.msgdgst)
    if args.key is None:
        hash = raw_input('Hash Key: ')
    else:
        hash = args.key
    while guessedhash != hash:
        add2list()
        guessed = ''
        guessedhash = ''
        for each in guessing:
            guessed += chars[each]
            guessedhash = mdf(guessed).hexdigest()
            if args.verbose:
                output = "%*s -> %s\r" % (max, guessed, guessedhash)
                sys.stdout.write(output)
                sys.stdout.flush()

    trueword = ''
    for each in guessing:
        trueword += chars[each]
    print '\nPassword is:      %s \nHash is:          %s' % (trueword,
                                                             guessedhash)


def _cli_opts():
    '''
    Parse command line options.
    @returns the arguments
    '''
    mepath = unicode(os.path.abspath(sys.argv[0]))
    mebase = '%s' % (os.path.basename(mepath))

    description = '''
        Implements encryption/decryption that is compatible with openssl
        AES-256 CBC mode.
        '''
    desc = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog=mebase,
                                     formatter_class=desc,
                                     description=description,
                                     )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--crack',
                       action='store_true',
                       help='crack mode')
    parser.add_argument('-k', '--key',
                        action='store',
                        help='hash key')
    parser.add_argument('-m', '--msgdgst',
                        action='store',
                        default='md5',
                        help='message digest (md5, sha, sha1, sha256, sha512),\
                              default is md5')
    group.add_argument('-t', '--test',
                       action='store_true',
                       help='test mode')
    parser.add_argument('-p', '--passphrase',
                        action='store',
                        help='passphrase to hash')
    parser.add_argument('-v', '--verbose',
                        action='count',
                        help='verbose mode')
    parser.add_argument('-V', '--version',
                        action='version',
                        version='%(prog)s v' + VERSION + " by " + AUTHOR)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = _cli_opts()
    try:
        if args.test:
            _runtest(args)
        elif args.crack:
            _runcrack(args)
    except KeyboardInterrupt:
        print "\nExit..."
        sys.exit(1)
