# This class will hold a xml representation
# Search for text in berner

import pandas as pd
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

from xml.etree import ElementTree
from xml.dom import minidom

from datetime import date

import ospath
import monitorwriter


objarray = []
lagerarray = []
numarray = []
datearray = []

#string = "Pos:"

#foundstart = False

alotstrings = ""

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

def searchincominggodsmarke(text):
    intarray = []

    for line in text:
        intarray.append(line)
        #print(line)
    
    for i in range(len(intarray)):
    #for obj in intarray:
         if "Godsmärke" in intarray[i]:
           #print("I FOUND godsmärke" + "at pos" + str(i))
           #print("We got date" + intarray[(i+1)])
           return(intarray[(i+1)])
        #     date = list(intarray[(i+1)])
        #     #print(date)
        #     #year = date[2:4]
        #     #print(year)
            
        #     yearstr = "".join(date[2:4])
        #     monthstr = "".join(date[5:7])
        #     daystr = "".join(date[8:10])

        #     #print("Heja" + yearstr + monthstr + daystr)
        #     #print(str(date[2:4]).join + str(date[5:7]).join + str(date[8:10]).join)

        #     return(yearstr + monthstr + daystr)
    #print("THIS IS A TEST" + text[0])



def searchincomingdate(text):
    intarray = []

    for line in text:
        intarray.append(line)
        #print(line)
    
    for i in range(len(intarray)):
    #for obj in intarray:
        if "Datum" in intarray[i]:
            #print("I FOUND A DATUM" + "at pos" + str(i))
            #print("We got date" + intarray[(i+1)])
            date = list(intarray[(i+1)])
            #print(date)
            #year = date[2:4]
            #print(year)
            
            yearstr = "".join(date[2:4])
            monthstr = "".join(date[5:7])
            daystr = "".join(date[8:10])

            #print("Heja" + yearstr + monthstr + daystr)
            #print(str(date[2:4]).join + str(date[5:7]).join + str(date[8:10]).join)

            return(yearstr + monthstr + daystr)
    #print("THIS IS A TEST" + text[0])


def searchdate(today):
    #print(alotstrings)
    #today = date.today()
    var = 0
    for lines in alotstrings:
        #print(lines)
        if "CR" in lines:
            lista = list(lines)
            if(lista[2].isdecimal()):
                #print(str(var) + lines + "\t" + str(lines[2:]))
                datearray.append(str(lines[2:]))
                lagerarray.append(lines)
                var = var + 1

        if "CL" in lines:
            #print(str(var) + lines + today)
            lagerarray.append(lines)
            datearray.append(today)
            var = var + 1

        if "CH" in lines:
            lista = list(lines)
            if(lista[2].isdecimal()):
                #print(str(var) + lines + "\t" + str(lines[2:]))
                datearray.append(str(lines[2:]))
                lagerarray.append(lines)
                
                var = var + 1
    




def run():
  global alotstrings
  
  intpath = ospath.ospath()
  outputline = ""
  string2 = "E "

  search = open(intpath.getPath() + 'temp.txt') 
  godsmarke = searchincominggodsmarke(search)
  #print(godsmarke)

  search = open(intpath.getPath() + 'temp.txt') 
  today = searchincomingdate(search)
  
  search = open(intpath.getPath() + 'temp.txt')
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

  tracker.addLeverantorskod("1670454")
  tracker.addKundOrdernr("X")
  tracker.addKundkod("1670454")
  tracker.addGodsmarkning(godsmarke)

  
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
              #tracker.addObjectBasic(lines, numbers[0])
              objarray.append(lines)
              numarray.append(numbers[0])


              #print(numbers[0])

  #tracker.printout()
  
  #print(today)
  searchdate(today)

#   count = 0
#   for obj in objarray:
#     print(str(count) + obj)
#     count = count + 1
  print(str(len(objarray)) + "::" + str(len(lagerarray)))
  if(len(objarray) == len(lagerarray)):
    for i in range(len(objarray)):
        tracker.addObjectFull(objarray[i], numarray[i], datearray[i])
        #print(objarray[i] + "\t"  + datearray[i])

  tracker.save(intpath.getPath() + "OrderOut.txt")
