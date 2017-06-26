Zum Zeichnen braucht man jeweils folgende Methoden:

1. erstelle ein Objekt der Klasse 
	VisualTM(band [],bandalphabet[],eingabealphabet[],Anzahl an Zuständen INT, akzeptierende Zustände[], leerzeichen String)

	bsp: VTM=VisualTM([str(11)],[11],[11,22],2,"q1","B")

2. erstelle Slides für das pdf, diese Fkt gibt einen String zurück, Speicher diesen in eine Liste, achte auf die richtige Reihenfolge, für die pdf.
	String= Objektname.draw_frame(alte band position hier wird das Zeichen veraendert INT, band wert neu String, Zustand des Lesekopfes String, band position neu INT)

	Bsp: slide1=VTM.draw_frame(0,"26","q1",0)
	oder
	Bsp2: slides=[]
		  slides.append(VTM.draw_frame(0,"26","q1",0))

3. schreiben des Dokumentes, ACHTUNG hier müssen alle in [2] erstellten Slides=[slide1,slide2,...] in einer Liste eingegeben werden	
	Objktname.write_file(Objektname.get_grunddokument(slides))

	Bsp. VTM.write_file(VTM.get_grunddokument(slides))

4. PDF-Viewer, hier ist die AUfgabenstellung kacke, eigentlich könnt ihr hier einen anderen viewer benutzten, dafür müsst ihr aber in meinem Code aktiv eingreifen, das ist doof. Wenn ihr die folgende funktion einfach nicht benutzt, wird euer Standart-pdf-Viewer verwendet.
Theoretisch:
	Objektname.set_viewername("PDF-Programm-Name")

5. PDF Anzeigen lassen! 
	Objektname.visualize()

	Bsp: VTM.visualize()

Mehr braucht ihr nicht, viel Spaß und viel Erfolg! 