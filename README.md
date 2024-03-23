# Repository for paper replication: Unlocking UTXO transactional patterns in blockchain and their impact on storage scalability.

## Introduction
Blockchain technology ensures record-keeping by redundantly storing and verifying transactions on a distributed network of nodes. Permissionless blockchains have pushed the advancement of decentralized applications, characterized by distributed business logic, resilience against centralized failure, and data immutability.  However, one of the remaining open challenges in permissionless blockchains is the scalability on storage, i.e. the database's ability to grow sub-linearly in relation to the number of nodes. Due to the intrinsic redundancy in design, enhancing transactional throughput often compromises storage, as seen in projects such as Elastico, OmniLedger, and Rapidchain. On the other hand, solutions seeking to minimize storage on nodes, such as CUB, Jidar, SASLedger, and SE-Chain, lack transactional throughput.

## Objective
The primary objective of this paper is to delve deep into the UTXO and Account Models, identifying their transactional patterns. By understanding these models thoroughly, we aim to pave the way for future research to enhance storage scalability in distributed environments. Our ultimate goal is to contribute to the advancement of blockchain technology by unlocking more efficient transactional patterns.

## Key Features
- **Granular Transactional Patterns**: We introduce finer transactional patterns compared to existing solutions, allowing for more flexibility and efficiency in transaction processing.

- **Scalability Focus**: By addressing the limitations of current transactional patterns, we aim to facilitate the scalability of storage in distributed environments, enabling blockchain technology to handle larger transaction volumes effectively.

- **Research Contribution**: This project serves as a foundational study for future research endeavors aimed at optimizing transactional models in blockchain technology.

## Getting Started
To get started with this project, follow these steps:

1. Download the Database: Download the database stored in Harvard Dataverse through the following link: https://doi.org/10.7910/DVN/6V8HRL

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
