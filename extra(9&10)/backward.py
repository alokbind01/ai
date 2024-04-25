class BackwardChainingDiagnosis:
    def __init__(self):
        self.rules = {
            "Flu": ["Fever", "Cough", "Fatigue"],
            "Common Cold": ["Cough", "Fatigue"],
            "Fatigue Syndrome": ["Fever", "Fatigue"],
        }

    def backward_chain(self, disease):
        required_symptoms = self.rules.get(disease, [])
        print(f"To confirm {disease}, check for the following symptoms: {', '.join(required_symptoms)}")
        user_input = input(f"Enter 'yes' if the patient has the symptom, separated by commas for these symptoms - {', '.join(required_symptoms)}: ")
        symptoms_present = [s.strip().lower() == 'yes' for s in user_input.split(",")]

        if all(symptoms_present):
            print(f"The hypothesis that the patient might have {disease} is supported.")
        else:
            print(f"The hypothesis that the patient might have {disease} is not supported.")

def backward_chaining_test():
    diagnosis = BackwardChainingDiagnosis()
    user_input = input("Enter the disease you want to diagnose: ")
    disease = user_input.strip().title()

    diagnosis.backward_chain(disease)

# Test the backward chaining diagnosis
backward_chaining_test()
