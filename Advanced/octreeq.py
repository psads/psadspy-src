#
#  octTreeQuant.py
#
#  Created by Brad Miller on 2005-07-14.
#  Copyright (c) 2005 Luther College. All rights reserved.
#

import sys
import os
import Image
        
class OctTree:
    def __init__(self):
        self.root = None
        self.maxLevel = 5
        self.numLeaves = 0
        self.leafList = []
            
    def insert(self,r,g,b):        
        if not self.root:
            self.root = self.otNode(outer=self)
        self.root.insert(r,g,b,0,self)

    def find(self,r,g,b):
        if self.root:
            return self.root.find(r,g,b,0)
    
    def findMinCube(self):
        minCount = sys.maxsize
        maxLev = 0
        minCube = None
        for i in self.leafList:
            if i.count <= minCount and i.level >= maxLev:
                minCube = i
                minCount = i.count
                maxLev = i.level
        return minCube
        
    def reduce(self,maxCubes):
        while len(self.leafList) > maxCubes:
            smallest = self.findMinCube()
            print("Smallest cube is: ", smallest.count, smallest.red, smallest.green, smallest.blue)
            smallest.parent.merge()
            self.leafList.append(smallest.parent)
            self.numLeaves = self.numLeaves + 1

    class otNode:
        def __init__(self,parent=None,level=0,outer=None):
            self.red = 0
            self.green = 0
            self.blue = 0
            self.count = 0
            self.parent = parent
            self.level = level
            self.oTree = outer
            self.children = [None]*8

        
        def insert(self,r,g,b,level,outer):
            if level < self.oTree.maxLevel:
                idx = self.computeIndex(r,g,b,level)
                if self.children[idx] == None:
                    self.children[idx] = outer.otNode(parent=self,level=level+1,outer=outer)
                self.children[idx].insert(r,g,b,level+1,outer)
            else:
                if self.count == 0:
                    self.oTree.numLeaves = self.oTree.numLeaves + 1
                    self.oTree.leafList.append(self)
                self.red += r
                self.green += g
                self.blue += b
                self.count = self.count + 1

        def computeIndex(self,r,g,b,l):
            shift = 8 - l
            rc = r >> shift-2 & 0x4
            gc = g >> shift-1 & 0x2
            bc = b >> shift & 0x1
            return(rc | gc | bc)
        
        def find(self,r,g,b,level):
            if level < self.oTree.maxLevel:
                idx = self.computeIndex(r,g,b,level)
                if self.children[idx]:
                    return self.children[idx].find(r,g,b,level+1)
                elif self.count > 0:
                    return ((self.red/self.count, self.green/self.count, self.blue/self.count))
                else:
                    print("error: No leaf node to represent this color")
            else:
                return ((self.red/self.count, self.green/self.count, self.blue/self.count))

        def merge(self):
            for i in self.children:
                if i:
                    print("combining ", i.calcId(), i.count, i.red, i.green, i.blue)
                    if i.count > 0:
                        self.oTree.leafList.remove(i)
                        self.oTree.numLeaves = self.oTree.numLeaves - 1
                    else:
                        print("Recursively Merging non-leaf...")
                        i.merge()
                    self.count += i.count
                    self.red += i.red
                    self.green += i.green
                    self.blue += i.blue
            for i in range(8):
                self.children[i] = None

        def calcId(self):
            sId = ""
            if self.count > 0:
                for i in range(1,self.oTree.maxLevel+1):
                    sId = sId + str(self.computeIndex(self.red/self.count, self.green/self.count,self.blue/self.count,i))
            return sId



        
def buildAndDisplay():
#    im = Image.open('/Users/bmiller/Projects/PyExamples/Image/lcastle.jpg')
    im = Image.open('bubbles.jpg')
    w,h = im.size
    ot = OctTree()
    for row in range(0,h):
        for col in range(0,w):
            r,g,b = im.getpixel((col,row))
            ot.insert(r,g,b)
    print("Num Leaves before reduce = ", ot.numLeaves, len(ot.leafList))        
    ot.reduce(256)
    diffCount = 0
    for row in range(0,h):
        for col in range(0,w):
            r,g,b = im.getpixel((col,row))
            nr,ng,nb = ot.find(r,g,b)
            if nr != r or ng != g or nb != b:
                diffCount = diffCount + 1
            im.putpixel((col,row),(nr,ng,nb))
    print("Num Leaves After = ", ot.numLeaves, len(ot.leafList))                
    print("There were ", diffCount, " pixel differences")
    for i in ot.leafList:
        print(i.red/i.count, i.green/i.count, i.blue/i.count)
    im.show()
   
   
if __name__ == '__main__':
    buildAndDisplay()

