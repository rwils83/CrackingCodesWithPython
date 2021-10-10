from chapter4.reverse_cipher import ReverseCipher as rc
from chapter5.ceaserCipher import CaesarCipher as cc
from chapter6.caesarcipherbruteforcer import BruteForcer as bf
from chapter7.transpositionCipher import TranspostionCipher as tc
import argparse as a


def arg_parse():
    description = "blah"
    parser = a.ArgumentParser()

    modes = parser.add_argument_group("modes")

    modes.add_argument("-rs", "--reversestring", action="store_true", help="blah")
    modes.add_argument("-cc", "--caesarcipher", action="store_true", help="blah")
    modes.add_argument("-bf", "--bruteforce", action="store_true", help="blah")
    modes.add_argument("-tc", "--transpositioncipher", action="store_true", help="blah")
    parser.add_argument("-k", "--key", action="store", help="blah")
    parser.add_argument("-m", "--message", action="store", help="blah")
    parser.add_argument("-d", "--decrypt", action="store_true", help="blah")
    parser.add_argument("-e", "--encrypt", action="store_true", help="blah")
    parser.add_argument("-if", "--inputfile", action="store", help="blah")
    parser.add_argument("-of", "--outfile", action="store", help="blah")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = arg_parse()
    if args.reversestring:
        if args.message is not None:
            print(rc(args.message).transform_message())
        elif args.inputfile is not None and args.outfile is not None:
            rc(None).transform_file(args.inputfile, args.outfile)
        else:
            print("Please use correctly")

    if args.caesarcipher:
        if args.message is not None and args.encrypt:
            print(cc(args.message, int(args.key), "encrypt").transform_message())
        elif args.message is not None and args.decrypt:
            print(cc(args.message, int(args.key), "decrypt").transform_message())
        elif args.inputfile is not None and args.outfile is not None and args.encrypt:
            print(cc(None, int(args.key), "encrypt").transform_file(args.inputfile, args.outfile))
        elif args.inputfile is not None and args.outfile is not None and args.decrypt:
            print(cc(None, int(args.key), "decrypt").transform_file(args.inputfile, args.outfile))
        else:
            if args.key is None:
                print("You must choose a key")
            elif args.message is None:
                print("You must give the message to encrypt/decrypt")
            elif not args.encrypt and not args.decrypt:
                print("You must choose to encrypt or decrypt the message")
    if args.bruteforce:
        if args.message is not None:
            bf(args.message).brute_force()
        else:
            print("You must provide a message to brute force")

    if args.transpositioncipher:
        if args.message is not None and args.encrypt and args.key is not None:
            print(tc(args.message, int(args.key)).transform())
        elif args.message is not None and args.decrypt and args.key is not None:
            print(tc(args.message, int(args.key)).decrypt())
