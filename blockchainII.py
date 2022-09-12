from block import Block, genesis, mine_block
class Blockchain:
    '''
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    '''
    
    def__init__(self):
        self.chain = [genesis()]
        
         def add_block(self, data):
            self.chain.append(mine_block(self.chain[-1], data))
             
         def __repr__(self):
             return f 'Blockchain: {self.chain}'
         
def main():             
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two') 
    
if __name__=='main':
    main()               