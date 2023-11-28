import re

var = "3123,2132.000"
test = int(re.sub('[^0-9,]', "", var).replace(",", ""))
print(test)