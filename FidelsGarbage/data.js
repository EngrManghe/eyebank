const eye_data =[
    {
        "medical_records": {
          "patient_details": {
            "name": "Joanna Sprague",
            "age": 70,
            "medical_history": [
              "CAD (Coronary Artery Disease)",
              "MI (Myocardial Infarction) in April 2024",
              "NSTEMI complicated by cardiogenic shock",
              "LVEF 20-25%",
              "Acute systolic heart failure",
              "Diabetes mellitus",
              "History of bipolar disorder"
            ],
            "hospital_course": [
              "Admitted on 09/19/2024",
              "Underwent PCI (Percutaneous Coronary Intervention)",
              "Impella device inserted on 09/21/2024 and removed on 09/27/2024",
              "Remained intubated with mechanical ventilatory support",
              "Discharged on 10/05/2024"
            ]
          },
          "medications": [
            "Amiodarone (IV drip)",
            "Primacor (Milrinone) drip",
            "Dual antiplatelet therapy (Aspirin 81 mg and Ticagrelor 90 mg)",
            "Spironolactone 12.5 mg daily",
            "Insulin drip",
            "Zosyn (Antibiotic for infection)",
            "Midodrine for blood pressure support"
          ],
          "hospital_discharge": "Discharged on 10/05/2024 after complications with cardiogenic shock and respiratory failure"
        },
        "septics": {
          "cause": "Sepsis due to suspected infection without a clear source",
          "complications": [
            "Fevers and leukocytosis",
            "No organism isolated in current cultures",
            "MRSA PCR negative",
            "Candida in urine (likely contaminant)"
          ],
          "treatment": [
            "Antibiotics (Zosyn)",
            "Mechanical ventilation",
            "Monitored for leukocytosis (WBC 17.2)",
            "Continued fluid management"
          ],
          "status": "Infection source not fully identified but treated with broad-spectrum antibiotics"
        },
        "blood_transfusion": {
          "reason": "Normocytic anemia due to critical illness",
          "hemoglobin_levels": [
            {"date": "09/30/2024", "value": "8.8 g/dL"},
            {"date": "10/02/2024", "value": "7.7 g/dL"},
            {"date": "10/03/2024", "value": "7.4 g/dL"}
          ],
          "transfusions": [
            {
              "date": "10/03/2024",
              "amount": "1 unit of packed cells",
              "target_hemoglobin": "> 8 g/dL due to cardiac disease"
            }
          ]
        }
      },
      {
        "medical_records": {
          "patient_details": {
            "name": "Ralph C. Samson",
            "age": 68,
            "medical_history": [
              "Hypertension",
              "Hip replacement surgery",
              "History of gastric bypass surgery",
              "History of joint replacement surgery",
              "History of rotator cuff repair",
              "History of abdomen surgery"
            ],
            "hospital_course": [
              "Patient found unresponsive by his wife on 10/07/2024 after hip replacement surgery on 10/05/2024.",
              "EMS initiated CPR and intubation in the field; epinephrine was administered.",
              "Arrived at the hospital in asystole and was pronounced dead after failed resuscitation efforts."
            ]
          },
          "medications": [
            "Epinephrine 1 mg IV (administered by EMS)",
            "Sodium bicarbonate 8.4% injection IV"
          ],
          "hospital_discharge": "Deceased on 10/07/2024 due to cardiac arrest and asystole."
        },
        "septics": {
          "cause": "No direct mention of sepsis in the records. Death due to cardiac arrest and asystole after hip replacement surgery.",
          "complications": [
            "Asystole",
            "Cardiac arrest"
          ],
          "treatment": [
            "CPR and advanced cardiac life support in the field and in the emergency department",
            "Intubation and administration of epinephrine and sodium bicarbonate"
          ],
          "status": "Patient was pronounced dead on arrival to the emergency department."
        },
        "blood_transfusion": {
          "reason": "No blood transfusion administered during this encounter."
        }
      },
      {
        "medical_records": {
          "patient_details": {
            "name": "Marjorie R. Ellis",
            "age": 68,
            "medical_history": [
              "MASH cirrhosis (Metabolic Associated Steatohepatitis Cirrhosis)",
              "Recurrent urinary tract infections (UTIs)",
              "Hypertension (HTN)",
              "Acute respiratory failure",
              "Persistent metabolic encephalopathy",
              "Malnutrition",
              "Volume overload"
            ],
            "hospital_course": [
              "Admitted on 10/01/2024 with altered mental status",
              "Treated for sepsis secondary to hospital-acquired pneumonia (HAP) and multi-drug resistant organism (MDRO) urinary tract infection (UTI)",
              "Course further complicated by acute respiratory failure and hepatic encephalopathy",
              "Hospital stay marked by volume overload, metabolic encephalopathy, and eventual transition to DNR-CC (Do Not Resuscitate-Comfort Care)",
              "Patient expired on 10/13/2024"
            ]
          },
          "medications": [
            "Cefepime 2g IV every 12 hours",
            "Meropenem (initial antibiotic)",
            "Vancomycin (discontinued after negative MRSA swab)",
            "Lactulose",
            "Rifaximin"
          ],
          "hospital_discharge": "Patient transitioned to comfort care (DNR-CC) and expired on 10/13/2024"
        },
        "septics": {
          "cause": "Sepsis due to multi-drug resistant Enterobacter cloacae UTI and hospital-acquired pneumonia (HAP)",
          "complications": [
            "Altered mental status",
            "Hypernatremia",
            "Respiratory failure",
            "Persistent fever and tachypnea"
          ],
          "treatment": [
            "Meropenem (initial antibiotic for UTI)",
            "Cefepime (ongoing antibiotic for pneumonia)",
            "Fluid resuscitation",
            "Monitoring of blood cultures and respiratory cultures"
          ],
          "status": "Sepsis worsened, leading to respiratory failure, metabolic encephalopathy, and eventual death on 10/13/2024"
        },
        "blood_transfusion": {
          "reason": "Pancytopenia and anemia exacerbated by acute illness",
          "hemoglobin_levels": [
            {
              "date": "10/03/2024",
              "value": "6.2 g/dL"
            },
            {
              "date": "10/05/2024",
              "value": "8.1 g/dL"
            }
          ],
          "transfusions": [
            {
              "date": "10/03/2024",
              "amount": "1 unit of packed red blood cells",
              "target_hemoglobin": "Transfuse for hemoglobin <7 g/dL and platelets <10"
            }
          ]
        }
      },
      {
        "medical_records": {
          "patient_details": {
            "name": "Jeffrey Cochran",
            "age": 59,
            "medical_history": [
              "Emphysema",
              "Metastatic tonsil squamous cell carcinoma",
              "Hypothyroidism",
              "Hypertension",
              "Chronic constipation"
            ],
            "hospital_course": [
              "Admitted on 09/16/2024 with sepsis secondary to pneumonia and empyema",
              "Underwent right thoracotomy, pleurectomy, and right lower lobectomy on 09/17/2024",
              "Chest tube placement for drainage",
              "Treated with antibiotics including cefepime and metronidazole",
              "Discharged on 10/15/2024"
            ]
          },
          "medications": [
            "Cefepime",
            "Metronidazole",
            "Norco (for pain)",
            "Dilaudid (for pain)",
            "Levothyroxine",
            "Lisinopril"
          ],
          "hospital_discharge": "Discharged on 10/15/2024 after treatment for pneumonia, empyema, and sepsis"
        },
        "septics": {
          "cause": "Sepsis secondary to right lower lobe pneumonia and empyema",
          "complications": [
            "Leukocytosis",
            "Respiratory distress",
            "Normocytic anemia"
          ],
          "treatment": [    
            "Antibiotics (cefepime, metronidazole)",
            "Right thoracotomy with pleurectomy and lobectomy",
            "Chest tube for drainage",
            "Continued IV antibiotics for 3 weeks"
          ],
          "status": "Patient recovered after surgical intervention and antibiotic therapy, discharged on 10/15/2024"
        },
        "blood_transfusion": {
          "reason": "Normocytic anemia secondary to acute blood loss",
          "hemoglobin_levels": [
            {
              "date": "09/24/2024",
              "value": "8.2 g/dL"
            }
          ],
          "transfusions": [
            {
              "date": "Not administered",
              "target_hemoglobin": "Transfuse for hemoglobin <7 g/dL"
            }
          ]
        }
      },

        
        
         
         
]