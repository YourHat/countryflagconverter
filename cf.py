from PIL import Image
import PIL
import numpy as np


iv = [[0,[243,244,241]],[1,[158,64,57]],[2,[76,76,84]],[3,[74,65,60]],[4,[159,89,103]],[5,[193,195,171]],[6,[151,86,94]],[7,[176,140,129]],[8,[167,182,109]],[9,[232,131,145]],[10,[80,199,144]],[11,[34,149,230]],[12,[135,71,82]],[13,[112,65,135]],[14,[251,244,228]],[15,[250,21,5]],[16,[95,80,75]],[17,[241,174,180]],[18,[16,74,45]],[19,[156,91,98]],[20,[233,138,153]],[21,[166,124,25]],[22,[234,205,210]],[23,[219,209,215]],[24,[187,165,154]],[25,[252,10,50]],[26,[150,89,127]],[27,[217,23,57]],[28,[239,220,220]],[29,[234,205,210]],[30,[93,173,134]],[31,[223,66,94]],[32,[27,52,33]],[33,[192,50,34]],[34,[151,97,117]],[35,[205,122,59]],[36,[207,169,59]],[37,[217,21,40]],[38,[182,130,133]],[39,[180,29,61]],[40,[156,55,55]],[41,[151,63,86]],[42,[121,105,97]],[43,[135,53,109]],[44,[235,196,187]],[45,[203,16,99]],[46,[29,132,108]],[47,[248,35,27]],[48,[165,181,171]],[49,[114,10,26]],[50,[126,118,71]],[51,[144,100,87]],[52,[153,113,40]],[53,[67,50,111]],[54,[90,140,70]],[55,[235,220,184]],[56,[95,100,101]],[57,[65,56,167]],[58,[156,119,42]],[59,[120,147,55]],[60,[158,118,42]],[61,[34,95,152]],[62,[99,129,52]],[63,[88,173,172]],[64,[31,116,94]],[65,[113,88,79]],[66,[159,124,97]],[67,[157,120,43]],[68,[10,144,191]],[69,[12,26,18]],[70,[158,98,59]],[71,[152,145,102]],[72,[244,55,54]],[73,[141,132,48]],[74,[89,172,133]],[75,[93,109,106]],[76,[82,91,31]],[77,[118,75,56]],[78,[158,136,125]],[79,[140,124,44]],[80,[103,180,205]],[81,[159,132,124]],[82,[92,49,44]],[83,[226,211,167]],[84,[97,100,90]],[85,[122,108,60]],[86,[23,137,71]],[87,[210,7,42]],[88,[68,27,8]],[89,[239,216,222]],[90,[82,135,102]],[91,[104,143,141]],[92,[95,101,136]],[93,[171,226,84]],[94,[183,6,31]],[95,[169,128,148]],[96,[157,131,121]],[97,[179,202,161]],[98,[90,116,134]],[99,[225,89,106]],[100,[158,127,155]],[101,[121,175,202]],[102,[218,41,68]],[103,[58,67,125]],[104,[159,111,142]],[105,[175,114,140]],[106,[159,114,142]],[107,[178,115,143]],[108,[219,60,80]],[109,[158,64,15]],[110,[182,64,93]],[111,[158,130,119]],[112,[31,23,39]],[113,[159,128,156]],[114,[164,130,122]],[115,[181,87,6]],[116,[242,185,188]],[117,[250,172,90]],[118,[233,130,144]],[119,[149,64,76]],[120,[181,143,92]],[121,[107,43,79]],[122,[190,155,178]],[123,[159,101,63]],[124,[164,112,146]],[125,[195,123,138]],[126,[150,51,58]],[127,[225,96,111]],[128,[132,117,171]],[129,[161,120,43]],[130,[100,125,32]],[131,[105,75,48]],[132,[145,172,54]],[133,[44,114,14]],[134,[192,29,57]],[135,[177,142,163]],[136,[53,115,110]],[137,[82,102,89]],[138,[86,181,215]],[139,[108,125,70]],[140,[182,124,44]],[141,[132,124,103]],[142,[203,103,128]],[143,[53,98,140]],[144,[50,33,74]],[145,[73,62,49]],[146,[15,84,128]],[147,[211,90,20]],[148,[145,108,104]],[149,[27,25,43]],[150,[30,143,188]],[151,[68,79,136]],[152,[230,196,37]],[153,[238,214,137]],[154,[86,115,167]],[155,[42,73,53]],[156,[95,83,96]],[157,[78,60,54]],[158,[158,185,218]],[159,[187,187,208]],[160,[205,214,219]],[161,[165,193,209]],[162,[171,181,140]],[163,[19,20,69]],[164,[85,49,47]],[165,[50,35,24]],[166,[75,23,48]],[167,[38,37,36]],[168,[219,234,250]],[169,[44,25,31]],[170,[214,192,121]],[171,[210,188,160]],[172,[221,125,25]]]

#multiple picture

#for x in range(10):
#    im = Image.open('d'+str(x)+'.jpg')
#    pix = im.load()
#    hight, width = im.size
#    numimage = []
#    for i in range(width):
#        numn = []
#        for j in range(hight):
#            v = 1
#            d = 1000
#            r,g,b = im.getpixel((j,i))
#            for h in iv:
#                q = abs(r - h[1][0]) + abs(g - h[1][1]) + abs(b - h[1][2])
#                if q <= d:
#                    d = q
#                    v = h[0]
#            numn.append(str(v)+'.jpg')
#        numimage.append(numn)
#    list_img = []
#    new_im = Image.new('RGB', (40*hight,40*width),(250,250,250))
#    l = 0
#    for i in numimage:
#        k = 0
#        for j in i:
#            new_im.paste(Image.open(j),(k,l))
#            k += 40
#        l +=40
#    new_im.save('pic'+str(x)+'.jpg')
#    print('pic'+str(x)+'.jpg is done!!')

#----------------------------------------------------------------
#one picture

im = Image.open('d0.jpg')
pix = im.load()
hight, width = im.size
numimage = []
for i in range(width):
    numn = []
    for j in range(hight):
        v = 1
        d = 1000
        r,g,b = im.getpixel((j,i))
        r = (r)
        for h in iv:
            q = abs(r - h[1][0]) + abs(g - h[1][1]) + abs(b - h[1][2])
            if q <= d:
                d = q
                v = h[0]
        numn.append(str(v)+'.jpg')
    numimage.append(numn)
list_img = []
new_im = Image.new('RGB', (40*hight,40*width),(250,250,250))
l = 0
for i in numimage:
    k = 0
    for j in i:
        new_im.paste(Image.open(j),(k,l))
        k += 40
    l +=40
new_im.save('newpic.jpg')
print('pic.jpg is done!!')

