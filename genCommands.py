# Import modules
import algosdk.v2client as v2client

# Connect to an algod client
algod_address = "https://xna-mainnet-api.algonode.cloud "
indexer_address = "https://mainnet-idx.algonode.cloud"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = v2client.algod.AlgodClient(algod_token, algod_address)
indexer_client = v2client.indexer.IndexerClient(algod_token, indexer_address)


def get_goal_commands(txn_obj, isGroup=False):
    # Check if the transaction object is named (as sometimes in blocks it in not named)
    txn = txn_obj.get("transaction", txn_obj)
    # Get the type of the transaction from the object 
    txn_type = txn["tx-type"]

    # Check if it is a payment transaction 
    if txn_type == "pay":
        # Get the amount, sender, receiver and fee from the object 
        amount = txn["payment-transaction"]["amount"]
        sender = txn["sender"]
        receiver = txn["payment-transaction"]["receiver"]
        fee = txn["fee"]

        # Construct a goal command string using these values 
        goal_cmd = f"goal clerk send -a {amount} -f {sender} -t {receiver} --fee {fee}"

    # Check if it is an application call transaction 
    elif txn_type == "appl":
        # Get the application ID and sender from the object 
        app_id = txn["application-transaction"]["application-id"]
        sender = txn["sender"]

        on_complete = txn["application-transaction"]["on-completion"]

        if on_complete == "optin":
            goal_cmd = f"goal app optin --app-id {app_id} --from {sender}"
        else:
            # Construct a goal command string using these values and append "--app-arg" for each additional argument in application args  
            goal_cmd = f"goal app call --app-id {app_id} --from {sender}"
            
            for i in range(0,len(txn["application-transaction"]["application-args"])):
                arg_value =txn["application-transaction"]["application-args"][i]
                goal_cmd += f" --app-arg \"b64:{arg_value}\""

            #  Discover and append "--app-accounts" for each account in application accounts
            for account in txn["application-transaction"]["accounts"]:
                goal_cmd += f" --app-account {account}"
            
            # Discover and append "--foreign-app" for each app in application foreign apps
            for account in txn["application-transaction"]["foreign-apps"]:
                goal_cmd += f" --foreign-app {account}"
            
            # Dicover and append foreign assets for each asset in application foreign assets
            for account in txn["application-transaction"]["foreign-assets"]:
                goal_cmd += f" --foreign-asset {account}"
            
       # Discover if the account rekeys and append "--rekey-to" if it does
        if txn.get("rekey-to", None) is not None:
            goal_cmd += f" --rekey-to {txn['rekey-to']}"
        
        

    # Check if it is an asset configuration transaction 
    elif txn_type == "acfg":
         # Get the asset ID and sender from the object 
        asset_id = txn["asset-config-transaction"]["asset-id"]
        sender = txn["sender"]

        # Check if it is an asset creation transaction (asset ID is 0) 
        if asset_id == 0:
            # Get the asset name, unit name, total supply and decimals from the object 
            asset_name = txn["asset-config-transaction"]["params"]["name"]
            unit_name = txn["asset-config-transaction"]["params"]["unit-name"]
            total_supply = txn["asset-config-transaction"]["params"]["total"]
            decimals = txn["asset-config-transaction"]["params"]["decimals"]

            # Construct a goal command string using these values 
            goal_cmd = f"goal asset create --creator {sender} --name {asset_name} --unitname {unit_name} --total {total_supply} --decimals {decimals}"

        else:
            # It is an asset reconfiguration transaction (asset ID is not 0) 
            # Get the new manager address from the object (if any) 
            new_manager = txn["asset-config-transaction"]["params"].get("manager", "")

            # Construct a goal command string using these values and append "--new-manager" if new manager address is not empty  
            goal_cmd = f"goal asset config --assetid {asset_id} --manager {sender}"
            
            if new_manager != "":
                goal_cmd += f" --new-manager {new_manager}"

    # Check if it is an asset transfer transaction 
    elif txn_type == "axfer":
        # Get the amount, sender, receiver and fee from the object 
        amount = txn["asset-transfer-transaction"]["amount"]
        sender = txn["sender"]
        receiver = txn["asset-transfer-transaction"]["receiver"]
        fee = txn["fee"]

        # It is an asset transfer transaction (amount is not 0) 
        # Get the asset ID from the object
        asset_id = txn["asset-transfer-transaction"]["asset-id"]

            # Construct a goal command string using these values
        goal_cmd = f"goal asset transfer -a {amount} -f {sender} -t {receiver} --assetid {asset_id} --fee {fee}"

    else:
         # It is an unknown type of transaction
         raise ValueError(f"Unknown transaction type: {txn_type}")
    
    # Check if there is a note in the transaction and append "--note" if there is
    if txn.get("note", None) is not None:
        note = txn["note"]
        goal_cmd += f" --note {note}"

    return goal_cmd


# Ask for a user input for the transaction or group transaction ID
txid = input("Enter a transaction ID: ")

# Get the transaction object by its ID
txn_obj = indexer_client.transaction(txid)

hasGroup = txn_obj["transaction"].get("group", None)

# Check if the transaction is part of a group transaction
if hasGroup is not None:
    # Get the group transaction ID
    group_txid = txn_obj["transaction"]["group"]
    print(f"Transaction {txid} is part of a group transaction with ID {group_txid}")
    block = txn_obj["transaction"]["confirmed-round"]
    print(f"Transaction {txid} was confirmed in block {block}")
    
    # get the block information
    block_info = indexer_client.block_info(block)
    
    # find the transactions in the block that are in the group transaction
    group_txns = []
    for tx in block_info["transactions"]:
        isGroup = tx.get("group", None)
        if isGroup is not None and tx["group"] == group_txid:
            group_txns.append(tx)

    # print the goal commands for each transaction in the group transaction
    print(f"Group transaction {group_txid} contains the following commands:")
    filenames = []
    for i, tx in enumerate(group_txns):
        # Get the goal command string
        goal_cmd = get_goal_commands(tx, True)
        fname = f"unsignedTx{i}.txn"
        print(f"{goal_cmd} --out {fname}")
        filenames.append(fname)
    else:
        
        print(f"{ ' '.join(filenames) } > combinedTrans.tx")
        print(f"goal clerk group -i combinedTrans.tx -o groupedTrans.tx")
        print(f"goal clerk sign -i groupedTrans.tx -o signedGroupedTrans.tx")
        print(f"goal clerk rawsend -f signedGroupedTrans.tx")
else:
    if isinstance(txn_obj, dict) and hasGroup is None:  
        # Get the goal command string
        print(f"Transaction {txid} is not part of a group transaction")
        goal_cmd = get_goal_commands(txn_obj)
        
        # Print out the generated goal command
        print(goal_cmd)


