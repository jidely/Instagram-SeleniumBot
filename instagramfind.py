followers = open("followers.txt","r")
following = open("following.txt","r")
right = open("rfollowing.txt","r+")
left = open("notfollowing.txt","w")

lines1 = followers.readlines()
lines2 = following.readlines()


for line1 in lines1:
	for line2 in lines2:
		if line2 in line1:
			right.write(line1)


for line2 in lines2:
	if line2 not in lines1:
		left.write(line2)
        

   

