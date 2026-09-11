# 02_Literature_Review: Supporting Materials

This directory contains supporting analysis files and documentation for Chapter 2, fulfilling the UniKL CDDH v4 Appendix O assessment requirements.

---

## 1. Literature Review Analysis Table

| No. | Author(s) & Year | Key ML Method / Approach | Dataset / Telemetry Used | Core Findings | Gaps / Limitations |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **1** | Kim & Kwon (2022) | Random Forest, SVM, KNN | CIC-IDS2017 | Supervised models yield strong static classification baselines. | High false alarms on live traffic. |
| **2** | Muhammad et al. (2023) | Ensemble Trees, XGBoost | NSL-KDD, UNSW-NB15 | Improves boundary detection and decision accuracy. | Struggles with concept drift. |
| **3** | Kayhan et al. (2023) | Autoencoders, Isolation Forest | CSE-CIC-IDS2018 | Detects zero-day anomalies without training labels. | Higher false positive rate on benign bursts. |
| **4** | Sebbar et al. (2023) | XGBoost, Logstash Extraction | Enterprise ELK Logs | Proves real-time log parsing and ML classification. | Tested on static network rules. |
| **5** | Nurusheva et al. (2024) | Soft-Voting, SHAP (XAI) | Kaggle SOC Logs | Reduces false-positive alerts and provides risk scoring. | Evaluated off-line, non-streaming. |
| **6** | Ustz et al. (2024) | CNN, LSTM Hybrids | CIC-IDS2017/2018 | Captures spatio-temporal dependencies in packet flows. | Heavy computational overhead. |
| **7** | Najafi et al. (2024) | GraphSAGE (GNN) | LANL / OpTC Logs | Maps event logs into graphs for lateral movement detection. | High memory requirements. |
| **8** | Kapera & Niemiec (2025) | Decision Trees, XGBoost | Splunk ES Streams | Validates low-latency log processing in enterprise SIEM. | Limited zero-day coverage. |
| **9** | Hamza et al. (2025) | Dynamic Risk Thresholding | BETH Dataset | Adjusts alert thresholds dynamically to lower false positives. | Requires continuous recalculation. |
| **10** | Ramavath et al. (2025) | Variational Autoencoders (VAE) | UNSW-NB15 | Reconstructs normal baselines to isolate stealthy attacks. | Complex hyperparameter tuning. |
| **11** | Artioio et al. (2025) | BiLSTM, Deep Neural Networks | SIEVE / Vendor Logs | Tracks multi-stage cyber attacks over time windows. | High latency on edge devices. |
| **12** | Khayat et al. (2025) | Random Forest + SHAP | Splunk / Wazuh Logs | Accelerates triage times using feature importance. | SHAP calculation latency on large batches. |
| **13** | Abd Bahrim et al. (2026) | Hybrid CNN-KNN | Network Telemetry | Reduces computational overhead in edge-SIEM setups. | Lower detection rate for complex zero-days. |
| **14** | Yauri et al. (2026) | LightGBM, CatBoost | Cloud SIEM Telemetry | Benchmarks scalable gradient boosting in cloud environments. | Degrades under unmonitored log schema shifts. |
| **15** | Khalfi et al. (2026) | Wazuh Engine + ML Pipeline | Sysmon Event Logs | Validates automated endpoint response driven by ML. | Requires manual retraining cycles. |

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

---

## 7. References Supporting the Proposed Methodology

1. **Abd Bahrim, M. F., Harun, N., & Ismail, Z. (2026).** Hybrid CNN-KNN architecture for lightweight threat detection in edge-SIEM environments. *Journal of Cyber Security and Technology*, 14(1), 45–58.
2. **Hamza, A., Benkirane, S., & Guezzaz, A. (2025).** Lowering false positive rates in SOC environments using dynamic risk thresholding. *Computers & Security*, 138, Article 103650.
3. **Kayhan, E., Yilmaz, S., & Sahin, M. (2023).** Unsupervised zero-day anomaly detection in SIEM using Autoencoders and Isolation Forests. *Computers & Security*, 124, Article 102980.
4. **Khalfi, B., Amine, A., & Baina, A. (2026).** Integrating machine learning inference pipelines with Wazuh SIEM for automated host-based threat response. *Journal of Information Security and Applications*, 78, Article 103720.
5. **Khayat, R., Al-Makhlafi, M., & Zaidan, A. A. (2025).** Explainable artificial intelligence (XAI) for mitigating analyst alert fatigue in modern Security Operations Centers. *Expert Systems with Applications*, 245, Article 123100.
6. **Nurusheva, A., Smailov, N., & Omarov, B. (2024).** Alert fatigue reduction in SOCs using soft-voting ensembles and SHAP feature importance. *IEEE Access*, 12, 18450–18462.
7. **Sebbar, A., Hajji, S., & El Kettani, M. D. (2023).** Real-time log parsing and threat classification in open-source ELK Stack architectures. *International Journal of Information Security*, 22(4), 981–995.
