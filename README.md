# flipbook
Design a language for describing flipbooks and implement a compiler for this language that can convert a flipbook description into a print able pdf (or a video).

### To Run
1. `pip install -r requirements.txt`
2. `python3 main.py test.flip`

### What's added as of now:
- Given a code of the format:

`start`

`<num1> <num2> <image1>`

`<num3> <num4> <image2>`

`.....`

`end`

where start and end are the keywords pointing to the executable portion of the code, num1 and num2 are the starting and ending frame (num1 <= num2) and image is the path to an image (.png, .jpg, .jpeg), saved in a file with a `.flip` extension
- The compiler scans and parses the code and if it is valid, creates a gif out of the given frames. If any frames are empty, a blank black image is set as placeholder.

### To be added
- Image resize (need to restructure with opencv)
- `combine` keyword to take multiple images as input and display them according the user-given matrix (ref. matplotlib plots)
- More error checking
