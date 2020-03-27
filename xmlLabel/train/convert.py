# -*- coding: utf-8 -*-

from xml.dom import minidom
import os
import glob

lut={}
lut["i1"] =0
lut["i10"] =0
lut["i11"] =0
lut["i12"] =0
lut["i13"] =0
lut["i14"] =0
lut["i15"] =0
lut["i2"] =0
lut["i3"] =0
lut["i4"] =0
lut["i5"] =0
lut["il100"] =0
lut["il110"] =0
lut["il50"] =0
lut["il60"] =0
lut["il70"] =0
lut["il80"] =0
lut["il90"] =0
lut["io"] =0
lut["ip"] =0
lut["p1"] =1
lut["p10"] =1
lut["p11"] =1
lut["p12"] =1
lut["p13"] =1
lut["p14"] =1
lut["p15"] =1
lut["p16"] =1
lut["p17"] =1
lut["p18"] =1
lut["p19"] =1
lut["p2"] =1
lut["p20"] =1
lut["p21"] =1
lut["p22"] =1
lut["p23"] =1
lut["p24"] =1
lut["p25"] =1
lut["p26"] =1
lut["p27"] =1
lut["p28"] =1
lut["p3"] =1
lut["p4"] =1
lut["p5"] =1
lut["p6"] =1
lut["p7"] =1
lut["p8"] =1
lut["p9"] =1
lut["pa10"] =1
lut["pa12"] =1
lut["pa13"] =1
lut["pa14"] =1
lut["pa8"] =1
lut["pb"] =1
lut["pc"] =1
lut["pg"] =1
lut["ph1.5"] =1
lut["ph2"] =1
lut["ph2.1"] =1
lut["ph2.2"] =1
lut["ph2.4"] =1
lut["ph2.5"] =1
lut["ph2.8"] =1
lut["ph2.9"] =1
lut["ph3"] =1
lut["ph3.2"] =1
lut["ph3.5"] =1
lut["ph3.8"] =1
lut["ph4"] =1
lut["ph4.2"] =1
lut["ph4.3"] =1
lut["ph4.5"] =1
lut["ph4.8"] =1
lut["ph5"] =1
lut["ph5.3"] =1
lut["ph5.5"] =1
lut["pl10"] =1
lut["pl100"] =1
lut["pl110"] =1
lut["pl120"] =1
lut["pl15"] =1
lut["pl20"] =1
lut["pl25"] =1
lut["pl30"] =1
lut["pl35"] =1
lut["pl40"] =1
lut["pl5"] =1
lut["pl50"] =1
lut["pl60"] =1
lut["pl65"] =1
lut["pl70"] =1
lut["pl80"] =1
lut["pl90"] =1
lut["pm10"] =1
lut["pm13"] =1
lut["pm15"] =1
lut["pm1.5"] =1
lut["pm2"] =1
lut["pm20"] =1
lut["pm25"] =1
lut["pm30"] =1
lut["pm35"] =1
lut["pm40"] =1
lut["pm46"] =1
lut["pm5"] =1
lut["pm50"] =1
lut["pm55"] =1
lut["pm8"] =1
lut["pn"] =1
lut["pne"] =1
lut["po"] =1
lut["pr10"] =1
lut["pr100"] =1
lut["pr20"] =1
lut["pr30"] =1
lut["pr40"] =1
lut["pr45"] =1
lut["pr50"] =1
lut["pr60"] =1
lut["pr70"] =1
lut["pr80"] =1
lut["ps"] =1
lut["pw2"] =1
lut["pw2.5"] =1
lut["pw3"] =1
lut["pw3.2"] =1
lut["pw3.5"] =1
lut["pw4"] =1
lut["pw4.2"] =1
lut["pw4.5"] =1
lut["w1"] =2
lut["w10"] =2
lut["w12"] =2
lut["w13"] =2
lut["w16"] =2
lut["w18"] =2
lut["w20"] =2
lut["w21"] =2
lut["w22"] =2
lut["w24"] =2
lut["w28"] =2
lut["w3"] =2
lut["w30"] =2
lut["w31"] =2
lut["w32"] =2
lut["w34"] =2
lut["w35"] =2
lut["w37"] =2
lut["w38"] =2
lut["w41"] =2
lut["w42"] =2
lut["w43"] =2
lut["w44"] =2
lut["w45"] =2
lut["w46"] =2
lut["w47"] =2
lut["w48"] =2
lut["w49"] =2
lut["w5"] =2
lut["w50"] =2
lut["w55"] =2
lut["w56"] =2
lut["w57"] =2
lut["w58"] =2
lut["w59"] =2
lut["w60"] =2
lut["w62"] =2
lut["w63"] =2
lut["w66"] =2
lut["w8"] =2
lut["wo"] =2
lut["i6"] =0
lut["i7"] =0
lut["i8"] =0
lut["i9"] =0
lut["ilx"] =0
lut["p29"] =1
lut["w29"] =2
lut["w33"] =2
lut["w36"] =2
lut["w39"] =2
lut["w4"] =2
lut["w40"] =2
lut["w51"] =2
lut["w52"] =2
lut["w53"] =2
lut["w54"] =2
lut["w6"] =2
lut["w61"] =2
lut["w64"] =2
lut["w65"] =2
lut["w67"] =2
lut["w7"] =2
lut["w9"] =2
lut["pax"] =1
lut["pd"] =1
lut["pe"] =1
lut["phx"] =1
lut["plx"] =1
lut["pmx"] =1
lut["pnl"] =1
lut["prx"] =1
lut["pwx"] =1
lut["w11"] =2
lut["w14"] =2
lut["w15"] =2
lut["w17"] =2
lut["w19"] =2
lut["w2"] =2
lut["w23"] =2
lut["w25"] =2
lut["w26"] =2
lut["w27"] =2
lut["pl0"] =1
lut["pl4"] =1
lut["pl3"] =1
lut["pm2.5"] =1
lut["ph4.4"] =1
lut["pn40"] =1
lut["ph3.3"] =1
lut["ph2.6"] =1


def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_xml2yolo( lut ):

    for fname in glob.glob("*.xml"):
        
        xmldoc = minidom.parse(fname)
        
        fname_out = (fname[:-4]+'.txt')

        with open(fname_out, "w") as f:

            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                # get class label
                classid =  (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in lut:
                    label_str = str(lut[classid])
                else:
                    label_str = "-1"
                    print ("warning: label '%s' not in look-up table" % classid)

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width,height), b)
                #print(bb)

                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print ("wrote %s" % fname_out)



def main():
    convert_xml2yolo( lut )


if __name__ == '__main__':
    main()