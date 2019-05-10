library(shiny)
library(ggplot2)
newdata<-read.csv("/Users/brucepei/Data_Science_Projects/shiny/bar_plot/newdata.csv")
shinyServer(function(input, output) {
  output$monthPlot <- renderPlot({
    
    newdata$Month <- factor(newdata$Month,levels = c("January", "February", "March", 'April','May','June','July','August','September','October','November','December'))
    cutoff<-input$cutoff
    ggplot(data=subset(newdata, ArrDelay>=cutoff),aes(Month,fill=DelayReason)) + geom_bar()
    })
  output$weekPlot <- renderPlot({
    
    newdata$WeekDay <- factor(newdata$WeekDay,levels = c("Monday", "Tuesday", "Wednesday", 'Thursday','Friday','Saturday','Sunday'))
    cutoff<-input$cutoff
    ggplot(data=subset(newdata, ArrDelay>=cutoff),aes(WeekDay,fill=DelayReason)) + geom_bar()
  })
  output$carrierPlot <- renderPlot({
    cutoff<-input$cutoff
    ggplot(data=subset(newdata, ArrDelay>=cutoff),aes(UniqueCarrier,fill=DelayReason)) + geom_bar()
  })
  output$summary <- renderPrint({
    cutoff<-input$cutoff
    summary(subset(newdata, ArrDelay>=cutoff))
    
  })
})
