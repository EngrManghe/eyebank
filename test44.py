test44.py 
import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split
from surprise.accuracy import rmse
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Convert the provided data into a DataFrame
data_dict = {
    "UserID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
               39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    "MovieID": list(range(101, 151)),
    "Rating": [5, 4, 5, 3, 5, 5, 2, 5, 4, 5, 5, 3, 5, 4, 2, 5, 4, 5, 3, 5, 
               5, 4, 5, 3, 5, 4, 5, 3, 5, 4, 5, 3, 5, 4, 5, 3, 4, 5, 3, 5, 
               5, 5, 4, 5, 4, 5, 4, 5, 5, 5]
}
df = pd.DataFrame(data_dict)

# Step 2: Prepare data for the Surprise library
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[["UserID", "MovieID", "Rating"]], reader)

# Step 3: Split data into training and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Step 4: Train a collaborative filtering model (SVD)
model = SVD()
model.fit(trainset)

# Step 5: Evaluate the model
predictions = model.test(testset)
rmse_value = rmse(predictions)

# Step 6: Generate top-5 recommendations for a specific user (e.g., UserID 1)
user_id = 1
all_movie_ids = df['MovieID'].unique()
watched_movies = df[df['UserID'] == user_id]['MovieID']
unwatched_movies = [movie for movie in all_movie_ids if movie not in watched_movies.values]

# Predict ratings for unwatched movies
recommendations = [(movie, model.predict(user_id, movie).est) for movie in unwatched_movies]
top_recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)[:5]

# Convert recommendations to a DataFrame for display
recommendations_df = pd.DataFrame(top_recommendations, columns=["MovieID", "PredictedRating"])
recommendations_df

# Visualize the top recommendations
plt.figure(figsize=(8, 6))
sns.barplot(x="MovieID", y="PredictedRating", data=recommendations_df, palette="viridis")
plt.title(f"Top-5 Recommendations for User {user_id}", fontsize=16)
plt.xlabel("MovieID", fontsize=12)
plt.ylabel("Predicted Rating", fontsize=12)
plt.show()
