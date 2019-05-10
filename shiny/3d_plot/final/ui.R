library(shiny)
library(rgl)

shinyUI(fluidPage(
  # App title ----
  titlePanel("House Price Analysis - Xiangyu Pei (Bruce) Jan 29th 2019 "),
  # Sidebar layout with input and output definitions ----

   mainPanel(
   # 1. add the house price of histogram and the mean
     	plotOutput(outputId = "Histplot"),
   # 2. add summary of house price
   		titlePanel("#1 Summary of the House Price "),
   		verbatimTextOutput("summary"),
   	# 3. then divide the data price into 4 groups base on the summary data
   		titlePanel("#2 Divide the Home Price into 4 groups base on Summary and identify the relationship between Home price and age of the home, number of bedrooms, tax and living space"),
   		rglwidgetOutput("mywebgl1"),
   		titlePanel("x is house sale price"),
   		titlePanel("y is number of bedrooms"),
   		titlePanel("z is age of the home (in years)"),
   		plotOutput(outputId = "regression1"),
		
		titlePanel(""),
		titlePanel(""),
		titlePanel(""),
		titlePanel(""),
   		rglwidgetOutput("mywebgl2"),
   		titlePanel("x is house sale price"),
   		titlePanel("y is taxes (in thousands of dollars)"),
   		titlePanel("z is living space (in thousands of square feet)"),
   		plotOutput(outputId = "regression2"),
   		plotOutput(outputId = "regression3"),
   		titlePanel("Summary:"),
   		titlePanel("More Expensive the home, Lower age of the home (newer)"),
   		titlePanel("No clear relationships between Home price and bedrooms"),
   		titlePanel("More Expensive the home, More tax"),
		titlePanel("More Expensive the home, More living space")


   		
   		
   		
     
     
    )
  )
)
