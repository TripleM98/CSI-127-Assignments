import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

def fruits(s, t, Position_Of_Tree, distance):
    
	Amount_Fruit = 0
	
	for fruit in distance:
            
		if (Position_Of_Tree + fruit >= s) and (Position_Of_Tree + fruit <= t):
                    
			Amount_Fruit += 1
			
	return Amount_Fruit

Apple_Value=fruits(s,t,a,apple)

print(Apple_Value)

Orange_Value=fruits(s,t,b,orange)

print(Orange_Value)