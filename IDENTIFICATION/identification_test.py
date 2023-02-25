# credit_card_test.py

# Tests to see  the methods in credit_card.py, probabilityfunction.py, and DTE.py


from identification import *
from DTE import *



id_example = '11000020160201010'
secret_key = 2048101736616812280
guess_key =  5496328831800304765

# Create probability
p  = IdentificationProbability()


# Use DTE on identification example
seed = encode(id_example, p)
ciphertext = secret_key ^ seed
decipher_seed = guess_key ^ ciphertext


print ("ID: "+id_example)
print ("CIPHERTEXT: "+str(ciphertext))
print ("GUESSED_SEED: "+str(decipher_seed))

message = decode(decipher_seed, p)
print ("decoded by a guessed seed, returned MESSAGE: "+message)

message = decode(seed, p)
print ("decoded by the right seed, returned MESSAGE: "+message)
