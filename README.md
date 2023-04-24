# Algorand Toolkit
This repo has tools that to aid with the debugging and exploration of smart contracts on the Algorand network.

## Generate Commands

![Generate commands demo](./images/genDemo.gif)]

One of the challenges to debugging and testing complex contracts on Algorand is reproducing the transactions, especially group transactions.

To run:
```bash
python ./genCommands.py
```

You will then see the following prompt:
```
Enter a transaction ID: 
```

Enter any transaction ID, and it will check if the transaction is part of a group and either return the goal command line to generate that transcation or transaction group.

The example shown in the gif uses a complex defi transaction is transaction id `7RA2CNQGRNFX4CSVGWARHUNCR22QOXT7N74JZ3ZAH6ZC27GJZ6TQ`.

It has 14 or so transactions in the group transaction. The response from the tool (including the results) is -
```bash
Transaction 7RA2CNQGRNFX4CSVGWARHUNCR22QOXT7N74JZ3ZAH6ZC27GJZ6TQ is part of a group transaction with ID UcqEEr5jZmsu6Gid5emOmz4HczhVaPLFV1PnWtM2pMs=
Transaction 7RA2CNQGRNFX4CSVGWARHUNCR22QOXT7N74JZ3ZAH6ZC27GJZ6TQ was confirmed in block 28492883
Group transaction UcqEEr5jZmsu6Gid5emOmz4HczhVaPLFV1PnWtM2pMs= contains the following commands:
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:Zm12" --foreign-app 465814065 --foreign-app 465814103 --foreign-app 465814149 --foreign-app 465814222 --foreign-app 465814278 --foreign-app 465814318 --note RmV0Y2ggVmFyaWFibGVz --out unsignedTx0.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:dXA=" --foreign-app 531724540 --foreign-app 451327550 --foreign-app 531725044 --foreign-app 531725449 --foreign-app 451327550 --foreign-app 531724540 --note VXBkYXRlIFByaWNlcw== --out unsignedTx1.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:dXBk" --app-account DWORILJUR57OBB36IRKTI36MASHIFBRYFS4PSLLUG6LEWCIAYNWOU4O3DY --foreign-app 465814065 --foreign-app 465814103 --foreign-app 465814149 --foreign-app 465814222 --foreign-app 465814278 --foreign-app 465814318 --note VXBkYXRlIFByb3RvY29s --out unsignedTx2.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfb25l" --note Rmlyc3QgRHVtbXkgVHhu --out unsignedTx3.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfdHdv" --note U2Vjb25kIER1bW15IFR4bg== --out unsignedTx4.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfdGhyZWU=" --note VGhpcmQgRHVtbXkgVHhu --out unsignedTx5.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfZm91cg==" --note Rm91cnRoIER1bW15IFR4bg== --out unsignedTx6.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfZml2ZQ==" --note RmlmdGggRHVtbXkgVHhu --out unsignedTx7.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfc2l4" --note U2l4dGggRHVtbXkgVHhu --out unsignedTx8.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfc2V2ZW4=" --note U2V2ZW50aCBEdW1teSBUeG4= --out unsignedTx9.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfZWlnaHQ=" --note RWlnaHRoIER1bW15IFR4bg== --out unsignedTx10.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:ZHVtbXlfbmluZQ==" --note TmluZXRoIER1bW15IFR4bg== --out unsignedTx11.txn
goal app call --app-id 465818260 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:cmN1" --app-arg "b64:AAAAAAAPMcE=" --note TWFuYWdlcjogcmN1 --out unsignedTx12.txn
goal app call --app-id 465814149 --from Q672EGGM3TEWUU2OQRVLE5A7QGQA34KY2ZNXCHWTIDKJSCT3VNGSGCG5MI --app-arg "b64:cmN1" --app-account DWORILJUR57OBB36IRKTI36MASHIFBRYFS4PSLLUG6LEWCIAYNWOU4O3DY --foreign-app 465818260 --foreign-asset 386192725 --note TWFya2V0OiByY3U= --out unsignedTx13.txn
unsignedTx0.txn unsignedTx1.txn unsignedTx2.txn unsignedTx3.txn unsignedTx4.txn unsignedTx5.txn unsignedTx6.txn unsignedTx7.txn unsignedTx8.txn unsignedTx9.txn unsignedTx10.txn unsignedTx11.txn unsignedTx12.txn unsignedTx13.txn > combinedTrans.tx
goal clerk group -i combinedTrans.tx -o groupedTrans.tx
goal clerk sign -i groupedTrans.tx -o signedGroupedTrans.tx
goal clerk rawsend -f signedGroupedTrans.tx
```

Note: This tool is still in alpha/active testing.

Currently, it does not handle application creation/deployment.