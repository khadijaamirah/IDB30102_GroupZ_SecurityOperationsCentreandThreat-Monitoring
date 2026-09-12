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

The proposed machine learning approach will be evaluated using the CIC-IDS2017 dataset for binary classification of network traffic as benign or malicious.

The Random Forest model will be compared with a Decision Tree baseline using the same dataset, preprocessing procedures and testing conditions.

| Evaluation Component | Planned Setting |
|---|---|
| Dataset | CIC-IDS2017 |
| Classification | Benign vs. Malicious |
| Proposed Model | Random Forest |
| Baseline Model | Decision Tree |
| Training/Test Split | 80% / 20% |
| Sampling | Stratified |
| Evaluation Metrics | Accuracy, Precision, Recall, F1-score |
| Comparison Condition | Same dataset and testing conditions |
| SIEM Environment | Wazuh (proposed integration) |

The main comparison will determine whether the Random Forest model provides better overall detection performance than the Decision Tree baseline, with particular attention to F1-score, precision and recall.

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

The repository contains preliminary technical components for the proposed machine learning-based cyber threat detection prototype.

The current preliminary implementation includes:

- **Dataset Loading:** Loads the CIC-IDS2017 dataset from a CSV file.
- **Data Preprocessing:** Cleans column names, removes invalid and missing values, and prepares the dataset for model training.
- **Binary Label Preparation:** Converts the traffic labels into two classes: benign and malicious.
- **Feature Preparation:** Selects numerical features from the prepared dataset for machine learning.
- **Data Splitting:** Splits the dataset into 80% training data and 20% testing data using stratified sampling.
- **Random Forest Model:** Implements Random Forest as the proposed machine learning model.
- **Decision Tree Model:** Implements Decision Tree as the baseline model.
- **Performance Evaluation:** Evaluates both models using accuracy, precision, recall and F1-score.
- **Expected Output:** Provides the expected format for comparing the performance of the Random Forest and Decision Tree models.

The current source code represents preliminary machine learning development and does not yet constitute a complete production SIEM system.
  
## Technologies and Tools

### Programming Language
- Python

### Machine Learning Library
- Scikit-learn

### Data Processing Libraries
- Pandas
- NumPy

### Machine Learning Models
- Random Forest Classifier
- Decision Tree Classifier (baseline)

### SIEM Environment
- Wazuh (proposed integration environment)

### Dataset
- CIC-IDS2017

### Development Tools
- GitHub
- Python development environment
  
## How to Run Preliminary Code

### 1. Clone the repository

git clone https://github.com/khadijaamirah/IDB30102_GroupZ_SecurityOperationsCentreandThreat-Monitoring-.git

### 2. Navigate to the source code folder

cd 04_Source_Code

### 3. Install the required Python libraries

pip install -r requirements.txt

### 4. Place the CIC-IDS2017 dataset

Place the prepared dataset file in the location expected by the source code:

CIC-IDS2017.csv

### 5. Run the Python source code

python baseline_model.py

### 6. View the output

The program will display the Accuracy, Precision, Recall and F1-score for:

- Random Forest
- Decision Tree

## Expected Outcome

The preliminary prototype is expected to produce performance results for both the Random Forest and Decision Tree models using accuracy, precision, recall and F1-score.

The Random Forest model is expected to be compared with the Decision Tree baseline under the same testing conditions. The final evaluation will determine whether the proposed approach improves cyber threat detection performance.

Actual performance values will be reported after the models are trained and tested using the prepared CIC-IDS2017 dataset.
