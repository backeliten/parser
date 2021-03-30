#!/usr/bin/python3

import monitorwriter
import readpdf
import elektroskandia.search
import berner.search
import monitorERP.parser

listofobjects = monitorwriter.monitorwriter()

readpdf.pdf_to_text("0203618.pdf")
elektroskandia.search.run()     #Do the actually parsing will read file in background

#elektroskandia.search.searchdate()


# #Add defaults
# listofobjects.addLeverantorskod("1670454")
# listofobjects.addKundOrdernr("X")
# listofobjects.addKundkod("1670454")
# listofobjects.addGodsmarkning("PERU")

# #Add objects
# listofobjects.addObjectBasic("1234", "23")
# listofobjects.addObjectBasic("4321", "56")

# listofobjects.addObjectFull("4321", "56", "210220")

# listofobjects.printout()