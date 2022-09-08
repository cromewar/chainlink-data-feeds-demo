# Chainlink Data Feeds Implementation for Brownie

This is a simple demo using Chainlink Data Feeds, deployed with brownie.

## Requirements

* Python3.x +
* eth-brownie
* ganache

> Deployed using Goerli Network

## Steps to reproduce

1. Clone the repo with `git clone`.
2. Rename the `.env.example` for `.env` and replace using your Wallet Key and Infura project id.
   > Note: Do not use a wallet with real assets, use a wallet with tokens for the testnets.
3. Run de code using brownie
   
   ```shell
    brownie run scripts/deploy.py --network goerli.
   ```
## For Local Testing

Chainlink Data Feeds are live contracts you must interact with, and they don't exists on a local development environment.

So we use Mocks (Fake Contracts to get them), which return a fake price, this is helpful for local testing only.

Just run the code without the network flag.

```shell
brownie run scripts/deploy.py
```

> Remember to have ganache installed for this.

## Real life Deployment.

If you want to see this same concept applied to a real life application, check out this links.

- (Spanish) Check out the Spanish course "Solidity de Cero a Experto" 100% free on [youtube](https://youtu.be/yN3zpI3sNAE), lesson 3 and 6.

- (English) Check out the English version of the course on [youtube](https://youtu.be/M576WGiDBdQ), same lessons.