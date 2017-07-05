#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys, subprocess, copy
class VisualTM:
    def __init__(self,band,einalpha,bandalpha,nozust,akztzust,leerzeichen):
        self.grunddokument=""
        self.bandtikz=""
        self.tmtikz=""
        self.leerzeichen=leerzeichen#String
        self.einalpha=einalpha      #List
        self.bandalpha=bandalpha    #List
        self.viewername=''
        self.neu_band=[self.leerzeichen]*1000+band+[self.leerzeichen]*1000    #List
        self.band=band              #List
        self.nozust=nozust          #Int
        self.kopf_q="q0"            #String
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
        anzeige=[]
        start=1000
        #print(self.neu_band,band_position_alt)
        
        #print(self.neu_band)
        anzeige=self.neu_band[0:3]+endband+self.neu_band[3+len(endband):-1] #setzt neuen Bandwert

        #print(anzeige)
        for i in range(13):    # Band aufmalen ausser es geht aus dem Band raus 
            if anzeige[i]!= self.leerzeichen :
                band=band+"\\node [on chain=1,tmtape] {"+str(anzeige[i])+"}; \n "
            else:
                band=band+"\\node [on chain=1,tmtape] {"+str(self.leerzeichen)+"}; \n "
        return band


    def get_bandtikz(self,band_position_alt,band_wert_neu,kopf_q,band_position_neu):
        #schreibt für jedes Element auf dem listband
        #einen Knoten auf dem Band
        band=""
        anzeige=[]
        start=1000
        #print(self.neu_band,band_position_alt)
        
        #print(self.neu_band)
        self.neu_band[start+band_position_alt]=band_wert_neu
        anzeige=self.neu_band[start-3+band_position_neu:start+10+band_position_neu] #setzt neuen Bandwert
        
        print("neu_band",anzeige)
        self.kopf_q=kopf_q #neuer Kopfzustand

        #print(anzeige)
        for i in range(13):    # Band aufmalen ausser es geht aus dem Band raus 
            if anzeige[i]!= self.leerzeichen :
                band=band+"\\node [on chain=1,tmtape] {"+str(anzeige[i])+"}; \n "
            else:
                band=band+"\\node [on chain=1,tmtape] {"+str(self.leerzeichen)+"}; \n "
        return band


    
    def draw_frame(self,band_position_alt,band_wert_neu,kopf_q,band_position_neu):
        return self.get_tmtikz(self.get_bandtikz(band_position_alt,band_wert_neu,kopf_q,band_position_neu))
    
    def write_file(self,data):
        TMVisual = open("TMvisual.tex", "w")
        TMVisual.write(data)
        TMVisual.close()
    
    def set_viewername(self,name):
        self.viewername=name    

    def visualize(self):
        print("...the machine is still turing... DO NOT SHUT DOWN...")
        os.system("texify -p TMvisual.tex >nul")

        pdf = "TMvisual.pdf"
        if self.viewername=='':
            os.startfile(pdf)
        else:
            subprocess.Popen("%s %s" % (self.viewername, pdf))


