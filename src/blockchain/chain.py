import copy
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        return Block(0, "0", [], int(time.time()), 0)

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        if len(self.pending_transactions) < 1:
            return False
        new_block = Block(len(self.chain), self.get_latest_block().hash, self.pending_transactions, int(time.time()), 0)
        new_block.sign_block(miner_address)
        self.chain.append(new_block)
        self.pending_transactions = []
        return True

    def get_balance_of_address(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction['from'] == address:
                    balance -= transaction['amount']
                elif transaction['to'] == address:
                    balance += transaction['amount']
        return balance

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
