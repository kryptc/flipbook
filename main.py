from sys import argv
from scanner import scanner
from parser import parser

import imageio
import numpy as np


class FlipBook :
    """ Parent class which will contain all required helper functions and 
    store necessary variables to produce required flipbook """
    
    def __init__(self):
        self.frame_list = []
        self.blank = np.zeros([720,720,3],dtype=np.uint8)
        self.blank.fill(0)
        
    def generate_gif(self, frames):
        for frame in frames:
            #if len(frame) == 3 // standard appending
            startFrame = frame[0]
            endFrame = frame[1]
            imageName = frame[2]
            self.add_image_to_frame_list(startFrame, endFrame, imageName)

        imageio.mimsave('flipbook.gif', self.frame_list)
        print("GIF named flipbook.gif has been generated")
        
    
    def add_image_to_frame_list(self,startFrame, endFrame, imageName):
        """ add other params/functions to do resizing/positioning etc """       
        for i in range(startFrame-1, endFrame-1):
            try:
                image = imageio.imread(imageName)
            except:
                print (imageName, " not found.")
                # BufferedImage bi= new BufferedImage(320,240,BufferedImage.TYPE_BYTE_GRAY);
                image=self.blank
            self.frame_list.append(image)


    def parse_input(self, text):
        code, frames = parser(text)
        if code:
            self.generate_gif(frames)
        else:
            exit()

    def scan_input(self, text):
        if scanner(text):
            self.parse_input(text)
            # print ("yeehaw")
        else:
            exit()

def main(argv):
    if len(argv) != 2:
        print("Usage: python3 main.py <inputfile>")
        return

    #read input file contents
    ipfile = argv[1]
    file_obj = open(ipfile,"r")
    if file_obj.mode=="r":
        text = file_obj.read()
        # print (text)
        FB = FlipBook()
        FB.scan_input(text)



if __name__ == '__main__':
    main(argv)