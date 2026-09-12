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

---

## Research Problem

### Problem 1: Cyber Threat Detection Accuracy

SIEM systems process large volumes of security events to detect potential cyber threats. However, false positives, false negatives and class imbalance can reduce detection accuracy and increase the workload of SOC analysts. Although machine learning has been applied to improve SIEM-based detection, its performance varies across different datasets and experimental conditions.

### Problem 2: Limited and Inconsistent Evaluation

Many existing machine learning-based SIEM studies rely on benchmark, simulated or limited datasets. Differences in datasets, evaluation metrics and experimental settings also make it difficult to compare the performance of different approaches consistently. Therefore, further research is needed using clearly defined and reproducible evaluation conditions.

---

## Research Aim

To develop a machine learning approach to improve cyber threat detection accuracy in Security Information and Event Management (SIEM) environments.

---

## Research Objectives

1. To study existing machine learning approaches for cyber threat detection in SIEM environments.
2. To develop a machine learning approach for cyber threat detection in a SIEM environment.
3. To test the detection performance of the proposed machine learning approach using defined evaluation metrics and conditions.

---

## Brief Description of the Proposed Solution

The proposed solution is a machine learning-based cyber threat detection prototype for a SIEM environment.

The CIC-IDS2017 dataset will be used for developing and evaluating the proposed approach. The data will undergo preprocessing and feature preparation before being used for binary classification of network traffic as benign or malicious.

Random Forest is used as the proposed machine learning model, while Decision Tree is used as the baseline model for comparison. The proposed approach is intended to be demonstrated within a Wazuh SIEM environment for security monitoring and threat detection.

The current implementation in the repository represents preliminary machine learning development and is not a complete production SIEM system.

---

## Selected Research Methodology and Development Model

### Research Methodology: Design Science Research (DSR)

Design Science Research is selected to guide the development and evaluation of the proposed machine learning-based cyber threat detection solution.

The DSR process consists of:

1. Problem Identification
2. Define the Research Objectives
3. Design and Development
4. Demonstration
5. Evaluation
6. Communication

### Development Model: Prototyping Model

The Prototyping Model is selected because the project focuses on developing and evaluating a proof-of-concept prototype rather than a complete enterprise SIEM system.

The development process consists of:

1. Requirement Identification
2. Initial Design
3. Prototype Development
4. Prototype Testing
5. Refinement
6. Final Prototype

---

## Proposed Evaluation Plan

The proposed Random Forest model will be compared with a Decision Tree baseline using the same dataset, preprocessing procedures and testing conditions.

### Baseline

**Decision Tree Classifier**

The Decision Tree model will be used as the baseline for comparison with the proposed Random Forest model.

### Dataset

**CIC-IDS2017**

The dataset contains labelled normal and malicious network traffic and will be used for training and testing the machine learning models.

The preliminary implementation uses an **80% training and 20% testing split** with stratified sampling.

### Test Environment

The machine learning approach is intended to be demonstrated in a **Wazuh SIEM environment** for security monitoring and detection output.

### Evaluation Metrics

The proposed evaluation will use:

- **Accuracy** – Overall proportion of correctly classified traffic.
- **Precision** – Proportion of predicted malicious traffic that is correctly identified.
- **Recall** – Ability to identify actual malicious traffic.
- **F1-score** – Balance between precision and recall.
- **False Positive Rate (FPR)** – Proportion of benign traffic incorrectly identified as malicious.

The Random Forest model will be compared with the Decision Tree baseline under the same dataset, preprocessing and testing conditions. The proposed approach will be considered successful if it demonstrates improved detection performance, particularly through a higher F1-score while maintaining suitable precision and recall and reducing false positive detections.

---

## Proposed System Architecture

The proposed system processes the CIC-IDS2017 dataset through data preprocessing and feature selection before applying the machine learning model. The resulting traffic classification is intended to be sent to the Wazuh SIEM environment for security monitoring and alert generation.

### System Flow

```text
CIC-IDS2017 Dataset
        ↓
Data Preprocessing
        ↓
Feature Selection
        ↓
Machine Learning Model
        ↓
Threat Classification
(Benign / Malicious)
        ↓
Wazuh SIEM Environment
        ↓
Security Alert / Detection Output
```

The proposed architecture and flowchart are provided in the:

**`03_Architecture_and_Flowchart/`** folder.

---

## Description of Technical Components Included in the Repository

The repository contains preliminary technical components for the proposed machine learning-based cyber threat detection prototype.

### Data Loading

The preliminary Python implementation loads the CIC-IDS2017 dataset from a CSV file.

### Data Preprocessing

The implementation:

- Cleans column names.
- Replaces infinite values with missing values.
- Removes missing values.

### Binary Classification

The original traffic labels are converted into two classes:

- `BENIGN` = 0
- `Malicious` = 1

### Feature Preparation

The preliminary implementation selects numerical features from the prepared dataset for machine learning.

### Training and Testing

The dataset is divided into:

- 80% training data
- 20% testing data

Stratified sampling is used during the split.

### Machine Learning Models

The repository includes:

- **Random Forest Classifier** – proposed model
- **Decision Tree Classifier** – baseline model

### Model Evaluation

The preliminary implementation evaluates the models using:

- Accuracy
- Precision
- Recall
- F1-score

The repository also contains an expected evaluation output that includes False Positive Rate (FPR) as a planned metric.

### Expected Output

The repository contains an expected output format for comparing the Random Forest and Decision Tree models. Final numerical results will be added after model training and testing are completed.

---

## Programming Languages, Software, Frameworks, Libraries, Datasets and Tools Expected to Be Used

### Programming Language

- **Python**

### Libraries

- **Pandas**
- **NumPy**
- **Scikit-learn**

### Machine Learning Models

- **Random Forest Classifier**
- **Decision Tree Classifier**

### SIEM

- **Wazuh** – proposed SIEM environment for security monitoring and detection output

### Dataset

- **CIC-IDS2017**

### Repository Platform

- **GitHub**

---

## Instructions for Executing Preliminary Code

### 1. Clone the repository

```bash
git clone https://github.com/khadijaamirah/IDB30102_GroupZ_SecurityOperationsCentreandThreat-Monitoring-.git
```

### 2. Navigate to the source code folder

```bash
cd 04_Source_Code
```

### 3. Install the required Python libraries

```bash
pip install -r requirements.txt
```

The required libraries are:

```text
pandas
numpy
scikit-learn
```

### 4. Prepare the dataset

Obtain the CIC-IDS2017 dataset from its official source and place the prepared CSV file in the location expected by the source code:

```text
CIC-IDS2017.csv
```

The complete dataset is not included in the repository. A sample input file is provided in:

```text
05_Data_or_Sample_Input/sample_input.csv
```

### 5. Run the preliminary source code

```bash
python baseline_model.py
```

Replace `baseline_model.py` with the actual Python source file name in the `04_Source_Code` folder.

### 6. View the output

The preliminary program produces evaluation results for:

- Random Forest
- Decision Tree

using:

- Accuracy
- Precision
- Recall
- F1-score

Final experimental results will be added after the model development and evaluation stages are completed.
