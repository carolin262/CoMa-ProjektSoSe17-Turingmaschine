import tm

inpu=input("Gebe hier die Inputliste, wie folgt ein (z.B 1,0,0,1,0) : ")
inp=inpu.split(',')
filename=input("Gebe hier bitte den Filename wie folgt als String ein: ./filename :")
bsp=tm.TM._parse_file(filename,inp)
maxslides=int(input("Wieviele Slides sollen max. erstellt werden ?(Integer) : "))
#VTM.set_viewername("Adobe")
colli=bsp[0]
VTM=bsp[1]
slides=[]
i=0
for x in colli.exec_TM(inp): 
    if i>maxslides:
        break
    i+=1
    #print(x)
    slides.append(VTM.draw_frame(*x))
VTM.write_file(VTM.get_grunddokument(slides))
VTM.visualize()

