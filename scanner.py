keywords={"start","end","combine"}
extensions=('.jpg','.jpeg','.png')
# import parser
def scanner(text):
	text = text.split('\n')
	flag = 0
	markers = [-1,len(text)]
	for it,lin in enumerate(text):
		if lin == "start":
			flag = 1
			markers[0] = it
		elif lin == "end":
			flag = 2
			markers[1] = min(it,markers[1])
		if flag == 1:
			tokens = lin.split()
			for t in tokens:
				if t in keywords:
					continue
				elif t.isdigit():
					continue
				elif t.endswith(extensions):
					continue
				else:
					print ("Unrecognized character " + str(t) + " on line " + str(it))
					return 0,markers
	if flag == 0:
		return 0,markers
	return 1,markers

