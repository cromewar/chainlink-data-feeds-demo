from posixpath import split
from brownie import GetPriceFeed, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_DEVELOPMENT_ENVIRONMENTS,
)


def deploy_price_feed():
    account = get_account()
    if network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print("Deploying Mocks...")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks Deployed!")

    price_feed = GetPriceFeed.deploy(price_feed_address, {"from": account})
    current_price = price_feed.getLatestPrice()
    print(f"The current price is {current_price}")


def main():
    deploy_price_feed()
