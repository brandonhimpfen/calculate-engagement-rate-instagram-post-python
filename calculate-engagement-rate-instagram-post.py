# Import necessary modules
import math

# Define function to calculate engagement rate
def calc_engagement_rate(likes, comments, followers):
    engagement_rate = ((likes + comments) / followers) * 100
    return round(engagement_rate, 2)

# Define example values for likes, comments, and followers
likes = 1000
comments = 200
followers = 5000

# Calculate engagement rate using example values
engagement_rate = calc_engagement_rate(likes, comments, followers)

# Print result
print("Engagement rate: {}%".format(engagement_rate))
