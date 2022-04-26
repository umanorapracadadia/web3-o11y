from web3 import Web3
import requests

# Infura credentials used to simulate accessing a node
infura_url = "https://mainnet.infura.io/v3/ba1169c3f1664f199460ec3f2a309e3c"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Confirm connection to web3
print(web3.isConnected())

# Get whale balances
snoop_balance = web3.eth.getBalance("0xCe90a7949bb78892F159F428D0dC23a8E3584d75")
paris_balance = web3.eth.getBalance("0xB6Aa5a1AA37a4195725cDF1576dc741d359b56bd")
serena_balance = web3.eth.getBalance("0x0864224F3cC570AB909EBF619f7583EF4a50b826")
lohan_balance = web3.eth.getBalance("0x3781d92e5449b5b689fEe308ded44882085b6312")
cuban_balance = web3.eth.getBalance("0xa679c6154b8d4619Af9F83f0bF9a13A680e01eCf")

# POST request to Events API for whale balances
headers = {'X-Insert-Key': '0c68ed1c1990c38fd55ede5fe96da0fc83bad06f', 'Content-Type': 'application/json'}
payload = {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'ParisHilton','balance':paris_balance/1000000000000000000}, {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'SnoopDogg', 'balance':snoop_balance}, {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'SerenaWilliams', 'balance':serena_balance/1000000000000000000}, {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'LindsayLohan', 'balance':lohan_balance/1000000000000000000}, {'eventType':'walletBalance', 'currency':'Ethereum', 'whale':'MarkCuban', 'balance':cuban_balance/1000000000000000000},

r = requests.post("https://insights-collector.newrelic.com/v1/accounts/1336182/events", json=payload, headers=headers)

# Get latest block stats
# blockNumber = web3.eth.blockNumber
block = web3.eth.get_block('latest')

# POST request to Events API for whale balances
headers = {'X-Insert-Key': '0c68ed1c1990c38fd55ede5fe96da0fc83bad06f', 'Content-Type': 'application/json'}

payload = {
    "eventType": "blockStatz",
    'difficulty': block.difficulty,
    #err 'extraData': block.extraData,
    'gasLimit': block.gasLimit,
    'gasUsed': block.gasUsed,
    #err 'hash': block.hash,
    #err 'logsBloom': block.logsBloom,
    'miner': block.miner,
    # 'nonce': block.nonce,
    'number': block.number,
    #err 'parentHash': block.parentHash,
    #err 'sha3Uncles': block.sha3Uncles,
    'size': block.size,
    #err 'stateRoot': block.stateRoot,
    #err 'totalDifficulty': block.totalDifficulty,
    #err 'transactionsRoot': block.transactionsRoot,
    'uncles': block.uncles,
}

r = requests.post("https://insights-collector.newrelic.com/v1/accounts/1336182/events", json=payload, headers=headers)

print('success')