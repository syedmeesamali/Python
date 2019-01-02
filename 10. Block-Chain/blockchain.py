import hashlib
import json

import textwrap
import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

class BlockChain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []

        #create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """Creates a new block in the Blockchain

        :param proof: <int> The proof given by proof of work (PoW) algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            }

        self.current_transactions = []
        self.chain.append(block)
        return block

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

    @property
    def last_block(self):
        #returns last block in the chain as of now
        return self.chain[-1]

    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_proof):
        """
        Simple proof of work algorithm
        - Finda number 'p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    #---------------------------------------
    #-------------FLASK AREA ---------------
    #---------------------------------------

    # Instantiate our Node
    app = Flask(__name__)

    #Generate a globally unique address for this node
    node_identifier = str(uuid4()).replace('-', '')

    #Instantiate the Blockchain
    blockchain = Blockchain()


    @app.route('/mine', methods=['GET'])
    def mine():
        #we run proof of work to get the next proof of work

        last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = blockchain.proof_of_work(last_proof)

        #we must receive reward for finding the proof.
        #the sender is "0" to signify that this node has mined a new coin

        blockchain.new_transaction(
            sender = "0",
            recipient = node_identifier,
            amount = 1,
            )
        #Forget the new block by adding it to the chain

        previous_hash = blockchain.hash(last_block)
        block = blockchain.new_block(proof, previous_hash)

        response = {
            'message': "New Block Forged",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
            }

        return jsonify(response), 200

    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        values = request.get_json()
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return "Missing Values", 400

        index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
        response = {'message': f'Transaction will be added to block {index}'}
        return jsonify(response), 201
    

    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
            }
        return jsonify(response), 200

    if __name__ =='__main__':
        app.run(host='0.0.0.0', port=5000)

    @app.route('/transactions/new', methods=['POST'])
    
