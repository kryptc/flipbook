keywords={"start","end","combine"}
extensions=('.jpg','.jpeg','.png')
# import parser
def scanner(text):
	text = text.split('\n')
	for it,lin in enumerate(text):
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
				return 0
	return 1

