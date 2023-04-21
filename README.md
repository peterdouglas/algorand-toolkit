# Algorand Toolkit
This repo has tools that to aid with the debugging and exploration of smart contracts on the Algorand network.

## Generate Commands
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

Currently, it does not handle application creation/deployment.