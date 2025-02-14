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
1. create a `.env` file using the `.env.sample` file. Run the following command
 `cp .env.sample .env` 
2. set WEB3_HTTP_NODE_URL with the https url of the ethereum mainnet node.
3. set FUUL_API_KEY with the Fuul Api key for this proect.

### run
To pick a winner at a particular block, run
```
    python raffle.py <BLOCK_NUMBER>
```
replace the <BLOCK_NUMBER> where the program ends.
