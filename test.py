import joblib
import numpy as np


def get_user_input(feature_names):
    features = []

    for feature_name in feature_names:
        while True:
            try:
                value = float(input(f'Enter value for {feature_name}: ')) or 0
                break
            except ValueError:
                print('Invalid input. Please enter a numeric value.')

        features.append(value)
    print(features)
    return np.array(features).reshape(1, -1)


def make_prediction(model_filename, user_input):
    print(user_input)
    model = joblib.load(model_filename)
    prediction = model.predict(user_input)[0]
    proba = model.predict_proba(user_input).max()
    return prediction, proba


features = ['age', 'blood pressure', 'albumin',
            'sugar', 'pus cellc cumps', 'bacteria', 'blood glucose rand',
            'blood urea', 'serum creatinine', 'hypertension',
            'diabetes mellitus',
            'caronory artery disease', 'appetite', 'pedal edema', 'anemia']

# user_input = get_user_input(features)
user_input = np.array([10.0, 0, 0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0]).reshape(1, -1)
prediction, proba = make_prediction(
    "Random_Forest_model.joblib", user_input)
print(
    f"Your test result is {'positive' if prediction == 1 else 'negative'}.")
print(f"The certanity of prediction: {proba*100:.2f}%")
