# TMDB Analysis

## Introduction

I have chosen to use the TMDb data set to answer a series of questions pertaining to the movie industry. This data originated from <a href="https://www.kaggle.com/juzershakir/tmdb-movies-dataset">Kaggle</a> but has since been cleaned by Udacity. This data set contains information about 10,000 movies collected from The Movie Database (TMDb).

Questions that I will attempt to answer in this analysis:

1. Which movies had the highest and which had the lowest profits?
2. Who are the directors that are producing the most profits in the movie industry?
3. Which actors appeared in the most movies?
4. Which movies had the longest runtimes and which had the shortest runtimes?
5. Average runtimes and the impact on movie profits

## Conclusions

Overall, this was an interesting data set to analyze. We only answered 5 questions, but it has the potential for much more using keywords, date ranges, or even popularity scores.

Avatar in the top spot for total profits seems like a tough movie to beat. But if anyone could do it, it would probably be Steven Spielberg who seems to really bring in the money for the studios. He's untouchable in profitability even compared to second place, Peter Jackson.

We also concluded that movies with a runtime over 120 minutes will earn an average of \$121,211,114 MORE in profits than those below the 120 minute mark. The movie industry's best bet would be to make their movies at least 120 minutes to maximize their profits.

By banking on a great director or a movie with a runtime above 120 minutes, the next movie made could potentially reach the average profitability of $477,706,188. And chances are good, the next movie you watch, whether in the theater or at home might contain Robert De Niro in either a lead or supporting role.

**Limitations:** While we started with over 10000 unique movies, for the sake of this analysis we cut out a substantial amount during our data wrangling portion. We eliminated those movies with a budget of zero and used only those with total profits above \$200,000,000. While that budget data isn't factually accurate, our decision of dropping all of those movies had an impact on our final analysis. If we were to say, fill those zeroes with the mean or next closest value, we could be coming to some different conclusions today. Likewise, if we reduced our total profits to include all ranges of profits, our data would tell a slightly different story.

