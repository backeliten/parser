from xml.dom import minidom

def run(filename):
    xmldoc = minidom.parse(filename)
    item = []
    quant = []
    itemlist = xmldoc.getElementsByTagName('Row')
    #print(len(itemlist))
    #print(itemlist[0].attributes['RowNumber'].value)
    for s in itemlist:
        #print("loop")
        if(s.attributes['RowType'].value == "1"):
            #print("hello world")
            parts = s.getElementsByTagName('Part')
            #print(parts[0].attributes['PartNumber'].value)
            item.append(parts[0].attributes['PartNumber'].value)
            quantitys = s.getElementsByTagName('Quantity')
            #print(quantitys[0].data)
            #for quantity in quantitys:
            #    print("Heööp")
            for node in quantitys:
                #print(node.childNodes)
                cnode = node.childNodes[0]
                if cnode.nodeType == node.TEXT_NODE:
                    quant.append(cnode.data)

    file = open("C:/Users/backe/temp/elektroskandiaout.txt", 'w')

    for a in range(len(item)):
        print(quant[a]+"\t"+item[a])
        file.write(quant[a]+"\t"+item[a]+"\n\r")

    file.close()

    fileelfa = open("C:/Users/backe/temp/elfaout.txt", 'w')

    for a in range(len(item)):
        print(quant[a]+","+item[a])
        fileelfa.write(quant[a]+","+item[a]+"\n\r")

    fileelfa.close()

#    <data>
#    <items>
#        <item name="item1"></item>
#        <item name="item2"></item>
#        <item name="item3"></item>
#        <item name="item4"></item>
#    </items>
#</data>
