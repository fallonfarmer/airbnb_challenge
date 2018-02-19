import pandas as pd

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

train.shape
train.head()
train.describe()
train.dtypes
test.shape
test.describe()

# clean data
# determine the number of missing entries in each column
for col in train.columns:
    print col + ', Number of Missing Values:', len(train[col][train[col].isnull()])
# missing values for bathrooms, bedrooms, beds, review_scores_rating
# first_review, host_has_profile_pic, host_identity_verified, host_response_rate
# host_since, last_review, neighbourhood, thumbnail_url, zipcode
