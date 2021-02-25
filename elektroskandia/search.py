# This class will hold a xml representation
# Search for text in berner

import pandas as pd
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

from xml.etree import ElementTree
from xml.dom import minidom

#import xmlwriter
import monitorwriter

#string = "Pos:"

#foundstart = False

#char = '.,/?-abcedefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ'

#output = open('output.txt', "w")



# def printout():
#   lines = outputline.split("\n")
#   non_empty_lines = [line for line in lines if line.strip() != ""]
#   string_without_empty_lines = ""
#   for line in non_empty_lines:
#       string_without_empty_lines += line + "\n"
#   #print("Compressed form:")
#   #print(string_without_empty_lines)
#   splitstring = string_without_empty_lines.splitlines()   
#   #print(splitstring[0])   #This is the header
#   #print(splitstring[0].split(' '))

#   #realdata = splitstring[1].split(' ')

#   #print("Output")
#   #tracked = xmlwriter.xmlwriter()
#   #for str in splitstring[1:]:
#     #print(str)
#  #   str = str.split(' ')
#  #   tracked.addObject(str[1], str[len(str)-6])

#   #tracked.printout()
#   #tracked.save("result.xml")
  
#   exit()

def run():
  outputline = ""
  string2 = "E "
  search = open('C:/temp/temp.txt') 
  for line in search:
    #re.sub(r'[^' + char +']', '?', line)
  #   print(line)
  #   if(foundstart == True):
  #     charc = line[0]
  #     if string2 in line:
  #       #print("Found exit")
  #       #output.close()
  #       #print(outputline)
  #       printout()

  #     if(charc != '-'):
  #       #print(line)
  #       outputline = outputline + line
  #       #output.write(line)

  #   elif string in line:
  #     foundstart = True
  #     #print("Found trigger")
  #     #print(line)
  #     outputline = outputline + line
  #     #output.write(line)
  #     #found first trigger
      outputline = outputline + line

  lines = outputline.split("\n")
  non_empty_lines = [line for line in lines if line.strip() != ""]
  string_without_empty_lines = ""
  for line in non_empty_lines:
      string_without_empty_lines += line + "\n"


  alotstrings = string_without_empty_lines.split("\n")

  #print(alotstrings)
  #print(string_without_empty_lines)
  number = 0
  #tracker = xmlwriter.xmlwriter()
  tracker = monitorwriter.monitorwriter()

  for lines in alotstrings:
      number = number +1
      if string2 in lines:
          lista = list(lines)
          if (lista[0] == 'E' and lista[1] == ' '):
              #print(lines)
              #print("number" + str(number))
  #            print("Howmany\n" + alotstrings[number-2])
              #print("Howmany")
              numbers = alotstrings[number-2].split(' ')
              tracker.addObject(lines, numbers[0])
              #print(numbers[0])

  #tracker.printout()

  tracker.save("C:/temp/OrderOut.txt")
