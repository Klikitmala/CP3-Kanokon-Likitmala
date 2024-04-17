#How to solve a Velocity(v),Distance(s), Time(t) problem?
#Input a Distance, that are greater than 1 km
#and also input Time that are greater than 1hr.
#The terminal result should show 12km/h.
s = int(input("Distance (km) = ")) #Distance's unit is kilometer.
t = int(input("Time (h) = ")) #Time's unit is hour.
v = s/t 
print("Velocity =",int(v),"km/h")