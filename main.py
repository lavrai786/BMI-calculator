import json
list1 = []
list2 = []
list3 = []
data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}, {"Gender": "Male", "HeightCm": 161, "WeightKg":
                                                              85}, {"Gender": "Male", "HeightCm": 180, "WeightKg": 77}, {"Gender": "Female", "HeightCm": 166,
                                                                                                                         "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
                                                                                                                                                                                                  "HeightCm": 167, "WeightKg": 82}]
for i in data:
    list1.append(i['WeightKg'])
    list2.append(i['HeightCm']/100)
    BMI = [round(x/y, 2) for x, y in zip(list1, list2)]
list3.append(BMI)
for i in list3[-1]:
    if i <= 18.4:
        print("BMI of the person is:", i, "RISK_LEVEL:", "Malnutrition risk")
    elif i >= 18.5 and i <= 24.9:
        print("BMI of the person is:", i, "RISK_LEVEL:", "Low risk")
    elif i >= 25 and i <= 29.9:
        print("BMI of the person is:", i, "RISK_LEVEL:", "Enhanced risk")
    elif i >= 30 and i <= 34.9:
        print("BMI of the person is:", i, "RISK_LEVEL:", "Medium risk")
    elif i >= 35 and i <= 39.9:
        print("BMI of the person is:", i, "RISK_LEVEL:", "High risk")
    elif i >= 40:
        print("BMI of the person is:", i, "RISK_LEVEL:", "Very high risk")
