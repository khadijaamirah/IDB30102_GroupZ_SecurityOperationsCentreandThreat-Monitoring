## Dataset

### Dataset Used

**CIC-IDS2017**

CIC-IDS2017 is a publicly available cybersecurity dataset containing normal and malicious network traffic. It provides labelled network traffic data for machine learning-based cyber threat classification.

### Data Source

Canadian Institute for Cybersecurity (CIC), University of New Brunswick.

Official dataset page:  
https://www.unb.ca/cic/datasets/ids-2017.html

### Intended Use

The dataset will be used to train and test the proposed Random Forest machine learning model for binary classification of network traffic as benign or malicious.

### Data Preparation

The selected data will undergo preprocessing and feature preparation before being used for machine learning. The prepared data will then be divided into training and testing subsets.

### Sample Input

A sample input file is provided in this folder to demonstrate the structure of the network traffic data used by the proposed approach.

The sample contains network flow features including:

- Flow Duration
- Total Forward Packets
- Total Backward Packets
- Flow Bytes/s
- Flow Packets/s
- Label

### Data Flow

CIC-IDS2017 Dataset → Data Preprocessing → Feature Preparation / Selection → Training / Testing Data

### Data Availability

The complete CIC-IDS2017 dataset is not uploaded to this repository. Users should obtain the dataset from its official source. The dataset is intended for academic and research purposes.
