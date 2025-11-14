import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
movies = pd.read_csv("C:\\Users\\USER\\Desktop\\microsoft\\module 2\\projects\\netflix_titles.csv")

# groups = movies.groupby([movies['type'],movies['rating']])['show_id'].size()
# fig, ax = plt.subplots()
# ax.boxplot(groups)
# plt.show()

# groups = movies.groupby(['director'])["rating_score"].mean().sort_values(ascending=False).reset_index()
# top5_groups = groups.head()
# fig, ax = plt.subplots()
# ax.bar(top5_groups['director'], top5_groups['rating_score'])
# plt.show()

# index = 0
# recommendations = list()
# movie_type = input("Enter what type of movie would you like to watch?: ")
# for i in movies['description']:
#     if movie_type.lower() in i.lower(): 
#         recommendations.append(movies.iloc[index]['title'])
#     index+=1
# # print(movies['title'].isin(np.array(recommendations)))
# new = movies[movies['title'].isin(recommendations)]
# index_title = new.sort_values(by = "rating_score",ascending=False).set_index("title")
# top_5 = index_title.head().index
# print("----------------------------------TOP PICKS FOR YOU----------------------------------")
# for i in top_5:
#     print(i)
# print("------------------------------------------------------------------------------------")