
# HVD1	30007_KNR	J9879	1	J9879		J9879		ABB
# HVD2	Plåtmodeller AB	Industrivägen 1	Hus 1	SE-123 45 Lillstaden		Sverige
# HVD3	ABB
# RAD1	1	1	1	OB7		11.00	110406	14.00	0	ob7	ST
# RAD1	1	4	1			1.00	110406	0	0	ob7 s  Texrade tetetetetetetettetetetetet	
# RAD1	2	1	1	OCT30049		12.00	110406	15.00	1.00	RULLBORD  GRYCKSBO2 BORD1 *3-0049*&	ST
# RAD1	2	4	1			1.00	110406	0	0	OCT TExtRaden  tstststststssssssssssssssssssssssssssssssss12	
# END1

# 1	1	HVD1	RecId
# 2	2		Kundkod                         x
# 4	3	 	Kundens Ordernr                 x
# 5	4	 	Kundens referens
# 8	5	 	Övr. upplysningar
# 9	6		Kod för leveransvillkor
# 10	7		Godsmärke rad1 1
# 11	8		Godsmärke rad1 2
# 12	9	 	Leverantörskod i Monitor
			
# 9	1	HVD2	RecId
# 10	2	 	Adress rad 1
# 11	3	 	Adress rad 2
# 14	2		Adress rad 3
# 16	2	 	Adress rad 4
# 17	1	 	Adress rad 5
# 18	2	 	Adress rad 6
# 20	1	HVD3	RecId
# 21	2	 	Kundkod faktura
# 23	1	RAD1	RecId
# 24	2	 	Radnummer  (köparens)
# 25	3	 	Radtyp
# 26	1	 	Kundens ordernr / radnivå
# 27	2	 	Kundens artikelNR
# 28	3	 	Artikel revision
# 29	1	 	Antal artiklar 
# 30	2	 	Leveransperiod
# 31	1	 	Pris
# 32	2	 	Rabatt
# 33	2		Text / Benämning
# 34	2		enhet 
# 33	1	END1	RecId


# Att få med

# Godsmärkning
# Inkommande datum
# Leveranstyp

# HVD1	1670454	X	 Gods 1					1670454
# RAD1	1	1		E3864692		2	210128
# RAD1	2	1		E2112055		5	210128
# END1

#date i formen år:mm:dd


class monitorwriter:
    
    kundkod = ""
    kundensOrdernr = ""
    godsmarkning = ""

    def __init__(self):
        self.dataarray = []

        self.kundkod = ""
        self.leverantorskod = "Empty"
        self.kundensOrdernr = ""
        self.godsmarkning = ""
        self.enhet = "st"

        self.header = ""
        self.objects = ""


    def addKundkod(self, name):
        self.kundkod = name

    def addKundOrdernr(self, name):
        self.kundensOrdernr = name

    def addLeverantorskod(self, name):
        self.leverantorskod = name

    def addGodsmarkning(self,name):
        self.godsmarkning = name


    def addObjectBasic(self, artikel, pieces):
        date = ""
        object = [artikel,pieces, date]
        self.dataarray.append(object)

    def addObjectFull(self, artikel, pieces, date):
        object = [artikel,pieces, date]
        self.dataarray.append(object)


    def renderArtikel(self):
        objects = ""
        var = 1
        for obj in self.dataarray: 
            objects = objects + "RAD1" + "\t" + str(var) + "\t1\t\t" +  str(obj[0]) + "\t\t" + str(obj[1]) + "\t" + str(obj[2]) + "\n"
            var = var + 1

        return objects

    def renderHead(self):
        header = ""
        print(self.kundkod)
        print(self.kundensOrdernr)
        print(self.godsmarkning)
        print(self.leverantorskod)
        #header = header + "HVD1" + "\t" + self.kundkod + "\t" + self.kundensOrdernr + "\t\t\t\t" + self.godsmarkning + "\t\t" + self.leverantorskod + "\n"
        header = header + "HVD1" + "\t" + self.kundkod + "\t" + self.kundensOrdernr + "\t\t\t\t" + self.godsmarkning + "\t\t" + self.leverantorskod + "\n"
        return header

    def renderTail(self):
        tail = ""
        tail = tail + "END1\n"
        return tail

    def printout(self):

        self.maintext = self.renderHead() + self.renderArtikel() + self.renderTail()
        print(self.maintext)
        # objects = ""
        # var = 1
        # for obj in self.dataarray: 
        #     #print("artikel " + str(obj[0]) + " antal " + str(obj[1]))
        #     objects = objects + "RAD1" + "\t" + str(var) + "\t1\t\t" +  str(obj[0]) + "\t\t" + str(obj[1]) + "\n"
        #     var = var + 1

        # objects = objects + "END1\n"
        # print(self.outputline)
        # print(objects)
        #self.outputline = self.outputline + objects
        #self.outputline = self.outputline + "totally"

    
    def save(self, filename):
        # objects = ""
        # var = 1
        # for obj in self.dataarray:
        #     var = var + 1
        #     #print("artikel " + str(obj[0]) + " antal " + str(obj[1]))
        #     objects = objects + "RAD1" + "\t" + str(var) + "\t1\t\t" +  str(obj[0]) + "\t\t" + str(obj[1]) + "\n"
        #     var = var + 1
        
        # objects = objects + "END1\n"
        # #self.outputline = self.outputline + objects
        # #self.outputline = self.outputline + "END1\n"
        self.maintext = self.renderHead() + self.renderArtikel() + self.renderTail()
        text_file = open(filename, "w")
        text_file.write(self.maintext)
        text_file.close()
        
        
    def empty(self):
        self.dataarray = []     #Clear list