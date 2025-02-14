## TCAP RAFFLE PROGRAM

This repo contains the code for selecting a winner for the TCAP raffle program.

### Process for selecting the winner:
- An end block will be announced well in advance to mark the conclusion of a specific program.
- The block hash of this end block will serve as the seed value for random function used in the script.
Since the end block is predetermined and each block includes a randao component, it provides a source of randomness that participants cannot manipulate.
- To enhance randomness further, the script applies a hashing function to the block hash.
- Participants are retrieved from the FUUL API and sorted by their addresses.
- Finally, Python's `random.choice` is used to select a winner.

### setup
1. clone the repository.

   `git clone https://github.com/cryptexfinance/tcap_raffle_program.git`
2. change directory

   `cd tcap_raffle_program`
3. create a `.env` file using the `.env.sample` file. Run the following command

   `cp .env.sample .env` 
4. set `WEB3_HTTP_NODE_URL` with the https url of the ethereum mainnet node.
5. set `FUUL_API_KEY` with the Fuul Api key for this project.
6. Create a python virtualenv. If you don't have pyenv installed then [read](https://github.com/pyenv/pyenv?tab=readme-ov-file#a-getting-pyenv).

   `pyenv virtualenv 3.11.3 tcap_raffle`
7. Activate virtualenv

   `pyenv activate tcap_raffle`
8. install requirements

   `pip install setup.py`

### run
To pick a winner at a particular block, run
```
    python raffle.py <BLOCK_NUMBER>
```
replace the <BLOCK_NUMBER> with the pre-announced block number for the program.
