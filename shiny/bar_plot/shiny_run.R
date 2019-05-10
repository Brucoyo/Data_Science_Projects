library(ggplot2)
library(dplyr)
library(tidyr)

#http://rtricks4kids.ok.ubc.ca/wjbraun/DS550/air.csv
# raw data download from here, which is around 800 MB.
rawdata<-read.csv("air.csv")

data<-select(rawdata,-c(DepTime,CRSDepTime,ArrTime,CRSArrTime,FlightNum,ActualElapsedTime,CRSElapsedTime,AirTime,TaxiIn,TaxiOut,Cancelled,CancellationCode,Diverted))

head(data)
summary(data)

data$WeekDay <- data$DayOfWeek


# Define numbers by actual days and months.
data$WeekDay[data$WeekDay == 1] <- 'Monday'
data$WeekDay[data$WeekDay == 2] <- 'Tuesday'
data$WeekDay[data$WeekDay == 3] <- 'Wednesday'
data$WeekDay[data$WeekDay == 4] <- 'Thursday'
data$WeekDay[data$WeekDay == 5] <- 'Friday'
data$WeekDay[data$WeekDay == 6] <- 'Saturday'
data$WeekDay[data$WeekDay == 7] <- 'Sunday'

data$WeekDay <- factor(data$WeekDay,levels = c("Monday", "Tuesday", "Wednesday", 'Thursday','Friday','Saturday','Sunday'))

data$Month[data$Month == 1] <- 'January'
data$Month[data$Month == 2] <- 'February'
data$Month[data$Month == 3] <- 'March'
data$Month[data$Month == 4] <- 'April'
data$Month[data$Month == 5] <- 'May'
data$Month[data$Month == 6] <- 'June'
data$Month[data$Month == 7] <-'July'
data$Month[data$Month == 8] <- 'August'
data$Month[data$Month == 9] <- 'September'
data$Month[data$Month == 10] <- 'October'
data$Month[data$Month == 11] <- 'November'
data$Month[data$Month == 12] <- 'December'

data$Month <- factor(data$Month,levels = c("January", "February", "March", 'April','May','June','July','August','September','October','November','December'))

data$DelayReason[data$CarrierDelay>0]='CarrierDelay'
data$DelayReason[data$WeatherDelay>data$CarrierDelay]='WeatherDelay'
data$DelayReason[data$NASDelay>data$WeatherDelay]='NASDelay'
data$DelayReason[data$SecurityDelay>data$NASDelay]='SecurityDelay'
data$DelayReason[data$LateAircraftDelay>data$SecurityDelay]='LateAircraftDelay'

data$DelayReason
head(data)


newdata<-select(data,-c(X,DayofMonth,DayOfWeek,TailNum,DepDelay,Distance,CarrierDelay,WeatherDelay,NASDelay,SecurityDelay,LateAircraftDelay,Dest,Origin))
head(newdata)
write.csv(newdata,file="newdata.csv")

ggplot(newdata,aes(UniqueCarrier,fill=DelayReason)) + geom_bar()
ggplot(newdata,aes(Month,fill=DelayReason)) + geom_bar()
ggplot(newdata,aes(WeekDay,fill=DelayReason)) + geom_bar()

getwd()
##shiny
library(shiny)
runApp("shiny/")
