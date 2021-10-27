class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        FirstCity = [i for i,j in costs] #Flying everyone to one city
        Diff = [j - i for i,j in costs]  #Evaluating Differences when sent to another city
        # Now we choose the smallest differences and calculated the total after sending the half to another city
        return sum(FirstCity) + sum(sorted(Diff)[:len(costs)//2])
    
# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
