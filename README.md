# Repository for paper replication: Unlocking UTXO transactional patterns in blockchain and their impact on storage scalability.

## Contribution
In this paper, we present an analysis of the storage impact of transactional models in Bitcoin and Ethereum. Subsequently, we model the Unspent Transaction Output (UTXO) as a graph, offering granular insight into the status of each transaction. This abstraction allows us to identify transactional patterns for Bitcoin and Ethereum transactions. We provide formal evidence to show that the UTXO model is more storage-expensive than the Account model. Finally, we characterize the transactional models, and based on this characterization, we quantify the effect on storage growth for the transactional Account model and the UTXO model.

## Objective
This repository aims to provide resources related to the methods used in the experiments described in the article. In addition to algorithms, software, graphics, and databases, it also includes other relevant resources that may be useful for researchers and professionals interested in exploring and reproducing the study's results.

## Dataverse Methodology
Considering that Bitcoin nodes manage a constantly growing database, the purpose of describing this methodology is to enable future work that uses this database to update the latest blocks without starting all the work from scratch.

- ***Computer Description***: The computer used in the experiments runs the Ubuntu 18.04 operating system and is equipped with an XEON processor with 92 virtual cores running at 2.4 GHz each. The computer has a total of 128 GB of dual-channel DDR4 RAM running at 3200 MHz. For data storage, a 2TB solid-state drive (SSD) was integrated to provide fast read/write speeds for easy access to the files and programs needed to run the experiments.

- ***Software***: we illustrate the methodology used to store the data in Figure 1, for which we used Bitcoin Core version 0.22 to synchronize a full Bitcoin node until July 4, 2023, and then extracted the data for further processing using BlockSci 0.7. 0. After obtaining the data, we filter it based on transaction patterns using Python3 and C++.

<p align="center">
  <img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Images/Framework.jpeg" alt="Benchmark" width="1000"">
</p>

Fig 1. Experimental framework for analyzing transactional patterns in the UTXO Model.

## Getting Started Replicating Experiments
To get started with this project, follow these steps:

1. Download the database stored in [Harvard Dataverse](url:https://dataverse.harvard.edu/) through the following doi: https://doi.org/10.7910/DVN/6V8HRL

2. Explore the Code: Take a look at the proposed transactional patterns and their implementations. In the "Examples" folder, algorithms necessary to run the experiments described in the article are provided.

3. Contribute: Feel free to contribute to the project by suggesting improvements, reporting issues, or implementing new transactional patterns.

## Contributing
We welcome contributions from the community! If you have any ideas, suggestions, or improvements, please open an issue or submit a pull request. Your contributions will help advance the research in transactional patterns for blockchain technology.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any inquiries or discussions related to this project, feel free to contact us at jdom1824@gmail.com jdom1824@inaoe.com jdom1824@inaoep.com


## Figures generated with this repository

<img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/raw/main/Examples/Points/Merging_points.png" alt="Merging Points" width="400"/>

Transaction Size vs. Number of Outputs for the Merging Pattern. Each point represents an individual transaction.


<img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/raw/main/Examples/Points/Splitting_points.png" alt="Splitting Points" width="400"/>

Transaction Size vs. Number of Outputs for the Splitting pattern. Each point represents an individual transaction.

<img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/raw/main/Examples/Points/Transferring_points.png" alt="Transfering Points" width="400"/>

Transaction Size vs. Number of Outputs for the Transferring Pattern. Each point represents an individual transaction.

<img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Histograms/Histograma_full_2.png" alt="Histogram Bitcoin" width="400"/>

Visual representation of the distribution of Bitcoin transaction sizes, using data from 84,474,947 transactions.

<img src="https://github.com/jdom1824/Unlocking-UTXO-transactional-patterns/blob/main/Examples/Histograms/transaction_histogram_E.png" alt="Histogram Bitcoin" width="400"/>

Visual representation of the distribution of Ethereum transaction sizes, using data from 348,506,740 transactions.
