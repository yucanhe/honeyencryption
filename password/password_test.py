# credit_card_test.py

# Tests to see if the methods in credit_card.py, probabilityfunction.py, and DTE.py

from password import *
from DTE import *




pwd_example = '123456'
secret_key = 2048101736616812280
guess_key =  5496328831800304765


id_fxns = TelNOProbabilityFxns()


seed = encode(pwd_example, id_fxns)
ciphertext = secret_key ^ seed
decipher_seed = guess_key ^ ciphertext


print ("PASSWORD: "+pwd_example)
print ("CIPHERTEXT: "+str(ciphertext))

message = decode(decipher_seed, id_fxns)
print ("decoded by the guessed seed, returned MESSAGE: "+message)

message = decode(seed, id_fxns)
print ("decoded by a right seed, returned MESSAGE: "+message)
