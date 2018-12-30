import hashlib
import json
from time import time

class BlockChain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        #Create a new block here
        pass

    def new_transaction(self, sender, recipient, amount):
        """Creates a new transaction to go into next block
        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    def hash(block):
        #Hashes of blocks
        pass

    def last_block(self):
        #returns last block in the chain as of now
        pass

    
    
