from joblib import dump, load
from scipy.sparse import csr_matrix
from implicit.nearest_neighbours import bm25_weight

dir_path = "path_to_data"

clicks = load(dir_path + "clicks.csv")

articles = []
users = []
data = []

for id, row in clicks.iterrows():
    articles.append(articles_categories[row["click_article_id"]])
    users.append(row["user_id"])
    data.append(1)

users_clicks = csr_matrix(
    (data, (articles, users)),
    shape = (364047,322897) #max consulted article id +1, number of users
)

categories_users_clicks = bm25_weight(categories_users_clicks, K1=100, B=0.8)
user_clicks = categories_users_clicks.T.tocsr()

dump(user_clicks, dir_path+"saves/user_clicks.joblib")