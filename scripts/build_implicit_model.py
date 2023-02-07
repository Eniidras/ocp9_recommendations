from joblib import load, dump
from implicit.als import AlternatingLeastSquares

dir_path = "../static/model/"

user_clicks = load(dir_path+"user_clicks.joblib")

model = AlternatingLeastSquares(factors=64, regularization=0.05, alpha=2.0)
model.fit(user_clicks)

# if required 
model = model.to_cpu()

dump(model, dir_path+"model_cpu.joblib")
