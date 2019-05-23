# from Crypto.PublicKey import RSA


# code = 'nooneknows'

# key = RSA.generate(1024)
# privatekey1 = key.exportKey(passphrase=code, pkcs=8)
# publickey1 = key.publickey().exportKey()


# file_out = open("private1.pem", "wb")
# file_out.write(privatekey1)
# print(privatekey1,'\n')

# file_out = open("public1.pem", "wb")
# file_out.write(publickey1)
# print(publickey1,'\n')
# 
# 
# from Crypto.PublicKey import RSA
# code = 'nooneknows'

# key = RSA.generate(1024)
# private_key = key.export_key(passphrase=code, pkcs=8).decode("utf-8")
# # file_out = open("private1.pem", "wb")
# # file_out.write(private_key)
# print(private_key.split('\n'))

# public_key = key.publickey().export_key(passphrase=code, pkcs=8)
# file_out = open("public1.pem", "wb")
# file_out.write(public_key)
# print(public_key)


# import jwt
# import time

# payload = {'user':'vietstar', 'header':'jsonwebtoken', 'exp': time.time() + 3600}

# privkey = RSA.importKey(open('private.pem', "rb").read(), passphrase=code)
# pubkey =RSA.importKey(open('public.pem', "rb").read(), passphrase=code).exportKey()
# privkey1 = RSA.importKey(open('private1.pem', "rb").read(), passphrase=code).exportKey()
# pubkey1 =RSA.importKey(open('public1.pem', "rb").read(), passphrase=code).exportKey()

# privkey1 = privkey.publickey().export_key()
# print(privkey1)

# public = 'MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgGWuHs+PnLBOThh8PCbz37YwJ+/dTM90hcGTHidtKU0Q3VAB4wCwoWyjxYncjX4tSEuenHmPAP63vaEAMkmR9xkzHINhDDAH5bVah0rTbRjOE4QhZ9fgwlJ7t1tkdDiD+jm6qfGQ8GyzM5NPfOV5h43LOW1jMFAWzoGiwUZlzochAgMBAAE='

# token = jwt.encode(payload, privkey , algorithm='RS256').decode('utf-8')
# print('token: ',token)

# msg = jwt.decode(token, pubkey , algorithms=['RS256'])
# print('msg: ',msg)

# token = jwt.encode(payload, public , algorithm='HS256').decode('utf-8')
# print('token: ',token)

# msg = jwt.decode(token, public , algorithms=['HS256'])
# print('msg: ',msg)
