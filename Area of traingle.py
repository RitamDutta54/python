#-------------------------------------------------------------------------------
# Name:        Area of traingle
# Purpose:
#
# Author:      Ritam
#
# Created:     14-03-2042
# Copyright:   (c) Admin 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Area of traingle
import math
s1=float(input(""))
s2=float(input(""))
s3=float(input(""))
s=(s1+s2+s3)/2
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("The area of triangle is",area)
