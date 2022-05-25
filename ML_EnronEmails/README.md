## Introduction

The goal of this project is to use the Enron dataset to determine persons of interest (POIs) using a machine learning algorithm. During the investigation into the company, the FERC created the Enron dataset. It contains roughly 146 users and those users are mostly senior management. As for the actual POIs, there were 18. I used 20 features of those given by Udacity.

The sheer size of this dataset is useful in applying machine learning algorithms as regular techniques would take too long and probably be prone to errors. Also, machine learning is valuable in researching this data if we don’t know exactly what we are looking for. We know we want to find the POIs but it is how we find them that makes machine learning application so valuable. It’s not as easy as following the money to the top executives, and in this case, we are following the emails.

## Conclusion

After tuning our Adaboost classifier using our hyperparameters, we received a 4% boost in our accuracy using our feature set. This means we could potentially identify a POI from our dataset with an 88% chance of choosing whether the POI was true. While all of our metrics increased as well, there is still room for improvement. A similar process from hypertuning parameters could be set up to increase precision, recall and our f1 score. Right now our precision of 66% means we'd be finding 33% false positive flags which doesn't sit well with me. I also think there are other features we could explore and I bet there are more outliers in that data as well.
