all: article.pdf presentation.pdf

rewardbias.eps: rewardbias.py
	rm -f rewardbias.eps
	./rewardbias.py

subsidycurve.eps: subsidycurve.py
	rm -f subsidycurve.eps
	./subsidycurve.py

article.pdf: rewardbias.eps subsidycurve.eps abstract.tex intro.tex centralizationrisk.tex dualpow.tex forwardblocks.tex coinbasepayoutqueue.tex smoothdifficulty.tex flexcap.tex hardlimits.tex sharding.tex parameters.tex extensionoutputs.tex conclusion.tex article.tex cites.bib
	pdflatex article.tex
	bibtex article.aux
	pdflatex article.tex
	pdflatex article.tex

presentation.pdf: rewardbias.eps subsidycurve.eps presentation.tex
	pdflatex presentation.tex
	pdflatex presentation.tex
