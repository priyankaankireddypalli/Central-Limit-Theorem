# wc
library(readr)
# Importing the dataset
wc <- read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\ProbCLT\\probability dataset\\wc-at.csv")
mean(wc$Waist) 
mean(wc$AT)

# Probability Distribution
library(UsingR)
densityplot(wc$Waist)
densityplot(wc$AT)

# Normal Quantile-Quantile Plot
qqnorm(wc$Waist)
qqline(wc$Waist)
qqnorm(wc$AT)
qqline(wc$AT)

library(moments)
# Graphical Representation
barplot(wc$Waist)
dotchart(wc$Waist)
barplot(wc$AT)
dotchart(wc$AT)
# Histogram
hist(wc$Waist) 
hist(wc$AT) 
# Boxplot
boxplot(wc$Waist) 
boxplot(wc$AT) 


