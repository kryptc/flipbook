extensions=('.jpg','.jpeg','.png')

def parser(text):
	text = text.split('\n')
	if text[0] != "start":
		print ("Syntax error: Code must start with keyword 'start'")
		return [0,0]
	elif text[-1] != "end":
		print ("Syntax error: Code must end with keyword 'end'")
		return [0,0]
	frame_img=[]
	for it,lin in enumerate(text[1:-1]):
		tokens = lin.split()
		#standard command
		if len(tokens) == 3:
			if tokens[0].isdigit() and tokens[1].isdigit() and tokens[2].endswith(extensions):
				if int(tokens[0]) > int(tokens[1]):
					print ("Syntax error on line " + str(it) + ": starting frame should be lesser than or equal to ending frame.")
					return [0,0]
				frame_img.append([int(tokens[0]),int(tokens[1]),tokens[2]])
				continue
			else:
				print ("Syntax error on line " + str(it))
				return [0,0]
		else:
			print ("Syntax error on line " + str(it) + ": too many or too few arguments in a single line")
			return [0,0]
	return [1, frame_img]
