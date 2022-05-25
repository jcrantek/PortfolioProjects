# Project 5: Explore and Summarize Data

#### Jeremy Crantek

#### August 20th, 2020

## Introduction

In this data analysis, we will be looking through the ‘wineQualityReds.csv’ file using the R language.

## Data Summary

```
## [1] 1599 12
```
The wines dataset contains 1599 records with 12 variables.

```
## 'data.frame': 1599 obs. of 12 variables:
## $ fixed.acidity : num 7.4 7.8 7.8 11.2 7.4 7.4 7.9 7.3 7.8 7. ...
## $ volatile.acidity : num 0.7 0.88 0.76 0.28 0.7 0.66 0.6 0.65 0.58 0. ...
## $ citric.acid : num 0 0 0.04 0.56 0 0 0.06 0 0.02 0. ...
## $ residual.sugar : num 1.9 2.6 2.3 1.9 1.9 1.8 1.6 1.2 2 6. ...
## $ chlorides : num 0.076 0.098 0.092 0.075 0.076 0.075 0.069 0.065 0.073 0. ...
## $ free.sulfur.dioxide : num 11 25 15 17 11 13 15 15 9 17 ...
## $ total.sulfur.dioxide: num 34 67 54 60 34 40 59 21 18 102 ...
## $ density : num 0.998 0.997 0.997 0.998 0. ...
## $ pH : num 3.51 3.2 3.26 3.16 3.51 3.51 3.3 3.39 3.36 3. ...
## $ sulphates : num 0.56 0.68 0.65 0.58 0.56 0.56 0.46 0.47 0.57 0. ...
## $ alcohol : num 9.4 9.8 9.8 9.8 9.4 9.4 9.4 10 9.5 10. ...
## $ quality : Ord.factor w/ 6 levels "3"<"4"<"5"<"6"<..: 3 3 3 4 3 3 3 5 5 3 ...
```
These are the 12 variables we will be working with during this data analysis.


```
## fixed.acidity volatile.acidity citric.acid residual.sugar
## Min. : 4.60 Min. :0.1200 Min. :0.000 Min. : 0.
## 1st Qu.: 7.10 1st Qu.:0.3900 1st Qu.:0.090 1st Qu.: 1.
## Median : 7.90 Median :0.5200 Median :0.260 Median : 2.
## Mean : 8.32 Mean :0.5278 Mean :0.271 Mean : 2.
## 3rd Qu.: 9.20 3rd Qu.:0.6400 3rd Qu.:0.420 3rd Qu.: 2.
## Max. :15.90 Max. :1.5800 Max. :1.000 Max. :15.
## chlorides free.sulfur.dioxide total.sulfur.dioxide
## Min. :0.01200 Min. : 1.00 Min. : 6.
## 1st Qu.:0.07000 1st Qu.: 7.00 1st Qu.: 22.
## Median :0.07900 Median :14.00 Median : 38.
## Mean :0.08747 Mean :15.87 Mean : 46.
## 3rd Qu.:0.09000 3rd Qu.:21.00 3rd Qu.: 62.
## Max. :0.61100 Max. :72.00 Max. :289.
## density pH sulphates alcohol quality
## Min. :0.9901 Min. :2.740 Min. :0.3300 Min. : 8.40 3: 10
## 1st Qu.:0.9956 1st Qu.:3.210 1st Qu.:0.5500 1st Qu.: 9.50 4: 53
## Median :0.9968 Median :3.310 Median :0.6200 Median :10.20 5:
## Mean :0.9967 Mean :3.311 Mean :0.6581 Mean :10.42 6:
## 3rd Qu.:0.9978 3rd Qu.:3.400 3rd Qu.:0.7300 3rd Qu.:11.10 7:
## Max. :1.0037 Max. :4.010 Max. :2.0000 Max. :14.90 8: 18
```
A statistical breakdown of the factors in the red wine.

## Univariate Plots Section

Here we start the individual histograms for each variable in the wines data set. The order of the plots will be the
same order as the variables appear in the dataset.

### Insert Image Here

## Univariate Analysis

** What is the structure of your dataset?**

There are 1599 different red wines in the set. The dataset contains 12 variables - fixed acidity, volatile acidity, citric
acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dixoide, density, pH, sulphates, alcohol and quality.

**What is/are the main feature(s) of interest in your dataset?**

I think this dataset steers the observer towards wine quality. Trying to find the main variable in the wine itself that
leads to a more sensory experience which results in a higher quality.

**What other features in the dataset do you think will help support your investigation into your feature(s) of
interest?**

I do not think one specific feature outweighs another at this point in the analysis. Bivariate analysis will help to
narrow down the impact on the quality of the red wine.

**Did you create any new variables from existing variables in the dataset?**

No new variables were created.

**Of the features you investigated, were there any unusual distributions?**

Fixed Acidity and Quality. I used log10 to scale fixed acidity’s distribution to a more normal shape. Quality was
unusual in that most of the wines fell between 3 through 8 so there are not any great wines or terrible wines in our
dataset.

**Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did
you do this?**

No.

## Bivariate Plots Section

In the Bivariate section, we’ll be comparing the overall wine quality vs the other factors in the dataset. Example:
Quality vs pH. Hopefully this will help us to determine a factor’s influence on the quality of the wine.


Fixed acidity seems to be comparable in amount in all qualities of wine.

### Insert Image Here

Volatile acidity seems to affect lower quality wines more. If it has less of this certain type of acidity, the quality
rises.

### Insert Image Here

The more citric acid in a red wine the higher quality wines. This is a pretty telling factor in regards to wine quality.

### Insert Image Here

Sugars don’t play a big part in quality. Seems the same amount of sugar is used in all qualities of red wine. I bet
this is different in white wines.

### Insert Image Here

Chlorides have little to no impact on quality of red wines.

### Insert Image Here

Sulfur dioxide (SO2) is fairly even across all qualities of our wines.

### Insert Image Here

Not much impact from total sulfur dioxide on quality.

### Insert Image Here

This one is interesting. Lower quality wines have more density and higher have lower density. An inverse effect.

### Insert Image Here

Another inverse comparison - as pH goes down, quality goes up.

### Insert Image Here

As quality goes up, sulphates goes up.

### Insert Image Here

Similar to sulphates, in that as alcohol content rises, so does the quality of the wine.

Although we compared all of the variables to quality, a correlation matrix might reveal other factors that are worth
comparing.

### Insert Image Here

Here are the others:

citric acid vs fixed acidity, citric acid vs volatile acidity, citric acid vs pH, density vs alcohol, density vs fixed acidity,
fixed acidity vs pH, total sulfur dioxide vs free sulfur dioxide

## Bivariate Analysis


### Insert Image Here


## Correlations

```
## [1] 0.6717034
```
Correlation - citric acid and fixed acidity

```
## [1] -0.5524957
```
Correlation - citric acid and volatile acidity

```
## [1] 0.2349373
```
Correlation - volatile acidity and pH

```
## [1] -0.5419041
```
Correlation - citric acid and pH

```
## [1] -0.4961798
```
Correlation - density and alcohol


```
## [1] 0.6680473
```
Correlation - density and fixed acidity

```
## [1] -0.6829782
```
Correlation - fixed acidity and pH

```
## [1] 0.6676665
```
Correlation - sulfur dioxide and free sulfur dioxide

## Correlation Results

Overall the correlations don’t seem out of the ordinary. For example, the correlation between volatile acidity and
citric acid should have a negative correlation. This is because volatile acidity is measured from the vinegar
portions of wine than the citric portions. They should counteract each other.

**Talk about some of the relationships you observed in this part of the investigation. How did the feature(s)
of interest vary with other features in the dataset?**

Quality being the feature of interest did show some positive correlations with alcohol levels especially but also with
citric acid and sulphates. Negative correlations stemmed from other factors such as volatile acidity, density, pH and
chlorides.

**Did you observe any interesting relationships between the other features (not the main feature(s) of
interest)?**

The pH levels of the wine were often lowered due to the rising acidity of the wine. so if citric acidity levels rise, pH
will fall. Also if fixed acidity rises, pH will fall. It makes sense from a chemical stance. In order to get pH to rise,
we’d have to introduce the opposite of citric acidity, volatile acidity. pH and volatile acidity have a positive
correlation.

Density and fixed acidity have a strong positive correlation. I believe this is because the more acidity that is
introduced to wine from other liquids, the less alcohol can exist. Less alcohol creates a more dense wine.

**What was the strongest relationship you found?**

Volatile acidity and quality has the strongest relationship, though it is a negative one.

## Multivariate Plots Section

In this section, I will be looking at two features that help wine reach it’s best quality ratings.


High quality wines contain low volatile acidity and low pH levels.

### Insert Image Here

High quality wines contain a high citric acid level and high alcohol content.

### Insert Image Here

High quality wines have a low residual sugars amount and a low volatile acidity level.

### Insert Image Here

High quality wines have a higher fixed acidity level and a lower density level.

### Insert Image Here

High quality wines have a low sulfur dioxide count and a high citric acid level.

### Insert Image Here

I believe what most of these comparisons are showing is that if there is more alcohol content and that wine content
is created from a large amount of citric acids (acid sucrose supplements), then the wine will be perceived as better.

## Multivariate Analysis

**Talk about some of the relationships you observed in this part of the investigation. Were there features
that strengthened each other in terms of looking at your feature(s) of interest?**

The features that strengthened each other were to have a low volatile acidity count and a high citric acid level
which led to a more alcoholic fruity wine.

**Were there any interesting or surprising interactions between features?**

Nothing too surprising. Quality comes down to citric acid levels being high which causes volatile acidity to be low.
This plus having a less dense wine that is more alcoholic will prove to be a quality wine.

**OPTIONAL: Did you create any models with your dataset? Discuss the strengths and limitations of your
model.**

No.

## Final Plots and Summary


### Plot One

I chose this quality histogram because the feature of quality stood out against the other more scientifically
measured variables. **Quality** became more of a result of the combination of features from the wine itself. In this
histogram, we can get a better breakdown of where each wine specifically falls into each quality rating. Most wines
are right in the middle of the quality scale at 5, while the top rated wines are very rare at 1.13%.

### Plot Two


I chose this plot because both factors had some of the highest positive and negative correlations with the quality of
the wine. **Volatile Acidity** is considered undesireable in red wines and it shows on this comparison against our
**Quality** factor. While it is not valued as much, some of it is still necessary for the overall flavor of wine. Remove it
altogether and I predict the quality of wine would decrease as well. On the counterpoint, **Citric Acid** is a sought
after ingredient in quality wines. The higher the alcohol from citric acid, the more desireable the wine. Although
wines of the past used citric acid from fruits direcly, modern day wines use fermented sucrose solutions to save
cost and still give the same effect to wine drinkers.

### Plot Three


**Alcohol** was also one of the largest factors in determining a high wine quality. This goes hand in hand with citric
acid in that the more alcohol from citric acid the higher the wine quality. In this plot we can determine that the
highest quality wines are also hold above average percentages of alcohol. Does this mean that if you purchase a
wine with higher alcoholic content it will be better? Probably, but make sure it’s sweeter too.

## Reflection

This exploration of data using R was my first time even using the R language. I found myself constantly comparing
it to analysing data using Python. I found lots to like though in R, from the easy way to load new packages, to the
overflowing amount of graphing types and customization. I can see why this still can be considered the language
of choice for analysis.

As for the dataset itself, I found it challenging in that I’m not much of a wine drinker. So to me, I had a hard time
relating to what would make a good wine. I learned a lot about the different factors and how they affect overall
quality from this dataset. I felt that this dataset was a bit skewed towards quality though as it was the only sensory
variable out of the set. The others were all based on their chemical influence on wine.

Things I would continue to find in this set, would be subsetting a lot of the data and remove outliers to clean up
some of the plots I made. Probably applying more statistical analysis as well. These plots look nice but sometimes
it’s good to have a nice table of data for study. I would find some xtable library examples out there on the ’net to
make even the tables look nice.
