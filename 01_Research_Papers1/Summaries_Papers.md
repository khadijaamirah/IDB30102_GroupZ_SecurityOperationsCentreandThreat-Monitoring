# 01_Research_Papers: Focused Literature Summaries

This document presents detailed summary tables for 5 key primary research papers reviewed in Chapter 2, following the standardized review format.

---

### Paper 1: Nurusheva et al. (2024)

| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Alert fatigue reduction in SOCs using soft-voting ensembles and SHAP feature importance |
| **Author(s)** | A. Nurusheva, N. Smailov, & B. Omarov |
| **Year** | 2024 |
| **Research Problem** | High false-positive alert rates in SOC environments causing severe security analyst fatigue and delayed threat response. |
| **Method / Technique** | Soft-voting ensemble models integrated with SHAP (SHapley Additive exPlanations) for explainable risk scoring. |
| **Dataset / Tools** | Kaggle SOC event logs, Python, SHAP framework |
| **Main Findings** | Significantly reduced false-positive rates while providing clear feature attribution scores for analyst triage. |
| **Limitation** | Tested on static dataset samples rather than high-throughput real-time streaming SIEM logs. |
| **Relevance to Proposed Research** | Demonstrates how XAI techniques reduce alert fatigue, directly supporting the proposed explainable SIEM framework. |

---

### Paper 2: Sebbar et al. (2023)

| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Real-time log parsing and threat classification in open-source ELK Stack architectures |
| **Author(s)** | A. Sebbar, S. Hajji, & M. D. El Kettani |
| **Year** | 2023 |
| **Research Problem** | Difficulty of parsing high-velocity raw security logs in real time for machine learning classifier inference. |
| **Method / Technique** | Supervised tree-based models (XGBoost, Random Forest) paired with Logstash pipeline extraction. |
| **Dataset / Tools** | Enterprise ELK Stack logs, Logstash, Elasticsearch, Kibana |
| **Main Findings** | Validated low-latency log processing and real-time classification within an open-source SIEM setup. |
| **Limitation** | Limited adaptation to unlabelled zero-day attacks and sudden concept drift in network traffic. |
| **Relevance to Proposed Research** | Establishes the architectural baseline for real-time log ingestion pipelines within open-source SIEM platforms. |

---

### Paper 3: Khayat et al. (2025)

| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Explainable artificial intelligence (XAI) for mitigating analyst alert fatigue in modern Security Operations Centers |
| **Author(s)** | R. Khayat, M. Al-Makhlafi, & A. A. Zaidan |
| **Year** | 2025 |
| **Research Problem** | Black-box ML alerts in SIEM platforms lack contextual clarity, slowing down incident investigation times. |
| **Method / Technique** | Random Forest classification combined with local SHAP feature importance visualizations. |
| **Dataset / Tools** | Splunk Enterprise Security & Wazuh event log telemetry |
| **Main Findings** | Accelerated analyst triage speed by converting abstract probability scores into interpretable decision metrics. |
| **Limitation** | Computational overhead increases when calculating SHAP values on large batch sizes. |
| **Relevance to Proposed Research** | Validates the practical necessity of adding explainability layers to host and network SIEM alerts. |

---

### Paper 4: Khalfi et al. (2026)

| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Integrating machine learning inference pipelines with Wazuh SIEM for automated host-based threat response |
| **Author(s)** | B. Khalfi, A. Amine, & A. Baina |
| **Year** | 2026 |
| **Research Problem** | Lack of seamless automated active-response integration between external ML models and host-based SIEM engines. |
| **Method / Technique** | Wazuh Rule Engine integrated with custom Python ML inference REST API pipelines. |
| **Dataset / Tools** | Windows Sysmon event logs, Wazuh SIEM, Python, REST APIs |
| **Main Findings** | Confirmed automated endpoint isolation and rule triggering driven directly by ML prediction outputs. |
| **Limitation** | Requires manual model retraining cycles when OS-level host log schemas change. |
| **Relevance to Proposed Research** | Serves as a direct practical blueprint for connecting machine learning models to host-based SIEM agents. |

---

### Paper 5: Kayhan et al. (2023)

| Item | Required Information |
| :--- | :--- |
| **Paper Title** | Unsupervised zero-day anomaly detection in SIEM using Autoencoders and Isolation Forests |
| **Author(s)** | E. Kayhan, S. Yilmaz, & M. Sahin |
| **Year** | 2023 |
| **Research Problem** | Inability of traditional supervised classifiers to detect unknown (zero-day) attacks without prior training labels. |
| **Method / Technique** | Unsupervised Deep Autoencoders combined with Isolation Forest anomaly scoring. |
| **Dataset / Tools** | CSE-CIC-IDS2018 dataset, TensorFlow/Keras, Scikit-learn |
| **Main Findings** | Successfully flagged anomalous network behaviors without reliance on pre-labeled attack signatures. |
| **Limitation** | Higher rate of false positives on benign traffic bursts compared to standard supervised models. |
| **Relevance to Proposed Research** | Highlights the need for hybrid anomaly detection models to address zero-day threats within SIEM architectures. |
