import secrets
import binascii
from ecdsa import SigningKey,SECP256k1
import hashlib

def generatePrivateKey():
	number = int(secrets.randbelow(1 << 256))
	while number < 1 or number > 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140:
	    number = secrets.randbelow(1 << 256)
	return binascii.hexlify(number.to_bytes(32, byteorder='big'))

PrivateKey=generatePrivateKey()

def generatePublicKey(privKey):
	bytes_privKey = binascii.unhexlify(privKey)
	return SigningKey.from_string(bytes_privKey, curve=SECP256k1).get_verifying_key().to_string()

PublicKey=generatePublicKey(PrivateKey)

def ripemd160(x):
    d = hashlib.new('ripemd160')
    d.update(x)
    return d

def hash160(x):
    return ripemd160(hashlib.sha256(x).digest())

hashed160Key=binascii.hexlify(PublicKey)

#def get_address_for_P2PKH_payments(pubKey, addr_version=0):
	#pubkey_hex = binascii.unhexlify(pubKey)
	#hashed_key = hash160(pubkey_hex).digest()
	#btc_addr = base58.b58encode_check(addr_version.to_bytes(1, byteorder="big") + hashed_key).decode()
	#return btc_addr

#Final=get_address_for_P2PKH_payments(hashed160Key)

print(str(PrivateKey,encoding="utf-8"))
print(str(hashed160Key,encoding="utf-8"))
