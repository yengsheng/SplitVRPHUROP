library(dplyr)
library(ggplot2)
library(caTools)
library(corrgram)


setwd("C:\\Users\\Yong Sheng\\Desktop\\UROP\\SplitVRPHUROP\\Normalized Data")
df <- read.csv("dataset_2.csv")

sampleSplit <- sample.split(Y=df$highest_split_distance_10x, SplitRatio=0.7)
trainSet <- subset(x=df, sampleSplit==TRUE)
testSet <- subset(x=df, sampleSplit==FALSE)

model <- lm(highest_split_distance_10x~ 0+lowest_demand +	original_objective + number_of_nodes, data=trainSet)
summary(model)


preds <- predict(model, testSet)

modelEval <- cbind(testSet$highest_split_distance_10x, preds)
colnames(modelEval) <- c('Actual', 'Predicted')
modelEval <- as.data.frame(modelEval)

mean((modelEval$Actual - modelEval$Predicted)^2)^(1/2)



model <- lm(highest_split_distance_10x ~ 0 + highest_demand +	lowest_demand +	original_objective + number_of_nodes, data=trainSet)
summary(model)


preds <- predict(model, testSet)

modelEval <- cbind(testSet$highest_split_distance_10x, preds)
colnames(modelEval) <- c('Actual', 'Predicted')
modelEval <- as.data.frame(modelEval)

mean((modelEval$Actual - modelEval$Predicted)^2)^(1/2)



model <- lm(highest_split_distance_10x ~ 0 + highest_demand +	lowest_demand +	original_objective, data=trainSet)
summary(model)


preds <- predict(model, testSet)

modelEval <- cbind(testSet$highest_split_distance_10x, preds)
colnames(modelEval) <- c('Actual', 'Predicted')
modelEval <- as.data.frame(modelEval)

mean((modelEval$Actual - modelEval$Predicted)^2)^(1/2)