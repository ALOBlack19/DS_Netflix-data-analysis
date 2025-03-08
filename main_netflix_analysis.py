#!/usr/bin/env python
# coding: utf-8

# # MINI PROJECT - NETFLIX

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
netflix = pd.read_csv("netflix_data.csv")
print(netflix)


# ## Data Cleaning and check

# ### 1. Check Missing values

# In[3]:


netflix.isnull().sum() 
netflix.isna().sum() 


# ### 2. Check duplicates

# In[4]:


duplicates = netflix[netflix.duplicated()]
print(duplicates)


# In[5]:


dup_sum = netflix.duplicated().sum()
print(dup_sum)


# ### 3. Check inconsistent data types

# In[6]:


print(netflix.info())


# ### 4. Check unexpected values

# #### Outliers in numerical columns

# In[7]:


description = netflix.describe()
desc_std = description.loc[["std", "mean", "min", "max"]]

desc_std.plot(kind = "bar")
plt.title("Statistical Analysis", weight = "bold")

print(desc_std)
plt.show()

# ### 5. Check white spaces and formatting Issues

# In[8]:


netflix["release_year"] = netflix["release_year"].astype(str).str.strip()
netflix["release_year"] = netflix["release_year"].astype(int)
print(netflix["release_year"])


# In[9]:


netflix["duration"] = netflix["duration"].astype(str).str.strip()
netflix["duration"] = netflix["duration"].astype(int)
print(netflix["duration"])


# ### 6. Check for Incorrect Data Entries

# In[10]:


rel_dur = netflix[["release_year", "duration"]]
dur_check_boolean = rel_dur["duration"] > 360
dur_check = rel_dur[rel_dur["duration"] > 360]
print(dur_check)


# In[11]:


years_check_boolean = rel_dur["release_year"].astype(str).str.len() > 4
years_check = rel_dur[rel_dur["release_year"].astype(str).str.len() > 4] # found that to check if the len of the values in the release_year column is greater than 4, I needed to change the format to string using(astype(str),
# and performing (.str.len()) because is the pandas function to calculate the length.
print(years_check)


# In[12]:


unex_check = dur_check_boolean.any() or years_check_boolean.any()
print(unex_check)


# ### 7. Check for Column name Issues

# In[13]:


print(netflix.columns)


# In[14]:


# netflix.columns = netflix.columns.str.strip()
# netflix.columns = netflix.str.lower()
# netflix.columns = netflix.str.replace(' ', '_')

# Any of the functions above were necessary.


# # Part 1: Understanding more about movies from the 1990s decade.

# ### Filtering the Netflix content type to show only the movies

# In[15]:


netflix_movies = netflix[netflix["type"] == "Movie"]
print(netflix_movies)


# In[16]:


# netflix_movies


# ### Filtering the release years

# In[17]:


netflix_movies_1990s = netflix_movies[(netflix_movies["release_year"] > 1989) & (netflix_movies["release_year"] < 2000)]
print(netflix_movies_1990s)


# ### Filtering duration

# In[22]:


netflix_movies_1990s_90m = netflix_movies_1990s[netflix_movies_1990s["duration"] < 90]
print(netflix_movies_1990s_90m.info())


# ### Counting the number of movies based on their duration

# In[19]:


m_freq_dur = netflix_movies_1990s_90m.groupby("duration").size()
max_freq = m_freq_dur.max()
movie_minutes = m_freq_dur[m_freq_dur == max_freq].index[0]

print(f"The most frequent movie durantion in the 1990s is: {movie_minutes} minutes in {max_freq} different movies")
num_movies_dur = netflix_movies_1990s_90m.groupby("duration")["title"].count()
num_movies_dur.plot(kind = "bar", color = "firebrick", rot = 45)
plt.title("Number of movies based on their duration", weight = "bold")
plt.ylabel("Counting of movies", weight = "bold")
plt.xlabel("Duration in minutes", weight = "bold")
plt.show()

# ### Number of short action movies

# In[20]:


act_movie_90s_90m = netflix_movies_1990s_90m[netflix_movies_1990s_90m["genre"] == "Action"]
short_movie_count = act_movie_90s_90m["genre"].value_counts()

print("The number of short actions movies is:\n ", short_movie_count)


# In[21]:


filter_action = act_movie_90s_90m[["type", "release_year", "duration", "genre"]]
print(filter_action)


# In[22]:


print(filter_action.shape())


# # Part 2: Investigating the trend in the duration of movies available on Netflix
# ### What does this trend look like over a longer period of time?

# ### Selecting only the necessary data to reach the goal

# In[23]:


nf_title_year = netflix_movies[["title","release_year", "duration"]]
print(nf_title_year)


# ### Sorting the dataframe by the release_years column

# In[24]:


sort_release = nf_title_year.sort_values(by = "release_year")
print(sort_release)


# ### Creating the average movie duration for each year

# In[25]:


avg_nf_dur_year = sort_release.groupby("release_year")["duration"].mean()
print(avg_nf_dur_year)


# In[26]:


ax = avg_nf_dur_year.plot(kind = "line", x = "release_year", y = "duration", color = "firebrick")
ax.set_xticks(range(1942,2023,10))
plt.show()

# ## Is this explainable by something like the genre of entertainment?
# ####        One of the possible answers to this question is how many different kinds of entertainment have appeared in the last 30 years, but that is not the only reason for the movie duration to decrease.
# ###### More information in the presentation slides.

# In[43]:


genre_exp = netflix_movies[["title", "release_year", "duration", "genre"]]
print(genre_exp)





