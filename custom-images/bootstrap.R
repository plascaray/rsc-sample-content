# use binary packages
local({r <- getOption("repos")
       r["CRAN"] <- "https://packagemanager.rstudio.com/cran/__linux__/bionic/2022-08-31" 
       options(repos=r)
})

install.packages(c("renv", "rmarkdown", "shiny", "dplyr", "plumber", "odbc"))
