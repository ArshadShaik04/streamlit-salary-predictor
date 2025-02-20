from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(data):
    x = np.array(data['YearsExperience']).reshape(-1, 1)
    y = np.array(data['Salary'])
    model = LinearRegression()
    model.fit(x, y)
    return model

def predict_salary(model, years_experience):
    return model.predict(np.array([[years_experience]]))[0]
