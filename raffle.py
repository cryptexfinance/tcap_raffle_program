import hashlib
import random
import os
from collections import namedtuple
from typing import List, Tuple

import click
import requests
from web3 import Web3, HTTPProvider

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class ConfigNotSet(Exception):
    def __init__(self, var_name):
        super().__init__(f"{var_name} is not set in .env")


Config = namedtuple(
    "Config",
    [
        "FUUL_API_KEY",
        "WEB3_HTTP_NODE_URL",
    ]
)


def get_env_var_or_raise(var_name: str) -> str:
    var = os.getenv(var_name)
    if not var:
        raise ConfigNotSet(var_name)
    return var


def get_config() -> Config:
    fuul_api_key = get_env_var_or_raise('FULL_API_KEY')
    wbe3_url = get_env_var_or_raise('WEB3_HTTP_NODE_URL')

    return Config(
        FUUL_API_KEY=fuul_api_key,
        WEB3_HTTP_NODE_URL=wbe3_url,
    )


def get_block_hash(config: Config, block_number: int) -> str:
    w3 = Web3(HTTPProvider(config.WEB3_HTTP_NODE_URL))
    return w3.eth.get_block(block_number).hash.to_0x_hex()


def get_participants(config: Config) -> List[Tuple[str, int]]:
    participants_data: List[Tuple[str, int]] = list()
    page = 1
    page_size = 25
    print('fetching participants and their points from leaderboard')
    while True:
        # TODO: add an end date to the program
        response = requests.get(
            f"https://api.fuul.xyz/api/v1/payouts/leaderboard/points/?page_size={page_size}&page={page}",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {config.FUUL_API_KEY}"
            }
        )
        response.raise_for_status()
        response_data = response.json()
        for _participant_data in response_data['results']:
            participants_data.append((_participant_data['address'], _participant_data['total_attributions']))
        total_results = response_data['total_results']
        if (page * page_size) >= total_results:
            break
        else:
            page += 1
    print('fetched participants and their points from leaderboard')
    return participants_data


def choose_weighted_winner(participants_data: List[Tuple[str, int]], block_hash: str) -> str:
    """
    Selects a winner using a weighted random selection based on points and a block hash.
    Args:
        participants_data (list): List of participant addresses and their points.
        block_hash (str): Ethereum block hash used as the random seed.
    Returns:
        str: The winner of the raffle.
    """
    if not participants_data:
        raise ValueError("Participants and points lists cannot be empty.")
    if not isinstance(block_hash, str) or len(block_hash) != 66 or not block_hash.startswith("0x"):
        raise ValueError("Invalid block hash format.")

    sorted_participants = sorted(participants_data, key=lambda x: x[0])

    # Create a weighted pool based on points
    weighted_pool = []
    for participant_data in sorted_participants:
        weighted_pool.extend([participant_data[0]] * participant_data[1])

    if not weighted_pool:
        raise ValueError("Weighted pool is empty. Ensure points are greater than zero.")

    # Convert the block hash to a random seed
    seed = int(hashlib.sha256(block_hash.encode()).hexdigest(), 16)

    # Use the seed to select a winner
    random.seed(seed)
    winner = random.choice(weighted_pool)
    return winner


@click.command()
@click.argument("block_number", type=int)
def main(block_number: int):
    config = get_config()
    block_hash = get_block_hash(config, block_number)
    participants_data = get_participants(config)
    winner = choose_weighted_winner(participants_data, block_hash)
    print(f'The winner is: {winner}')


if __name__ == "__main__":
    main()
