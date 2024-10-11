## Getting Started

### With a Local LaTeX Installation

*[See below](#with-a-remote-cloud-based-service) for alternatives to a local LaTeX installation*

*See “[minimal installation](minimal_installation)” for instructions on how to build/use a minimal installation of LaTeX (<100 MB vs. 5GB for tex-live), which is just enough to compile the template successfully*

1. Download LaTeX:
   * **Windows:** install [TeX-Live](https://www.tug.org/texlive/) or [MikTeX](https://miktex.org).
   * **Linux:** install [TeX-Live](https://www.tug.org/texlive/) or [MikTeX](https://miktex.org).
   * **macOS:** install [MacTeX](https://www.tug.org/mactex/) (a macOS version of [TeX-Live](https://www.tug.org/texlive/)) or [MikTeX](https://miktex.org).
2. Download “unipdthesis” by either:
   * Cloning the [GitHub repository](https://github.com/BIRSAx2/unipdthesis) with <kbd>git clone --depth=1 https://github.com/BIRSAx2/unipdthesis.git</kbd>; or
   <!-- * Downloading the [latest version from the GitHub repository as a Zip file](https://github.com/BIRSAx2/unipdthesis/archive/main.zip) -->
3. Compile the document with you favorite LaTeX processor (pdfLaTeX, XeLaTeX or LuaLaTeX):
   * The main file is named “*template.tex*”.
   * Either load it in your favorite [LaTeX text editor](https://en.wikipedia.org/wiki/Comparison_of_TeX_editors) or compile it in the terminal with
     <kbd>latexmk -shell-escape -file-line-error  -pdf template</kbd>.  If you use a LaTeX text editor, please notice that the NOVAthesis template uses `biber`and not `bibtex` to process the bibliography, which means that most probably you have to open the _Editor Preferences_ and somewhere (depends on the Editor) change `bibtex`to `biber`.
   * If Murphy is elsewhere, LaTeX will create the file “`template.pdf`”, which you may open with your favorite PDF viewer.
4. Edit the files in the “*Config*” folder:

| File                 | Contents                                                                                                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0_memoir.tex`       | Options specific for the `memoir` package.  _Don't touch this file unless you know what you are doing!_                                                                     |
| `1_unipdthesis.tex`   | Configure the template, i.e., the document type, the school, the used languages, etc.                                                                                       |
| **`2_biblatex.tex`** | **Configure the bibliography.**                                                                                                                                             |
| **`3_cover.tex`**    | **Configure cover contents (e.g., author's name, thesis/dissertation title, advisers, committee, etc)**                                                                     |
| **`4_files.tex`**    | **Configure the files for chapters, appendices, annexes, etc…**                                                                                                         |
| **`5_packages.tex`** | **Configure additional packages and commands**                                                                                                                              |
| `6_list_of.tex`      | Configure the lists to be printed (table of contents, list of figures, list of tables, list of listings, etc).  _Don't touch this file unless you know what you are doing!_ |
|                      |                                                                                                                                                                             |
| `9_nova_fct.tex`     | Configuration specific to **nova/fct**                                                                                                                                      |
| `9_nova_ims.tex`     | Configuration specific to **nova/ims**                                                                                                                                      |
| `9_nova_itqb.tex`    | Configuration specific to **nova/itqb**                                                                                                                                     |
| `9_ulisboa_fmv.tex`  | Configuration specific to **ulisboa/fmv**                                                                                                                                   |
| `9_uminho.tex`       | Configuration specific to **uminho** (all schools)                                                                                                                          |

5. Recompile de document:
   * See 3. above.
6. You're done with a beautifully formatted thesis/dissertation! 😃