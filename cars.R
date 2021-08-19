# Cars
library(readr)
# Importing the dataset
cars <- read_csv("C:\\Users\\WIN10\\Desktop\\LEARNING\\DS\\ProbCLT\\probability dataset\\Cars.csv")
mean(cars$MPG) 

# Probability Distribution
library(UsingR)
densityplot(cars$MPG)

# Normal Quantile-Quantile Plot
qqnorm(cars$MPG)
qqline(cars$MPG)
# Transformation to make variable normal
qqnorm(log(cars$MPG))
qqline(log(cars$MPG))
qqnorm(sqrt(cars$MPG))
qqline(sqrt(cars$MPG))
library(moments)

# Graphical Representation
barplot(cars$MPG)
dotchart(cars$MPG)
# Histogram
hist(cars$MPG) 
# Boxplot
boxplot(cars$MPG) 


