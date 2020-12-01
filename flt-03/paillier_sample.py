#!/usr/bin/env python3

"""Paillier encryption library for partially homomorphic encryption."""
import random

import phe
from phe import EncodedNumber, paillier
from phe.util import invert, powmod, getprimeover, isqrt
import numpy as np

# test
if __name__ == "__main__":
    public_key, private_key = paillier.generate_paillier_keypair(n_length=10)
    print('pub', public_key.g, public_key.n)
    print('priv', private_key.p, private_key.q)
    A=[3,32]
    print('A', A)
    enA=[public_key.encrypt(x) for x in A]
    print(enA[0].ciphertext(False))
    print(enA[0].ciphertext(False).bit_length())
    B=[4,16]
    print('B', B)
    enB=[public_key.encrypt(x) for x in B]
    print(enB[0].ciphertext(False))
    print(enB[0].ciphertext(False).bit_length())
    en=np.add(enA,enB)
    print(en[0].ciphertext(False))
    print(en[0].ciphertext(False).bit_length())
    for x in en:
        print(private_key.decrypt(x))

  
