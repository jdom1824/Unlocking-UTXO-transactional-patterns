# Repository for paper replication: Unlocking UTXO transactional patterns in blockchain and their impact on storage scalability.

## Contribution
In this paper, we present an analysis of the storage impact of transactional models in Bitcoin and Ethereum. Subsequently, we model the Unspent Transaction Output (UTXO) as a graph, offering granular insight into the status of each transaction. This abstraction allows us to identify transactional patterns for Bitcoin and Ethereum transactions. We provide formal evidence to show that the UTXO model is more storage-expensive than the Account model. Finally, we characterize the transactional models, and based on this characterization, we quantify the effect on storage growth for the transactional Account model and the UTXO model.

## Objective
This repository aims to provide resources related to the methods used in the experiments described in the article. In addition to algorithms, software, graphics, and databases, it also includes other relevant resources that may be useful for researchers and professionals interested in exploring and reproducing the study's results.

## Dataverse Collection
Considering that Bitcoin nodes manage a constantly growing database, the purpose of describing this methodology is to enable future work that uses this database to update the latest blocks without starting all the work from scratch.

- ***Experimental Setup***: the computer used in the experiments runs the Ubuntu 18.04 operating system and is equipped with an XEON processor with 92 virtual cores running at 2.4 GHz each. The computer has a total of 128 GB of dual-channel DDR4 RAM running at 3200 MHz. For data storage, a 2TB solid-state drive (SSD) was integrated to provide fast read/write speeds for easy access to the files and programs needed to run the experiments.

- ***Software***: we illustrate the methodology used to store the data in Figure 1, for which we used Bitcoin Core version 0.22 to synchronize a full Bitcoin node until July 4, 2023, and then extracted the data for further processing using BlockSci 0.7. 0. After obtaining the data, we filter it based on transaction patterns using Python3 and C++.
  
<p align="center">
  <img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Images/Framework.jpeg" alt="Benchmark" width="1000"/>
  <br>
  <em>Fig 1. Experimental framework for analyzing transactional patterns in the UTXO Model.
</p>

- ***Results***: the first dataverse that offers a detailed number of inputs and outputs generated in Bitcoin, from the genesis block to block 831,732. It includes various attributes such as TotalSize, Size, Inputs, Outputs, Block, and VinTxIds, providing comprehensive insights into the characteristics and components of individual transactions within the Bitcoin blockchain network.

--> Download the database stored in [Harvard Dataverse](url:https://dataverse.harvard.edu/) through the following doi: https://doi.org/10.7910/DVN/6V8HRL <--

**Attributes**:

1. Transaction: Identifier for the transaction. 
2. Total Size: Total size of the transaction, including SegWit.
3. Size: Size of the transaction.
4. Inputs: Number of inputs involved in the transaction.
5. Outputs: Number of outputs generated by the transaction.
6. Block:Identifier for the block containing the transaction.
7. VinTxIds: Array of previous transactions involved in the current transaction (Input Transaction IDs).

## Replicating Experiments

### 1. Transaction Sizes in Bitcoin and Ethereum

Our initial experiments provide preliminary evidence that our hypothesis regarding transaction storage efficiency in Ethereum compared to Bitcoin is true. To reach this conclusion, we conducted a comparative analysis of the bitcoin and Ethereum blockchains.

**Requirements and Setup**

Replicating these experiments requires Python 3 or higher, along with the specific requirements of each algorithm. For example, to run the transaction memory comparison algorithms in Bitcoin, you need to download the database and load each of its parts using the Pandas and Matplotlib libraries. For Ethereum, the necessary data can be obtained from Etherscan.io.

**Source code**

The original source code for the algorithms can be found [here](https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/tree/main/Examples/Histograms).

**Results**

<p align="center">
  <img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Histograms/Histograma_full_2.png" alt="Histogram Bitcoin" width="400"/>
  <br>
  <em>Fig 2. Visual representation of the distribution of Bitcoin transaction sizes, using data from 84,474,947 transactions.</em>
</p>

<p align="center">
  <img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Histograms/transaction_histogram_E.png" alt="Histogram Ethereum" width="400"/>
  <br>
  <em>Fig 3. Visual representation of the distribution of Ethereum transaction sizes, using data from 348,506,740 transactions.</em>
</p>

### 2. Analysis on the Storage Cost in Transactional Patterns of the UTXO Model

After defining the 'spent by' relation and the transactional patterns along with their metrics, we analyzed the storage requirements for each of the transferring, merging, and splitting patterns.

**Requirements and Setup**

To replicate these experiments, Python 3 or higher is required, along with the Pandas, Numpy, Collections, and Matplotlib libraries. Additionally, access to the Harvard dataverse parts is necessary.

**Source code**

The original source code for the algorithms can be found [here](https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Points/points.py) and [here](https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Torta/Torta_G.py).

**Results**

<p align="center">
  <img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Torta/pattern_distribution_pie.png" alt="Histogram Bitcoin" width="400"/>
  <br>
  <em>Fig 4. Proportional distribution of Splitting, Merging, and Transferring Patterns in the Dataset.</em>
</p>

<p align="center">
  <img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Points/Splitting_points.png" alt="Histogram Bitcoin" width="400"/>
  <br>
  <em>Fig 5. Transaction Size vs. Number of Outputs for the Splitting pattern. Each point represents an individual transaction.</em>
</p>

<p align="center">
  <img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Points/Transferring_points.png" alt="Histogram Bitcoin" width="400"/>
  <br>
  <em>Fig 6. Transaction Size vs. Number of Outputs for the Transferring Pattern. Each point represents an individual transaction.</em>
</p>

<p align="center">
  <img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Points/Merging_points.png" alt="Histogram Bitcoin" width="400"/>
  <br>
  <em>Fig 7. Transaction Size vs. Number of Outputs for the Merging Pattern. Each point represents an individual transaction.</em>
</p>

## Contributing
We welcome contributions from the community! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request. Your contributions will help advance the research in transactional patterns for blockchain technology.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any inquiries or discussions related to this project, feel free to contact us at jdom1824@gmail.com jdom1824@inaoe.com jdom1824@inaoep.com

