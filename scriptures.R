install.packages("scriptuRs")
library(scriptuRs)
library(tidyverse)



scriptures <- lds_scriptures()

scriptures |> 
  group_by(volume_title, book_title) |> 
  summarize(total_verses = n())

write.csv(scriptures, 'data.csv', row.names=F)
