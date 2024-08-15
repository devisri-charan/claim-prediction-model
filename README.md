#   Claim Prediction Model
- Endpoint `/predict`: Accepts a POST request with input data in JSON format, processes it, and returns the predicted claim amount.
- Example Input: A JSON object containing the features used in the model, such as 
```
{
    "Gender": 1,
    "Race": 1,
    "RenalDiseaseIndicator": 0, 
    "State": 39, 
    "Country": 230,
    "ChronicCond_Alzheimer":  1,
    "ChronicCond_Heartfailure":  0,
    "ChronicCond_KidneyDisease":  1,
    "ChronicCond_Cancer":  0,
    "ChronicCond_ObstrPulmonary":  0,
    "ChronicCond_Depression":  0,
    "ChronicCond_Diabetes":  1,
    "ChronicCond_IschemicHeart":  0,
    "ChronicCond_Osteoporasis":  1,
    "ChronicCond_rheumatoidarthritis":  1,
    "ChronicCond_stroke":  1,
    "PatientType":  0,
    "PotentialFraud":  1,
    "IPTotalAmount":  39204,
    "OPTotalAmount":  130,
    "ClaimSettlementDelay":  6,
    "TreatmentDuration":  6,
    "Age": 67
}
```
- Output: The predicted claim amount as a JSON response.
```
{
    "predicted_claim_amount": 26298.0
}
```
