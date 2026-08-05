
library(tidyverse)

read_lines_raw("2015/data/input_day8.txt") |>
  map_chr(rawToChar) -> input

sumTotal = 0 
sumEval = 0 

for (i in seq_along(input)) {
  sumTotal <- sumTotal + nchar(input[i])
  sumEval <- sumEval + nchar(eval(parse(text = input[i])))
}

print(sumTotal - sumEval)
