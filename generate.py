import pandas as pd
from web3 import Web3
from mnemonic import Mnemonic
from eth_keys import keys
from eth_utils import to_checksum_address
from typing import List, Dict

def generate_ethereum_wallets(count: int) -> List[Dict[str, str]]:
    wallets = []
    mnemo = Mnemonic("english")

    for _ in range(count):
        mnemonic_phrase = mnemo.generate(strength=128)
        seed = mnemo.to_seed(mnemonic_phrase)
        private_key = keys.PrivateKey(seed[:32])
        address = to_checksum_address(private_key.public_key.to_checksum_address())

        wallets.append({
            "address": address,
            "private_key": private_key.to_hex(),
            "mnemonic_phrase": mnemonic_phrase
        })

    return wallets

wallets = generate_ethereum_wallets(10)

# Print wallet information to the console
for i, wallet in enumerate(wallets):
    print(f"Wallet #{i + 1}")
    print(f"Address: {wallet['address']}")
    print(f"Private Key: {wallet['private_key']}")
    print(f"Mnemonic Phrase: {wallet['mnemonic_phrase']}")
    print("-------------------------------")

# Save wallet information to a text file
with open("wallets.txt", "w") as file:
    for wallet in wallets:
        file.write(f"{wallet['address']},{wallet['private_key']}\n")


# Save wallet information to an Excel file
df = pd.DataFrame(wallets)
df.index.name = "Wallet #"
df.index += 1
df.to_excel("wallets.xlsx", engine="openpyxl")
