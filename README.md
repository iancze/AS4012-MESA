# AS4012: Nebulae And Stars 2 Stellar Structure Computational Project
* University of St Andrews, Spring 2024
* Instructor: Dr. Ian Czekala

For this assessed computational project (25% of module grade), you will compute the internal structure of a Sun-like star on the Zero-Age-Main-Sequence (ZAMS) using Modules for Experiments in Stellar Astrophysics code. You will use the online interface MESA-web to run a numerical integration and write your own Python code to analyze the output.


All materials must be submitted through Moodle by **DATE**. There will be a penalty of 5% of the total available marks per day or partial day of late submission, including weekends and holidays. Requests for extensions made after the end of Week 5 will not be considered.

## Installation

[![tests](https://github.com/iancze/AS4012-MESA/actions/workflows/tests.yml/badge.svg)](https://github.com/iancze/AS4012-MESA/actions/workflows/tests.yml)

This repository includes code to help you analyze and plot the output from your MESA-Web run. To install this code into your Python enivornment

1. Download this repository from GitHub.
2. Enter the root of the repository, and run 
```
pip install .
```
3. Now, in your Python interpreter, you should be able to do
```
>>> import as4012_mesa
```
If you have any issues, please review the [guide to installing Python packages](https://packaging.python.org/en/latest/tutorials/installing-packages/). If your issues persist, please contact <ic95@st-andrews.ac.uk>.


## Assignment

See the [**Assignment Questions**](doc/assignment.md).


## References

* [Asplund et al. 2009ARA&A..47..481A](https://ui.adsabs.harvard.edu/abs/2009ARA%26A..47..481A/abstract) You can download the article if you are on the StA network, otherwise there is a copy on Moodle.  
* [MESA-Web](http://user.astro.wisc.edu/~townsend/static.php?ref=mesa-web) the interface you will use to access MESA.
* [MESA](https://docs.mesastar.org/en/release-r23.05.1/), the underlying software (FYI, only).
