# Architecture and Flowchart

This folder contains the proposed system architecture and flowchart for the machine learning-based SIEM cyber threat detection prototype.

## Proposed Architecture

The proposed architecture shows how the CIC-IDS2017 dataset is processed before being used by the machine learning model. The model classifies network traffic as benign or malicious, and the detection result is intended to be sent to the Wazuh SIEM environment for security monitoring and alert generation.

## Proposed Flowchart

The flowchart shows the overall process from dataset loading, data preprocessing, feature preparation and model training to threat classification and performance evaluation. The proposed workflow also includes sending the detection result to the SIEM environment for security monitoring.

## Architecture Components

1. **CIC-IDS2017 Dataset** – Provides normal and malicious network traffic.
2. **Data Preprocessing** – Cleans and prepares the dataset for model development.
3. **Feature Selection** – Identifies relevant network features for threat detection.
4. **Machine Learning Model** – Applies the proposed machine learning approach for threat detection.
5. **Threat Classification** – Classifies traffic as benign or malicious.
6. **Wazuh SIEM Environment** – Provides the proposed environment for security event monitoring and alert generation.
7. **Security Alert / Detection Output** – Presents the detected threat information for SOC analysts.
