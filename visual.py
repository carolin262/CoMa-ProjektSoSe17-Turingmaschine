#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
class VisualTM:
    def __init__(self):
        self.grunddokument=""
        self.bandtikz=""
        self.tmtikz=""
        self.viewername="AdobeReader"
    
    def get_grunddokument(self):
        """
        erstellt das eigentliche Dokument,
        mit packages, Deckblatt,etc.
        TM-Frames muessen nur noch eingefuegt
        werden
        """
        listband,einalpha,bandalpha,nozust,akztzust=0,0,0,0,0
        dokument=\
'\documentclass[10pt]{beamer} \n \
\hypersetup{pdfpagemode=FullScreen} \n \
\\usepackage{tikz} \n \
\\usetikzlibrary{shadows,patterns,shapes} \n \
\\usetikzlibrary{shapes.arrows,chains} \n \
% serifenfreier Font -- fuer Praesentation geeignet/er \n\
\renewcommand\familydefault{\sfdefault} \n \
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
\newcommand{\themename}{\textbf{\textsc{metropolis}}\\xspace} \n \
\title{Deterministische Turing-Maschine} \n \
\subtitle{TU-Berlin, SoSe17, CoMa2 Programmierprojekt} \n \
\author{Carolin Schwarz 371802 CO2-155,\\ Duc Hoang Tran 222476 CO2-133,\\ Li Yinying 380390 CO2-144\\} \n \
\institute{Betreuer: Ansgar} \n \
\titlegraphic{\hfill\includegraphics[height=2cm]{tu.jpg}} \n \
\begin{document} \n \
\maketitle \n '
        dokument = dokument + self.get_tmtikz(self,listband,einalpha,bandalpha,nozust,akztzust)
        dokument = dokument + "\end{document}"
        return dokument
    
    def get_tmtikz(self,listband,einalpha,bandalpha,nozust,akztzust):
        """
        erstellt die TM-Frames,
        das Band wird hier eingefuegt
        """
        tmframe='\begin{frame}[fragile]{CoMa Turingmaschine} \n \
\n \
\\begin{itemize} \n \
\item Eingabealphabet : \n \
\item Bandalphabet : \n \
\item Leerzeichen :  \n \
\item anzahl an Zustaenden : \n \
\item akzept. Zustaende : \n \
\end{itemize} \n \
\\begin{figure} \n \
\\begin{tikzpicture} \n \
\n \
\edef\sizetape{0.7cm} \n \
\tikzstyle{tmtape}=[draw,minimum size=\sizetape] \n \
\n \
%% Draw TM tape \n \
\\begin{scope}[start chain=1 going right,node distance=-0.15mm] \n \
\node [on chain=1,tmtape,draw=none] {$\\ldots$}; \n \
\node [on chain=1,tmtape] {}; \n \
"+self.get_bandtikz(listband)+" \n \
\node [on chain=1,tmtape,draw=none] {$\ldots$}; \n \
\end{scope} \n \
\end{tikzpicture} \n \
\\begin{tikzpicture} \n \
\node [draw,align=left]{akt. Zustand}; \n \
\\begin{scope}[start chain=2 going right] \n \
\node [draw,left=3cm,arrow box,name=p,on chain=2,arrow box arrows={north:.5cm},minimum size=0.5cm] {}; \n \
\draw[on chain=2]{}; \n \
\node [draw, name=q,left=0cm,on chain=2]{q0}; \n \
\draw [<-] (p) -- (q); \n \
\chainin (q) [join]; \n \
\end{scope} \n \
\end{tikzpicture} \n \
\end{figure} 	\n \
\end{frame} \n'
        return tmframe

    def get_bandtikz(listband):
        #schreibt für jedes Element auf dem listband
        #einen Knoten auf dem Band
            
        band=""
        for i in range(len(listband)):
            band=band+"\node [on chain=1,tmtape] {"+str(listband[i])+"}; \n "
        return band
