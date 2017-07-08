import tm
import visual
import os, sys, subprocess

if len(sys.argv) < 4: #ueberprueft auf BOM
    #fragt nach input
    inpu=input("Gebe hier die Inputliste, wie folgt ein (z.B 1,0,0,1,0) : ")
    inp=inpu.split(',')
    filename=input("Gebe hier bitte den Filename wie folgt als String ein: ./filename :")
    viewer=input("Gebe hier den Viewer mit Name an bei d wird der Defaultviewer benutzt : " )

else:
    _, inpu, filename, viewer = sys.argv
    inp = inpu.split(',')

#liest Datei ein und gibt Mal-Kommandos zurueck
turingmachine=tm.TM._parse_file(filename)
tm_commands=turingmachine.exec_TM(inp)

if turingmachine.num_tapes  == "2":
   #schreibt die Mal-Kommandos, zur ueberpruefung
   for x in tm_commands:
        print(x)

else:
    # erstellt Visualisierungsklasse
    VTM=visual.VisualTM(inp, turingmachine.input_alphabet, turingmachine.gamma, turingmachine.num_states, turingmachine.F, turingmachine.blank)

    #setzt viewer
    if viewer != "d":
        VTM.set_viewername(viewer)

    #sammelt alle pdf-Seiten in slides
    slides=[]
    for x in tm_commands:
        print(x)
        slides.append(VTM.draw_frame(*x))

    #erstellt das gesamte Dokument und fuehrt es aus
    VTM.write_file(VTM.get_grunddokument(slides))
    VTM.visualize()
   
