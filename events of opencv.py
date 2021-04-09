# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:25:20 2020

@author: jadin
"""


import cv2
def main():
    events=[i for i in dir(cv2) if "EVENT" in i]
    print(events)
    
if __name__=="__main__":
    main()