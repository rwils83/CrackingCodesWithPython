# Cracking Codes with Python

## What is it?
A work through of the book Cracking Codes with Python

## I read the book, this isn't the example code from it
Yeah, writing a bunch of singular app files wasn't how I wanted to do it. So I went a slightly more OOP route.

## How can I help?
:shrug: I mean, it is a walkthrough of a book. I don't think there is much to do after the book is done. Although I may
go through and create a different release with a bit more of a proper setup for fun.

## How do I use it?
usage: main.py [-h] [-rs] [-cc] [-bf] [-tc] [-k KEY] [-m MESSAGE] [-d] [-e] [-if INPUTFILE] [-of OUTFILE]

Different cipher stuff from the book Cracking Codes with Python  

optional arguments:  
  -h, --help            show this help message and exit  

modes:  
  -rs, --reversestring  Performs a basic string reversal. Use with -if and -of to reverse an entire text file.  
  -cc, --caesarcipher   Performs a basic Caesar cipher. Returns all lower case letters. Requires: -k/--key <key> and -m/--message <message>. Use with -if and -of to do an entire file.  
  -bf, --bruteforce     Use to bruteforce a cipher_text created with a Caesar cipher if the key is not known.  
  -tc, --transpositioncipher
                        Use for a Transposition cipher. Requires -m <message> -k <key>, use with -if and -of to do an entire file  

inputs:  
  -m MESSAGE, --message MESSAGE  
                        Message to decrypt/encrypt.   
  -if INPUTFILE, --inputfile INPUTFILE
                        Full path to file to decrypt/encrypt  
  -of OUTFILE, --outfile OUTFILE
                        Full path to file for result of decrypting/encrypting -if.  

required:  
  -k KEY, --key KEY     The key for a Caesar or Transposition Cipher. Required to be of type int  
  -d, --decrypt         Set mode to decrypt.  
  -e, --encrypt         Set mode to encrypt  
