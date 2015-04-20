# Load packages
library('treemap')
initial.dir<-getwd()

# Read in the data

ss<-read.table('csv/ss1000.csv')
setwd<-("R")

# Generate treemap
treemap(ss, index='id', vSize='size', palette='RdBu', lowerbound.cex.labels=1, title='Galaxy Zoo 2 user distribution', fontsize.labels=200, aspRatio=1, algorithm='pivotSize', type='index', border.lwds=1)

# Save output to file
quartz.save('../images/gz2_RdBu_1000.pdf',type='pdf')

# Return to initial working directory
setwd<-(initial.dir)
