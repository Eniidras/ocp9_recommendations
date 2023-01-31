from joblib import load

dir_path = "static/model/"

model = load(dir_path+"model_cpu.joblib")
user_clicks = load(dir_path+"user_clicks.joblib")

def recommend(user_id):
    ids, scores = model.recommend(user_id, user_clicks[user_id], N=10, filter_already_liked_items=True)
    return ids
