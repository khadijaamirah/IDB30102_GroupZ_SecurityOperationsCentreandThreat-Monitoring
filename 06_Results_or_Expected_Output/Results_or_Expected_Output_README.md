# Results / Expected Output

## Expected Detection Output

The proposed system is expected to classify network traffic into two categories:

- Benign
- Malicious

The Random Forest model will process the prepared CIC-IDS2017 data and produce a classification result for each input instance. Malicious traffic will be identified as a potential cyber threat and the detection result will be demonstrated through the Wazuh SIEM environment.

## Expected Evaluation

The proposed Random Forest model will be compared with a Decision Tree baseline using the same dataset, preprocessing and testing conditions.

The evaluation will use:

- Accuracy
- Precision
- Recall
- F1-score
- False Positive Rate (FPR)

## Expected Outcome

The proposed approach is expected to demonstrate improved cyber threat detection performance compared with the Decision Tree baseline. In particular, the Random Forest model is expected to achieve a higher F1-score while maintaining suitable precision and recall.

## Expected SIEM Output

The Wazuh environment is expected to display the detection result as a security monitoring output. Malicious traffic should generate a threat detection or alert output that can support SOC analyst monitoring.

## Note

The results in this folder represent expected outputs at the research proposal stage. Final experimental results will be added after the model development and evaluation stages are completed.
