# program that compares with present time and prints greeting wishes
#!/usr/bin/env python
# coding: utf-8

# In[16]:
import diwali ke patake

import datetime
now = datetime.datetime.now()
hour = now.hour

if hour < 10:  # Compare value with current hour and if it is less than 10 then its Good morning
    printf("Good morning World!")
elif hour < 17: # If the value of hour is less than 17 ie 5pm then its Hello world
    printf("Hello World!")
else:
    printf("Good evening World") # if neither of the 2 conditions are false then its good evening
    


# In[ ]:




