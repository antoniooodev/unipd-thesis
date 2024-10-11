.PHONY: clean tectonic tectonic-debug latexmk latexmk-debug

clean:
	rm -rf build/*

tectonic:
	mkdir -p build
	@echo "Compiling template.tex with tectonic (silent mode)..."
	@tectonic -X compile template.tex --keep-intermediates > /dev/null 2>&1
	@echo "Running makeglossaries..."
	@makeglossaries template > /dev/null 2>&1
	@echo "Compiling template.tex again with tectonic..."
	@tectonic -X compile template.tex > /dev/null 2>&1
	@echo "Moving generated files to build directory..."
	@mv template.acn template.acr template.alg template.aux template.bbl template.bcf template.glg template.glo template.gls template.ist template.lof template.lot template.toc template.run.xml template.slg template.slo template.sls ./build/

tectonic-debug:
	mkdir -p build
	@echo "Compiling template.tex with tectonic (debug mode)..."
	@tectonic -X compile template.tex --keep-intermediates
	@echo "Running makeglossaries..."
	@makeglossaries template
	@echo "Compiling template.tex again with tectonic..."
	@tectonic -X compile template.tex
	@echo "Moving generated files to build directory..."
	@mv template.acn template.acr template.alg template.aux template.bbl template.bcf template.glg template.glo template.gls template.ist template.lof template.lot template.toc template.run.xml template.slg template.slo template.sls ./build/

latexmk:
	mkdir -p build
	@echo "Compiling template.tex with latexmk..."
	@latexmk -shell-escape -file-line-error -pdf template > /dev/null 2>&1
	@echo "Moving generated files to build directory..."
	@mv template.acn template.acr template.alg template.aux template.bbl template.bcf template.blg template.fdb_latexmk template.fls template.glg template.glo template.gls template.ist template.lof template.log template.lot template.run.xml template.toc template.slg template.slo template.sls ./build/

latexmk-debug:
	mkdir -p build
	@echo "Compiling template.tex with latexmk (debug mode)..."
	@latexmk -shell-escape -file-line-error -pdf template
	@echo "Moving generated files to build directory..."
	@mv template.acn template.acr template.alg template.aux template.bbl template.bcf template.blg template.fdb_latexmk template.fls template.glg template.glo template.gls template.ist template.lof template.log template.lot template.run.xml template.toc template.slg template.slo template.sls ./build/