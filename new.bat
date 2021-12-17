geth --datadir .\ init genesis.json
geth --datadir .\ --networkid 1547 --http --http.corsdomain "*" --allow-insecure-unlock --http.api "net, web3 personal, eth"