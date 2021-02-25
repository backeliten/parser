# This class will hold a xml representation
# Search for text in berner

import pandas as pd
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

from xml.etree import ElementTree
from xml.dom import minidom

import ospath

def printout():
  lines = outputline.split("\n")
  non_empty_lines = [line for line in lines if line.strip() != ""]
  string_without_empty_lines = ""
  for line in non_empty_lines:
      string_without_empty_lines += line + "\n"
  #print("Compressed form:")
  #print(string_without_empty_lines)
  splitstring = string_without_empty_lines.splitlines()   
  #print(splitstring[0])   #This is the header
  #print(splitstring[0].split(' '))

  #realdata = splitstring[1].split(' ')

  print(splitstring)
  #tracked = xmlwriter.xmlwriter()
  #for str in splitstring[1:]:
    #print(str)
  #  str = str.split(' ')
  #  tracked.addObject(str[1], str[len(str)-6])

  #tracked.printout()
  #tracked.save("result.xml")
  
  exit()

def run():
  intpath = ospath.ospath()
  string = "Pos:"
  string2 = "Order"
  foundstart = False
  outputline = ""
  search = open(intpath.getPath()+'temp.txt')
  for line in search:
    #re.sub(r'[^' + char +']', '?', line)
  #  print(line)
    if(foundstart == True):
      charc = line[0]
      if string2 in line:
        #print("Found exit")
        #output.close()
        #print(outputline)
        printout()

      if(charc != '-'):
        #print(line)
        outputline = outputline + line
        #output.write(line)

    elif string in line:
      foundstart = True
      #print("Found trigger")
      #print(line)
      outputline = outputline + line
      #output.write(line)
      #found first trigger

