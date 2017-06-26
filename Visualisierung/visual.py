#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys, subprocess, copy
class VisualTM:
    def __init__(self,band,bandalpha,einalpha,nozust,akztzust,leerzeichen):
        self.grunddokument=""
        self.bandtikz=""
        self.tmtikz=""
        self.viewername="Adobe"
        self.einalpha=einalpha      #List
        self.bandalpha=bandalpha    #List
        self.neu_band=copy.deepcopy(band)     #List
        self.band=band              #List
        self.nozust=nozust          #Int
        self.kopf_q="q0"            #String
        self.leerzeichen=leerzeichen#String
        self.akztzust=akztzust
    
    def get_grunddokument(self,frames):
        """
        erstellt das eigentliche Dokument,
        mit packages, Deckblatt,etc.
        TM-Frames muessen nur noch eingefuegt
        werden
        """
        dokument=\
'\documentclass[10pt]{beamer} \n \
\hypersetup{pdfpagemode=FullScreen} \n \
\\usepackage{tikz} \n \
\\usetikzlibrary{shadows,patterns,shapes} \n \
\\usetikzlibrary{shapes.arrows,chains} \n \
% serifenfreier Font -- fuer Praesentation geeignet/er \n\
\\renewcommand\\familydefault{\sfdefault} \n \
\listfiles % damit im Log alle benutzten Pakete aufgelistet werden \n \
\\usetheme[progressbar=frametitle]{metropolis} \n \
\\usepackage{appendixnumberbeamer} \n \
\\usepackage{booktabs} \n \
\\usepackage[scale=2]{ccicons} \n \
\\usepackage[utf8]{inputenc} \n \
\\usepackage{pgfplots} \n \
\\usepgfplotslibrary{dateplot} \n \
\\usepackage[ngerman]{babel} \n \
\\usepackage{xspace} \n \
\\newcommand{\\themename}{\\textbf{\\textsc{metropolis}}\\xspace} \n \
\\title{Deterministische Turing-Maschine} \n \
\subtitle{TU-Berlin, SoSe17, CoMa2 Programmierprojekt} \n \
\\author{Carolin Schwarz 371802 CO2-155,\\\ Duc Hoang Tran 222476 CO2-133,\\\ Li Yinying 380390 CO2-144\\\} \n \
\institute{Betreuer: Ansgar} \n \
\\begin{document} \n \
\\maketitle \n'                 #Frame mit Anfangsband
        dokument=dokument+'\\begin{frame}[fragile]{CoMa Turingmaschine} \n \
\n \
\\begin{itemize} \n \
\item Eingabealphabet : '
        dokument=dokument+str(self.einalpha) 
        dokument=dokument+' \n \
\item Bandalphabet : '
        dokument=dokument+str(self.bandalpha)
        dokument=dokument+' \n \
\item Leerzeichen : '
        dokument=dokument+self.leerzeichen
        dokument=dokument+' \n \
\item anzahl an Zustaenden : '
        dokument=dokument+str(self.nozust)
        dokument=dokument+' \n \
\item akzept. Zustaende : '
        dokument=dokument+str(self.akztzust)
        dokument=dokument+\
'\n \
\end{itemize} \n \
\\begin{figure} \n \
\\begin{tikzpicture} \n \
\n \
\edef\sizetape{0.7cm} \n \
\\tikzstyle{tmtape}=[draw,minimum size=\sizetape] \n \
\n \
%% Draw TM tape \n \
\\begin{scope}[start chain=1 going right,node distance=-0.15mm] \n \
\\node [on chain=1,tmtape,draw=none] {$\\ldots$}; \n \
'
        dokument=dokument+self.get_anfang_end_band(self.band)
        dokument=dokument+' \n \
\\node [on chain=1,tmtape,draw=none] {$\ldots$}; \n \
\end{scope} \n \
\end{tikzpicture} \n \
\\begin{tikzpicture} \n \
\\node [draw,align=left]{akt. Zustand}; \n \
\\begin{scope}[start chain=2 going right] \n \
\\node [draw,left=3cm,arrow box,name=p,on chain=2,arrow box arrows={north:.5cm},minimum size=0.5cm] {}; \n \
\draw[on chain=2]{}; \n \
\\node [draw, name=q,left=0cm,on chain=2]{'
        dokument=dokument+self.kopf_q
        dokument=dokument+'}; \n \
\draw [<-] (p) -- (q); \n \
\chainin (q) [join]; \n \
\end{scope} \n \
\end{tikzpicture} \n \
\end{figure} 	\n \
\end{frame} \n'
        for i in range(len(frames)):
            dokument = dokument + frames[i] #self.get_tmtikz([12,2,3],einalpha,bandalpha,nozust,akztzust)
        dokument=dokument+'\end{document}'
        return(dokument)
    
    def get_tmtikz(self,band):
        """
        erstellt die TM-Frames,
        das Band wird hier eingefuegt
        """
        tmframe='\\begin{frame}[fragile]{CoMa Turingmaschine} \n \
\n \
\\begin{itemize} \n \
\item Eingabealphabet : '
        tmframe=tmframe+str(self.einalpha) 
        tmframe=tmframe+' \n \
\item Bandalphabet : '
        tmframe=tmframe+str(self.bandalpha)
        tmframe=tmframe+' \n \
\item Leerzeichen : '
        tmframe=tmframe+self.leerzeichen
        tmframe=tmframe+' \n \
\item anzahl an Zustaenden : '
        tmframe=tmframe+str(self.nozust)
        tmframe=tmframe+' \n \
\item akzept. Zustaende : '
        tmframe=tmframe+str(self.akztzust)
        tmframe=tmframe+'\n \
\end{itemize} \n \
\\begin{figure} \n \
\\begin{tikzpicture} \n \
\n \
\edef\sizetape{0.7cm} \n \
\\tikzstyle{tmtape}=[draw,minimum size=\sizetape] \n \
\n \
%% Draw TM tape \n \
\\begin{scope}[start chain=1 going right,node distance=-0.15mm] \n \
\\node [on chain=1,tmtape,draw=none] {$\\ldots$}; \n \
'
        tmframe=tmframe+band
        tmframe=tmframe+' \n \
\\node [on chain=1,tmtape,draw=none] {$\ldots$}; \n \
\end{scope} \n \
\end{tikzpicture} \n \
\\begin{tikzpicture} \n \
\\node [draw,align=left]{akt. Zustand}; \n \
\\begin{scope}[start chain=2 going right] \n \
\\node [draw,left=3cm,arrow box,name=p,on chain=2,arrow box arrows={north:.5cm},minimum size=0.5cm] {}; \n \
\draw[on chain=2]{}; \n \
\\node [draw, name=q,left=0cm,on chain=2]{'
        tmframe=tmframe+self.kopf_q
        tmframe=tmframe+'}; \n \
\draw [<-] (p) -- (q); \n \
\chainin (q) [join]; \n \
\end{scope} \n \
\end{tikzpicture} \n \
\end{figure} 	\n \
\end{frame} \n'
        return tmframe
    
    def get_anfang_end_band(self,endband):
        band=""
        bandindex=0
        for i in range(3): #vorne auffuellen mit leerzeichen bis zum akt.Zustand
            band=band+"\\node [on chain=1,tmtape] {"+str(self.leerzeichen)+"}; \n "
            bandindex+=1
        for i in range(len(endband)):     # Band aufmalen ausser es geht aus dem Band raus 
            if (bandindex) > 12:
                break
            #if self.neu_band[i]==str(self.leerzeichen):
            #    band=band+"\\node [on chain=1,tmtape] {"+str(self.leerzeichen)+"}; \n "
            #    bandindex=bandindex+1
            #    platzhaltermitte+=1
            #else:
            band=band+"\\node [on chain=1,tmtape] {"+str(endband[i])+"}; \n "
            bandindex=bandindex+1

        for i in range(13-bandindex):
            band=band+"\\node [on chain=1,tmtape] {"+str(self.leerzeichen)+"}; \n "
            bandindex=bandindex+1
        return band


    def get_bandtikz(self,band_position_alt,band_wert_neu,kopf_q,band_position_neu):
        #schreibt für jedes Element auf dem listband
        #einen Knoten auf dem Band
        band=""
        bandlaenge=len(self.neu_band)
        bandindex,platzhaltermitte=0,0
        if len(self.neu_band)<band_position_alt:
            self.neu_band.append(str(self.leerzeichen))
            bandindex=bandindex-1
            bandlaenge+=1
        if band_position_alt < 0:
            bandindex=bandindex-1
            bandlaenge+=1
            help=[]
            help=copy.deepcopy(self.neu_band)
            self.neu_band=[]
            self.neu_band.append(band_wert_neu)
            for i,e in enumerate(help):
                self.neu_band.append(e)
        else:
            self.neu_band[band_position_alt]=band_wert_neu  #setzt neuen Bandwert
        self.kopf_q=kopf_q                              #setzt neuen Kopfzustand q_
        platzhalterVorne=3-(band_position_neu)

        for i in range(platzhalterVorne): #vorne auffuellen mit leerzeichen bis zum akt.Zustand
            band=band+"\\node [on chain=1,tmtape] {"+str(self.leerzeichen)+"}; \n "
            bandindex=bandindex+1
        for i in range(bandlaenge):     # Band aufmalen ausser es geht aus dem Band raus 
            if (bandindex) > 12:
                break
            #if self.neu_band[i]==str(self.leerzeichen):
            #    band=band+"\\node [on chain=1,tmtape] {"+str(self.leerzeichen)+"}; \n "
            #    bandindex=bandindex+1
            #    platzhaltermitte+=1
            #else:
            band=band+"\\node [on chain=1,tmtape] {"+str(self.neu_band[i])+"}; \n "
            bandindex=bandindex+1

        if 12-len(self.neu_band)-(platzhalterVorne) > 0:       #hinten auffuellen mit leerzeichen
            for i in range(13-len(self.neu_band)-platzhalterVorne):
                band=band+"\\node [on chain=1,tmtape] {"+str(self.leerzeichen)+"}; \n "
                bandindex=bandindex+1
        return band


    
    def draw_frame(self,band_position_alt,band_wert_neu,kopf_q,band_position_neu):
        return self.get_tmtikz(self.get_bandtikz(band_position_alt,band_wert_neu,kopf_q,band_position_neu))
    
    def write_file(self,data):
        TMVisual = open("TMvisual.tex", "w")
        TMVisual.write(data)
        TMVisual.close()
    
    def set_viewername(self,name):
        if name=="Foxit":
            acrobatPath = r'C:/Program Files (x86)/Foxit Software/FoxitReader/FoxitReader.exe'
        elif name=="Sumatra":
            acrobatPath = r'C:/Program Files/SumatraPDF/SumatraPDF.exe'
            
        self.viewername=acrobatPath
    
    def visualize(self):
        os.system("texify -p TMvisual.tex")

        pdf = "TMvisual.pdf"
        
        if self.viewername=="Adobe":
            os.startfile("TMvisual.pdf")
        else:
            subprocess.Popen("%s %s" % (self.viewername, pdf))

def test():    
    VTM=VisualTM([1,2,3],[str(11),str(22),str(33),str(44),str(55),str(112),str(222),str(332),str(113),str(223),str(333),str(114),str(224),str(334)],2,"q1,q2","B")
    VTM=VisualTM([str(21),str(78)],[1,2,3],[str(11)],2,"q1,q2","B")

    frame=[VTM.draw_frame(0,"26","q5",0),VTM.draw_frame(0,"1","q1",-1),VTM.draw_frame(-1,"wtf","q3",-2)]
    VTM.write_file(VTM.get_grunddokument(frame))
    VTM.set_viewername("Sumatra")
    VTM.visualize()
