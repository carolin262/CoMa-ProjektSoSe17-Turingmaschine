import tm
import visual
import os, sys, subprocess

if len(sys.argv) < 4:
    inpu=input("Gebe hier die Inputliste, wie folgt ein (z.B 1,0,0,1,0) : ")
    inp=inpu.split(',')
    filename=input("Gebe hier bitte den Filename wie folgt als String ein: ./filename :")
    viewer=input("Gebe hier den Viewer mit Name an bei d wird der Defaultviewer benutzt : " )
else:
    _, inpu, filename, viewer = sys.argv
    inp = inpu.split(',')

turingmachine=tm.TM._parse_file(filename)
tm_commands=turingmachine.exec_TM(inp)

if turingmachine.num_tapes  == "2":
   for x in tm_commands:
        print(x)

else:
    VTM=visual.VisualTM(inp, turingmachine.input_alphabet, turingmachine.gamma, turingmachine.num_states, turingmachine.F, turingmachine.blank)
    if viewer != "d":
        VTM.set_viewername(viewer)
    slides=[]

    for x in tm_commands:
        print(x)
        slides.append(VTM.draw_frame(*x))
    VTM.write_file(VTM.get_grunddokument(slides))
    VTM.visualize()
   
