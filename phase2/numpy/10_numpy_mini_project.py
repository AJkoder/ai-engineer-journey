import numpy as np

# Mini-project: Analyse fictional HeartTalk feedback.
# These are sample ratings, not real user conversations.

helpfulness_ratings = np.array([4, 5, 3, 5, 4, 2, 5, 4])
response_times = np.array([1.2, 1.5, 2.1, 1.1, 1.8, 2.5, 1.3, 1.6])

print("HEARTTALK PERFORMANCE REPORT")
print("-" * 35)

print("Number of feedback ratings:", helpfulness_ratings.size)
print("Average helpfulness:", np.mean(helpfulness_ratings))
print("Median helpfulness:", np.median(helpfulness_ratings))
print("Lowest rating:", np.min(helpfulness_ratings))
print("Highest rating:", np.max(helpfulness_ratings))

print("\nAverage response time:", np.mean(response_times), "seconds")
print("Fastest response:", np.min(response_times), "seconds")
print("Slowest response:", np.max(response_times), "seconds")

# Count ratings of 4 or higher.
positive_ratings = helpfulness_ratings[helpfulness_ratings >= 4]
print("\nRatings of 4 or higher:", positive_ratings.size)

# Percentage of positive ratings.
positive_percentage = (
    positive_ratings.size / helpfulness_ratings.size
) * 100

print("Positive rating percentage:", positive_percentage, "%")

# Practice:
# 1. Add two more feedback ratings.
# 2. Calculate the standard deviation of helpfulness ratings.
# 3. Find all response times below 1.5 seconds.
# 4. Explain what these statistics tell us about the chatbot.
