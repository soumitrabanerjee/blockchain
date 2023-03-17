my_blockchain = Blockchain()

# Add a block with a transaction
my_blockchain.add_block(Block(1, ["Transaction 1"], time(), ""))

# Add another block with multiple transactions
my_blockchain.add_block(Block(2, ["Transaction 2", "Transaction 3"], time(), ""))
