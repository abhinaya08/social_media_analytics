# Assignment 1

The learning objectives for this assignment are to learn ways to

1. Detect social “influencers” using network analytics
2. Quantify the financial value of influence
3. Identify and leverage influencers 

The assignment has two parts: I and II. In Part I, you will use training data on social influence to build a model predicting influencers, to find out the important predictors of influence, and to quantify the financial value of influence. In Part II, you will collect tweets, and use the predictors from Part I to identify 100 top influencers in a domain of your choice. 

## Part I: Find predictors of influence

The dataset for Part I can be http://www.kaggle.com/c/predict-who-is-more-influential-in-a-social-network
Each observation describes two individuals, A and B. There are 11 variables for each person based on Twitter activity, e.g., number of followers, retweets, network characteristics, etc. Each observation shows whether A > B (Choice = “1”) or B > A (Choice = “0”). 

Using the training data set (train.csv), create an analytic model for pairs of individuals to classify who is more influential
1. Check if you should use all variables
2. Perhaps a transformation of A/B or A-B variables will be better than using A and B variables separately. This may also be easier to interpret. 

### Report the confusion matrix of your “best” model (provide screenshot)
![Confusion matrix](confusion_matrix.PNG)

### From your model, which factors are best predictors of influence? (Provide screenshots). 
![Feature Importance](feature_importance.PNG)

### Are there any surprises here? How can a business use your model/results? 
Our model can be especially useful if a business wants to identify influencers or ambassadors for its products. As we know, endorsements play a huge role today in customer conversion. Customers often spend a lot of time perusing reviews, especially leaning towards recommendations giving by gurus in that field. 


### What is the lift in expected net profit from using your analytic model (versus not using analytics)? What is the lift in net profit from using a perfect analytic model (versus not using analytics)?

![Lift calculations](lift_chart_1.PNG)

![Lift chart](lift_chart_2.PNG)

## Part II: Finding influencers from Twitter 

Collect about 5000 tweets on any topic (e.g., politics, sports, current events, etc.). In addition to the tweet itself, the Twitter API provides a large quantity of information about the tweet as well as the author. Fetch all of this additional information along with the tweets. 

Most social network analysis tools (e.g., NodeXL, Gephi or UCINet) will take the first two columns and draw arrows from the user in the left column to the one in the right – You can also use Networkx in Python to draw networks. Note that in most cases the set of tweets you may fetch will not have the original tweet that is being retweeted by someone else. E.g., a tweet in your data (tweeted by, say, @XYZ) may be:  “RT @ABC Working on my social media assignment.” 

It is quite possible that you will not have the original tweet by @ABC in your data. Still an arrow should go from @XYZ to @ABC. Therefore, even if you have fetched 5000 tweets by 5000 unique users, your network may consist of a much larger set of users.

Calculate the degree, betweenness and closeness of each node in the above network. 

### Using the results from Part I, create a list of top 50 influencers from the tweets. 
Here is one way to do it. Suppose four factors – retweets, listed count, # followers and network characteristic 1 turned out to be the most important indicators of influence in assignment 1. Now create a score for each author from your Twitter data: 

$Score = w1*retweets + w2*listed_count + w3*#followers + w4*(scaled degree + betweenness + closeness)$ 

where w1+w2+w3+ w4 =1 Choose the weights (it is subjective) such that bigger weights are given to factors that were more important (as judged by coefficients and p values in Part I). You should normalize your data before creating the overall scores.  Note that the Kaggle data doesn’t show what each network characteristic means. However, generally such metrics are presented in the following sequence: Degree, betweenness and closeness. 

## Code etc

1. Part 1 Python Notebook [(here)](https://github.com/abhinaya08/social_media_analytics/blob/master/Assignment1/SMAPart1.ipynb)
2. Part 2 Python Notebook [(here)](https://github.com/abhinaya08/social_media_analytics/blob/master/Assignment1/SMA%20Part%202.ipynb)
3. Part 2 Twitter Scraper [(here)](https://github.com/abhinaya08/social_media_analytics/blob/master/Assignment1/twitter_scraper2.py)
4. Part 2 scraped tweets [(here)](https://github.com/abhinaya08/social_media_analytics/blob/master/Assignment1/part2.csv)



