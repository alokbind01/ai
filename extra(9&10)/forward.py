class ForwardChainingDiagnosis:
    def __init__(self):
        self.rules = {
            "Flu": ["Fever", "Cough"],
            "Common Cold": ["Cough", "Fatigue"],
            "Fatigue Syndrome": ["Fever", "Fatigue"],
        }

    def forward_chain(self, symptoms):
        possible_diseases = []
        for disease, required_symptoms in self.rules.items():
            if all(symptom in symptoms for symptom in required_symptoms):
                possible_diseases.append(disease)
        return possible_diseases


def forward_chaining_test():
    diagnosis = ForwardChainingDiagnosis()
    user_input = input("Enter your symptoms separated by commas (e.g., Fever, Cough, Fatigue): ")
    symptoms = [s.strip().title() for s in user_input.split(",")]

    possible_diseases = diagnosis.forward_chain(symptoms)
    if possible_diseases:
        print("Possible diseases based on your symptoms:")
        for disease in possible_diseases:
            print(f"- {disease}")
    else:
        print("No matching diseases found.")


# Test the forward chaining diagnosis
forward_chaining_test()
