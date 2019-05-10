library(shiny)
library(ggplot2)
library(MPV)
library(rgl)

	data<-table.b4	
  	data$pricla[data$y<1000]='cla4'
  	data$pricla[data$y<=29.9]='cla1'
  	data$pricla[data$y<=33.7&data$y>29.9]='cla2'
  	data$pricla[data$y<=38.15&data$y>33.7]='cla3'
  	
  	
options(rgl.useNULL = TRUE)
shinyServer(function(input, output, session) {


  output$Histplot <- renderPlot({
    sp <-ggplot(data=data, aes(data$y)) + 
  geom_histogram(breaks=seq(20, 50, by = 2), 
                 col="red", 
                 fill="green", 
                 alpha = .2) + 
  labs(title="Histogram for House Price") +
  labs(x="House price", y="Count") + 
  xlim(c(18,52)) + 
  ylim(c(0,6))
sp + geom_vline(xintercept = mean(data$y), linetype="dotted", color = "blue", size = 1.5)
  })
  
  
  
  output$summary <- renderPrint({
    colnames(data)[1] <- "price"
    summary(data$price)
  })
  
  
  output$mywebgl1 <- renderRglwidget({  	
  	open3d() 
	#clear3d() # remove earlier picture
	bg3d("gray") # colour the background gray
cla1 <- with(subset(data, pricla == "cla1"), 
               spheres3d(y, x7, x8, 
                         col="red",
                         radius = 1.5))
cla2 <- with(subset(data, pricla == "cla2"), 
                   spheres3d(y, x7, x8, 
                             col="yellow",
                             radius = 1.5))
cla3 <- with(subset(data, pricla == "cla3"), 
                  spheres3d(y, x7, x8, 
                            col="blue",
                            radius = 1.5))
cla4 <- with(subset(data, pricla == "cla4"), 
             spheres3d(y, x7, x8, 
                       col="black",
                       radius = 1.5))
aspect3d(1,1,1)
axesid <- decorate3d()

scene1 <- scene3d()
rgl.close()
	save <- options(rgl.inShiny = TRUE)
  	on.exit(options(save))
rglwidget(scene1)  	
  })  
  
  output$regression1 <- renderPlot({
  	plot(data$y ~ data$x8, data = data, main = "More Expensive the home, Lower age of the home (newer)",xlab="age of the home (in years)", ylab="sale price of the house (in thousands of dollars)",
     col="grey")
reg <- lm(data$y ~ data$x8, data = data)
abline(reg, col='blue')
      })

  output$mywebgl2 <- renderRglwidget({  	
  	open3d() 
	#clear3d() # remove earlier picture
	bg3d("gray") # colour the background gray
cla1 <- with(subset(data, pricla == "cla1"), 
               spheres3d(y, x1, x4, 
                         col="red",
                         radius = .5))
cla2 <- with(subset(data, pricla == "cla2"), 
                   spheres3d(y, x1, x4, 
                             col="yellow",
                             radius = .5))
cla3 <- with(subset(data, pricla == "cla3"), 
                  spheres3d(y, x1, x4, 
                            col="blue",
                            radius = .5))
cla4 <- with(subset(data, pricla == "cla4"), 
             spheres3d(y, x1, x4, 
                       col="black",
                       radius = .5))
aspect3d(1,1,1)
axesid <- decorate3d()
scene2 <- scene3d()
rgl.close()
	save <- options(rgl.inShiny = TRUE)
  	on.exit(options(save))
rglwidget(scene2)  	
  })  


 	output$regression2 <- renderPlot({
  	plot(data$y ~ data$x1, data = data, main = "More Expensive the home, More tax",xlab="taxes (in thousands of dollars)", ylab="sale price of the house (in thousands of dollars)",
     col="grey")
reg <- lm(data$y ~ data$x1, data = data)
abline(reg, col='red')
      })

 	output$regression3 <- renderPlot({
  	plot(data$y ~ data$x4, data = data, main = "More Expensive the home, More tax",xlab="living space (in thousands of square feet)", ylab="sale price of the house (in thousands of dollars)",
     col="grey")
reg <- lm(data$y ~ data$x4, data = data)
abline(reg, col='blue')
      })
	
  

  
})