# import rsa

# (pubkey, privkey) = rsa.newkeys(512)

# with open('private.pem', mode='rb') as privatefile:
# keydata = privatefile.read() 
# privkey = rsa.PrivateKey.load_pkcs1(keydata)

#print (privkey)
# print (pubkey)

# message = 'we try for hidden message'.encode('utf8')
# signature = rsa.sign(message, privkey, 'SHA-256')
# print('signature: ',signature)

# verified = rsa.verify(message, signature, pubkey)
# print('verified: ',verified)

# token = rsa.encrypt(message, pubkey)
# print('token: ',token)

# response = rsa.decrypt(token, privkey)
# print('msg: ',response)
import jwt
import time

payload = {'user':'vietstar', 'header':'jsontoken', 'exp': time.time() + 3600}

privkey = open('private.key').read()
pubkey = open('public.key').read()

public = 'MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgGWuHs+PnLBOThh8PCbz37YwJ+/dTM90hcGTHidtKU0Q3VAB4wCwoWyjxYncjX4tSEuenHmPAP63vaEAMkmR9xkzHINhDDAH5bVah0rTbRjOE4QhZ9fgwlJ7t1tkdDiD+jm6qfGQ8GyzM5NPfOV5h43LOW1jMFAWzoGiwUZlzochAgMBAAE='

# token = jwt.encode(payload, privkey , algorithm='RS256').decode('utf-8')
# print('token: ',token)

# msg = jwt.decode(token, pubkey , algorithms=['RS256'])
# print('msg: ',msg)

token = jwt.encode(payload, public , algorithm='HS256').decode('utf-8')
print('token: ',token)

msg = jwt.decode(token, public , algorithms=['HS256'])
print('msg: ',msg)
