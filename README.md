# Development of a Machine Learning Approach to Improve Cyber Threat Detection Accuracy in Security Information and Event Management

## Group Members and Student IDs
### Group Z
1) Siti Khadijah Amirah Binti Mohd Zaidi (52215124487)
2) Nurul Humaira Aqilah Binti Abdul Rahim (52215124553)
3) Nurin Binti Hasan (52215124134)
4) Nurul Najwa Binti Idrus (52215124883)

## Assigned Research Area

**Security Operations Centre (SOC) and Threat Monitoring**

The research focuses on Security Information and Event Management (SIEM) and the application of machine learning for cyber threat detection.

## Research Problem

### Problem 1: Cyber Threat Detection Accuracy

SIEM systems process large volumes of security events to detect potential cyber threats. However, false positives, false negatives and class imbalance can reduce detection accuracy and increase the workload of SOC analysts. Although machine learning has been applied to improve SIEM-based detection, its performance varies across different datasets and experimental conditions.

### Problem 2: Limited and Inconsistent Evaluation

Many existing machine learning-based SIEM studies rely on benchmark, simulated or limited datasets. Differences in datasets, evaluation metrics and experimental settings also make it difficult to compare the performance of different approaches consistently. Therefore, further research is needed using clearly defined and reproducible evaluation conditions.

## Research Aim

To develop a machine learning approach to improve cyber threat detection accuracy in Security Information and Event Management (SIEM) environments.

## Research Objectives

1. To study existing machine learning approaches for cyber threat detection in SIEM environments.
2. To develop a machine learning approach for cyber threat detection in a SIEM environment.
3. To test the detection performance of the proposed machine learning approach using defined evaluation metrics and conditions.

## Proposed Solution

The proposed solution is a machine learning-based cyber threat detection prototype integrated with a Wazuh SIEM environment.

The CIC-IDS2017 dataset will be used as the main dataset for model development and evaluation. The data will undergo preprocessing and feature selection before being used to train a Random Forest model for binary classification of network traffic as benign or malicious.

A Decision Tree model will be used as the baseline for comparison. The classification results will be demonstrated within the Wazuh SIEM environment to support security event monitoring and threat detection output.

The proposed approach will be evaluated under the same testing conditions as the baseline to determine whether it can improve cyber threat detection performance.

## Research Methodology

### Research Methodology: Design Science Research (DSR)

The study uses Design Science Research (DSR) to guide the development and evaluation of the proposed machine learning-based threat detection solution.

The DSR phases are:

1. Problem Identification
2. Define the Research Objectives
3. Design and Development
4. Demonstration
5. Evaluation
6. Communication

### Development Model: Prototyping Model

The Prototyping Model is used to develop the proposed proof-of-concept prototype. The development process consists of:

1. Requirement Identification
2. Initial Design
3. Prototype Development
4. Prototype Testing
5. Refinement
6. Final Prototype

## Proposed Evaluation Plan

The proposed approach will be evaluated using the CIC-IDS2017 dataset.

| Evaluation Component | Planned Setting |
|---|---|
| Dataset | CIC-IDS2017 |
| Classification | Benign and malicious traffic |
| Proposed ML Approach | Random Forest |
| Baseline | Decision Tree |
| SIEM Environment | Wazuh |
| Evaluation Metrics | Accuracy, Precision, Recall, F1-score |
| Comparison Conditions | Same dataset, preprocessing and testing conditions |

The Random Forest model and Decision Tree baseline will use the same dataset, preprocessing procedures and testing conditions to ensure a fair comparison.

The proposed approach will be considered successful if the Random Forest model demonstrates improved detection performance, particularly through a higher F1-score while maintaining suitable precision and recall.

## Proposed System Architecture

The proposed system consists of the following main stages:

1. **CIC-IDS2017 Dataset** – Provides normal and malicious network traffic.
2. **Data Preprocessing** – Cleans and prepares the dataset for machine learning.
3. **Feature Selection** – Selects relevant network traffic features.
4. **Machine Learning Model** – Uses Random Forest for threat detection.
5. **Threat Classification** – Classifies network traffic as benign or malicious.
6. **SIEM Environment** – Uses Wazuh to demonstrate security event monitoring.
7. **Security Alert / Detection Output** – Provides threat detection results for SOC analysts.

## Technical Components

The repository contains preliminary technical components supporting the proposed machine learning-based SIEM threat detection approach. These components are intended to demonstrate the technical direction and feasibility of the proposed research.

The planned technical components include:

- Dataset preparation and loading
- Data preprocessing
- Feature selection
- Random Forest model implementation
- Decision Tree baseline implementation
- Binary threat classification
- Wazuh SIEM integration
- Detection output
- Model evaluation and performance measurement
  
## Technologies and Tools

### Programming Language
- [To be confirmed from repository]

### Machine Learning
- Random Forest
- Decision Tree (baseline)

### SIEM
- Wazuh

### Dataset
- CIC-IDS2017

### Libraries / Frameworks
- [To be confirmed from repository]

### Development / Analysis Tools
- [To be confirmed from repository]
  
## How to Run Preliminary Code
