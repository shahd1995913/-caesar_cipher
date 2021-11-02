# import nltk, re
from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import (decrypt,encrypt,crack,count_words )


def test_version():
    assert __version__ == '0.1.0'


"""
1. encrypt a string with a given shift
2. decrypt a previously encrypted string with the same shift
3. encryption should handle upper and lower case letters
4. encryption should allow non-alpha characters but ignore them, including white space
5. decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.


"""

def test_encrypt():
    data =encrypt('shahd',1)
    expexted ='tibie'
    real=data
    assert expexted==real
    


def test_encrypt_upper():
    data =encrypt('ALI',1)
    expexted ='BMJ'
    real=data
    assert expexted==real    
    
    
def test_decrypt():
    data =decrypt('shahd',1)
    expexted ='rgzgc'
    real=data
    assert expexted==real


def test_encrypt2():
  
    data = encrypt('It was the best of times, it was the worst of times.',3)
    expexted ='Lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv.'
    real=data
    assert expexted==real

def test_count_words():
    
    data =count_words("It was the best of times, it was the worst of times")
    expexted =12
    real=data
    assert expexted==real


