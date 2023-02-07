from joblib import load

dir_path = "static/model/"

model = load(dir_path+"model_cpu.joblib")
user_clicks = load(dir_path+"user_clicks.joblib")

def recommend(user_id, number_items=5, filter_already_liked_items=False):
    ids, scores = model.recommend(user_id, user_clicks[user_id], N=number_items, filter_already_liked_items=filter_already_liked_items)
    return ids
