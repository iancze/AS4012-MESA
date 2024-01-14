# AS4012: Nebulae And Stars 2 Stellar Structure Computational Project
* University of St Andrews, Spring 2024
* Instructor: Dr. Ian Czekala

For this assessed computational project, you will compute the internal structure of a Sun-like star on the Zero-Age-Main-Sequence (ZAMS) using the Modules for Experiments in Stellar Astrophysics (MESA) code. In Part I, you will use the online interface MESA-web to run a numerical integration and write your own Python code to analyze the output. In Part II, you will implement your own Lagrangian scheme to solve the equations of stellar structure, and compare your results to your MESA run in Part I. For the full assignment, see the [**Assignment Questions**](doc/assignment.md).

## Submission

All materials must be submitted through Moodle by **23:59 February 23rd, 2024**. There will be a penalty of 5% of the total available marks per day or partial day of late submission, including weekends and holidays. Requests for extensions made after the end of Week 5 (Feb 16) will not be considered.

Use the Moodle submission tool to submit:

**Report** containing the narrative text, plots, and numerical results requested for each question. You are free to prepare this report with whatever combination of tools you wish, but it must be self-contained *as a single PDF*. I would suggest either
* save plots as `*.png`, insert into Word or LaTeX document, add text, save to PDF.
* work directly in a Jupyter Notebook, plots appear in Notebook, add text with markdown cells, export to PDF.

**Code**: your `*.py` or `*.ipynb` files. Alternatively, create a "secret" [Gist](https://gist.github.com/) with your code and submit the link.

## Grading Rubric
The assignment counts for 25% of your module grade. The [**Assignment Questions**](doc/assignment.md) have point values listed beside them. There are an additional XX points awarded for report quality, for a total of YY points.

**Excellent** quality reports will:
* Demonstrate a correct understanding of the underlying physics solved by the MESA code.
* Concisely and directly explain the significance of numerical results using narrative text.
* Contain correct numerical results, and correctly implement the Lagrangian scheme.
* Demonstrate an understanding of how the Lagrangian scheme in Part II relates to the output from MESA in Part I.

**Average** quality reports may:
* Demonstrate a largely correct understanding of the subject matter, but may evidence small misconceptions.
* Present correct numerical results, but may fail to fully explain their significance.
* Be vague or overly wordy with their narrative text.
* Fail to demonstrate understanding of the conceptual links between Part I and II.

**Poor** quality reports may:
* Demonstrate an incorrect understanding of the subject matter and the numerical calculations.
* Contain numerical errors.
* Fail to connect physical and numerical understanding across parts of the assignment.
* Be incomplete.

The narrative aspect of your report is as important to understanding the results of your analysis as your numerical values are. Assume that you are writing a technical report to your manager or team members. Take pride in your work and strive for clarity, concision, and excellence.


## Assignment Questions

See the [**Assignment Questions**](doc/assignment.md).

## Code Installation

[![tests](https://github.com/iancze/AS4012-MESA/actions/workflows/tests.yml/badge.svg)](https://github.com/iancze/AS4012-MESA/actions/workflows/tests.yml)

This repository includes code to help you analyze and plot the output from your MESA-Web run. To install this code into your Python environment

1. Download this repository from GitHub.
2. Enter the root of the repository, and run 
```
pip install .
```
3. Now, in your Python interpreter, you should be able to do
```
>>> import as4012_sstr
```
If you have any issues, please review the [guide to installing Python packages](https://packaging.python.org/en/latest/tutorials/installing-packages/). If your issues persist, please contact <ic95@st-andrews.ac.uk>.

## References

* [Asplund et al. 2009ARA&A..47..481A](https://ui.adsabs.harvard.edu/abs/2009ARA%26A..47..481A/abstract) You can download the article if you are on the StA network, otherwise there is a copy on Moodle.  
* [R. Kippenhahn, A. Weigert, A. Weiss (2013) "Stellar structure and Evolution](https://sta.rl.talis.com/link?url=https%3A%2F%2Fdoi-org.ezproxy.st-andrews.ac.uk%2F10.1007%2F978-3-642-30304-3&sig=fdcd1071b225a1cf90b44eda5279280c95987ab43c127ec62127524cf667c523) E-Textbook (free to StA)
* [MESA-Web](http://user.astro.wisc.edu/~townsend/static.php?ref=mesa-web) the online interface you will use to run MESA.
* [Fields et al. 2023](https://ui.adsabs.harvard.edu/abs/2023arXiv230915930F/abstract): Publication to appear in the Astronomy Education Journal describing MESA-Web
* [MESA](https://docs.mesastar.org/en/release-r23.05.1/), the underlying software (FYI).
* [DSFE 2018 grading rubric](https://matthew-brett.github.io/dsfe/projects/rubric), inspiration for rubric.


```{toctree}
:caption: Contents
:maxdepth: 2

assignment
api
```
