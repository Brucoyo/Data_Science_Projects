library(shiny)
shinyUI(fluidPage(
  # App title ----
  titlePanel("Flight Delay Times of Different Delay Duration by Unique Carriers, Months and Weeks."),
  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    # Sidebar panel for inputs ----
    sidebarPanel(
      sliderInput(inputId = "cutoff",
                  label = "delay duration",
                 min = 1,
                  max = 700,
                  value = 30)
   ),
    mainPanel(
      plotOutput(outputId = "monthPlot"),
      plotOutput(outputId = "weekPlot"),
      plotOutput(outputId = "carrierPlot"),
      verbatimTextOutput("summary")
    )
  ))
)
  