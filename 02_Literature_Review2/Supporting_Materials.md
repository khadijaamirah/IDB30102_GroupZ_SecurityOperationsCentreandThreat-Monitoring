# 02_Literature_Review: Supporting Materials

This directory contains supporting analysis files and documentation for Chapter 2, fulfilling the UniKL CDDH v4 Appendix O assessment requirements.

---

## 1. Literature Review Analysis Table

| No. | Author(s) & Year | ML Approach | Dataset/Data Source | SIEM Function/Environment | Key Findings & Evaluation | Limitation/Relevance |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | Kim and Kwon (2022) | CNN, LSTM, GRU with customized threat-event encoding | 2.6 million threat events from a security vendor's SOC | Threat event encoding, ML classification and efficiency comparison in a SOC environment | LSTM achieved the highest F1 score, recall ranged from 94.07% - 95.11%. CNN static (1D) was the most cost-effective model. | Data came from one security vendor SOC limiting generalization. Shows that ML can improve SIEM threat classification while efficiency remains important. |
| **2** | Muhammad et al. (2023) | SVM-based ML anomaly detection | Live network traffic during a DoS test | Zeek Slips ELK Stack for live SIEM/IDS analysis | Successfully detected DoS attacks. Elasticsearch used 785 CPU and 2300 MB RAM. | Tested in a local/virtualized environment with a limited DoS scenario. Useful for discussing practical SIEM integration and resource requirements. |
| **3** | Kayhan et al. (2023) | Autoencoder anomaly detection | 10,485 SIEM process audit events collected through EDR | Extract term and character level command features to detect anomalous commands | UHAC identified around 84% - 89% of anomalies when the top 10% of data was investigated. | Based on text-based commands from one organization. Demonstrates the value of unsupervised ML for anomalies or potentially unknown behavior. |
| **4** | Sebbar et al. (2023) | SVM, Random Forest, Decision Tree and AdaBoost | Real world network traffic and collected events logs | ML analyses traffic, detects threats and sends events to Elastic SIEM for real time monitoring. | RF achieved 0.98 accuracy, 0.97 precision and 0.96 F1 score, SVM achieved 0.97 accuracy. | Limited ML techniques and weak anomaly detection. Strong evidence for real time ML-SIEM integration. |
| **5** | Nurusheva et al. (2024) | SVM, RF, Decision Tree and AdaBoost | MITRE ATT&CK samples, security event logs, IRP data and CSV data | Collection, normalization, features extraction, ML detection, continuous monitoring and alert generation using ELK/Splunk. | Implemented an ML integrated SIEM using ELK and TheHive with DVWA testing and Telegram alerts to SOC Level 1. | Dataset details and comparative model results were not clearly reported, production SOC validation was unclear. |
| **6** | Ustz et al. (2024) | Supervised adaptive misuse detection/ SVM | Four weeks of SIEM process creation events from an enterprise with 50,000 users + 500 crafted evasions | Converts SIEM events into features and detects evasions of conventional SIEM rules. | 44% of the SIEM rules analyzed could be evaded. AMIDES detected most crafted evasions without false alerts. | Focused mainly on Windows process creation events and crafted evasions. Shows why conventional rule-based SIEM detection can have blind spots. |
| **7** | Najafi et al. (2024) | HEOD ensemble of context-aware outlier detection models | Public cybersecurity dataset 20 TB EDR logs from an enterprise with 100,000 assets | Generates contextual outlier scores and ranks suspicious activity for analysts deployed alongside enterprise SIEM. | Achieved strong outlier detection performance and was successfully deployed alongside an enterprise SIEM for LOLBins detection. | Mainly analyses features individually and may miss relationships across multiple features. Strong evidence for realistic enterprise scale detection. |
| **8** | Kapera and Niemiec (2025) | ML-based dynamic risk thresholds | Splunk Enterprise Security logs | Dynamically adjusts alert thresholds according to risk scores. | Reduce false positive alerts by 26% compared with static thresholds in a live Splunk SIEM environment. | Focuses on dynamic alert thresholds rather than general threat classification. Highly relevant to false positives and alert fatigue. |
| **9** | Hamza et al. (2025) | AdaBoost, CART, KNN, SVM, RF, LR, NB, LDA, MLP, DNN, CNN and LSTM | CIC-IDS2017 | Preprocessing, feature representation, model training and network intrusion detection. | RF achieved 99.85% accuracy, CNN+KNN achieved 99% accuracy, 93% precision and 89% F1 score. | Difficulty detecting infrequent attacks and class imbalance, live SIEM deployment has not been fully validated. Excellent evidence for comparing ML performance. |
| **10** | Ramavath et al. (2025) | VAE, GraphSAGE and LOF | CSE-CIC-DS2018, synthetic SIEM dataset, LANL and OpTC validation data | SIEM log parsing, security graph construction, embedding and real time anomaly alerts. | GraphSAGE + LOF achieved 0.93 AUC-ROC, 0.88 F1 score, 0.02 FPR and 87.2% detection rate, outperforming rule-based SIEM and Isolation Forest baselines. | Performance depends on embedding/hyperparameters, false positives still require expert review, and concept drift remains a concern. |
| **11** | Adiga et al. (2025) | SVM, BERT, LSTM and other classification models | SIEVE synthetic SIEM logs generated from public cybersecurity logs tested with real logs | Generates synthetic logs, trains classifiers and tests on synthetic and real SIEM logs. | SVM achieved 0.9323 – 0.9737 Macro F1 and remained robust on real logs, BERT performance degraded on real logs. | Synthetic logs may not fully represent real enterprise log complexity. Very important for explaining the dataset/generalization problem. |
| **12** | Khayat et al. (2025) | Ensembles LSTM, CNN and BRNN with attention and feature selection | Network/ security event data | Extracts textual, statics and temporal features, detects threats and priorities alerts. | Achieved 99.28% accuracy, 99.46% precision and 98.67% F-measure using an 80/20 split. | Performance depends on dataset and experimental configuration; broader real-world validation is needed. |
| **13** | Abd Bahrim et al. (2026) | RF, Extra Trees, KNN and Soft Voting Ensemble | BETH Cloud Traffic, Login Anomaly and TON-IoT datasets | ML anomaly classification, Elasticsearch storage, Kibana visualization and real time monitoring. | Soft voting achieved 78%, 80% and 75% accuracy across the three datasets. | Dataset imbalance and local simulated testing limit real-world validation. Strong evidence that performance differs across datasets. |
| **14** | Yauri et al. (2026) | Logistic Regression, RF, Gradient Boosting, SVM, DT, NB and Neural Networks | 98,321 SIEM records from a Palo Alto firewall | SIEM log collection, clustering, experts labelling and supervised ML classification. | Gradient Boosting achieved 97.97% accuracy, 0.9732 F1 score and 0.9964 RO-AUC. Hyperparameter tuning improved performance. | Data came from one Palo Alto firewall. Directly aligned with ML based classification of SIEM security events. |
| **15** | Khalfi et al. (2026) | Distributed RF | 1,000,107 network flows covering eight attack types | Real time flow processing integrated with Wazuh, Kibana and Elasticsearch. | Achieved 92.34% accuracy and >92% precision with processing of 1,000+ flows and low resource usage. | Lower precision for infiltration attacks and limited visibility of encrypted data exfiltration. Useful for realistic, production oriented SIEM deployment. |

---

## 2. Comparison of Existing Techniques

| Technique Family | Representative Algorithms | Key Strengths | Major Weaknesses | SIEM Operational Suitability |
| :--- | :--- | :--- | :--- | :--- |
| **Supervised Learning** | Random Forest, XGBoost, LightGBM | High accuracy, fast inference, low compute costs. | Cannot detect novel (zero-day) attacks. | **High** (ideal for high-throughput rule enhancement). |
| **Deep Learning** | CNN, LSTM, BiLSTM | Captures complex spatio-temporal patterns. | High memory footprint, latency bottlenecks. | **Medium** (best suited for offline or batch analysis). |
| **Unsupervised Anomaly** | Autoencoders, Isolation Forest | Detects unknown anomalies without labels. | High false positive rate on normal traffic spikes. | **Medium** (requires secondary risk validation). |
| **Graph Neural Networks** | GraphSAGE, GCN | Models relationships and lateral movement paths. | Computationally intensive graph construction. | **Low-Medium** (requires enterprise graph data pipelines). |
| **Explainable AI (XAI)** | SHAP, LIME | Provides interpretable risk scores for analyst triage. | Adds processing latency to real-time pipelines. | **High** (critical for alert fatigue reduction). |

---

## 3. Research Gap Analysis

* **Validation Gap:** Excessive reliance on static benchmark datasets (CIC-IDS2017, NSL-KDD) that do not reflect live enterprise log velocity and noise.
* **Adaptability Gap:** Supervised classifiers experience severe performance degradation when encountering zero-day attacks or concept drift without dynamic retraining.
* **Usability Gap:** Deep learning architectures operate as black boxes, lacking integrated real-time explainability (XAI) to assist SOC analyst triage.
* **Deployment Gap:** Machine learning models are primarily tested in isolated lab environments rather than deployed on production-scale SIEM streaming pipelines (e.g., Wazuh/ELK).

---

## 4. Summary of Methods and Algorithms Identified

* **Tree-Based Gradient Boosting (XGBoost, LightGBM, CatBoost):** Used for fast, structured feature classification with low prediction latency.
* **Deep Neural Networks (CNN, LSTM, BiLSTM):** Employed for sequence classification across time-series log events.
* **Unsupervised Reconstruction Models (Autoencoders, VAE, Isolation Forest):** Leveraged for baseline reconstruction and zero-day anomaly detection.
* **Explainable AI Frameworks (SHAP, Soft-Voting Ensembles):** Applied to compute feature importance scores and reduce analyst alert fatigue.

---

## 5. Relevant Datasets

* **Benchmark Datasets:** CIC-IDS2017, CSE-CIC-IDS2018, NSL-KDD, UNSW-NB15.
* **Enterprise Log Datasets:** BETH Dataset, LANL / OpTC graph telemetry, Sysmon host event logs.
* **SIEM Telemetry Streams:** Live Splunk ES, Wazuh Sysmon, and ELK Stack event pipelines.

---

## 6. Evaluation Metrics Identified

* **Detection Accuracy ($Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$):** Standard overall model performance metric.
* **Precision ($Precision = \frac{TP}{TP + FP}$):** Critical for measuring false alarm rates.
* **Recall / Sensitivity ($Recall = \frac{TP}{TP + FN}$):** Measures the ability to catch all actual attacks.
* **F1-Score ($F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$):** Harmonic mean balancing false positives and false negatives.
* **False Positive Rate ($FPR = \frac{FP}{FP + TN}$):** Key metric for assessing alert fatigue reduction.
* **Inference Latency (ms):** Measures operational suitability for real-time streaming log ingestion.
