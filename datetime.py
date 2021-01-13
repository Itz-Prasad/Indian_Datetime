
# Program for getting local datetime in India

#Importing packages
from datetime import datetime
import pytz

# Setting Indian time zone
IST = pytz.timezone('Asia/Kolkata')

#Getting Indian time
Date_India = datetime.now(IST)

# Specifying format (Format : %Y:%m:%d %H:%M:%S %Z %z )
format = "%d/%m/%Y %H:%M"

# Printing time
print(Date_India.strftime(format))
