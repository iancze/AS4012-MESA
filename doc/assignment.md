# Assignment

## Submission
Use the Moodle submission tool to submit:

**Report** containing the narrative text, plots, and numerical results requested for each question. You are free to prepare this report with whatever combination of tools you wish, but it must be self-contained *as a single PDF*. I would suggest either
* save plots as `*.png`, insert into Word or LaTeX document, add text, save to PDF.
* work directly in a Jupyter Notebook, plots appear in Notebook, add text with markdown cells, export to PDF.

**Code**: your `*.py` or `*.ipynb` files. Alternatively, create a "secret" [Gist](https://gist.github.com/) with your code and submit the link.

## Questions

1. (2pts) **Abundances**: Read [Asplund et al. 2009ARA&A..47..481A](https://ui.adsabs.harvard.edu/abs/2009ARA%26A..47..481A/abstract), paying particular attention to Section 1, Section 3, and Tables 1 and 3. What are the recommended values of $X$, $Y$, $Z$, and $XC$ for the protosun, how do they differ from the present day values, and why?

2. (2pts) **First MESA run**: Choose one initial stellar mass from the set of {0.8, 0.9, 1.0, 1.1, 1.2} $M_\odot$ and run [MESA-Web](http://user.astro.wisc.edu/~townsend/static.php?ref=mesa-web) with the following additional parameters: $Z = 0.02$, ?
    
    2.1. Create plots of output of your run using the script (also Jup?), as shown in the plotting example. Submit figures for XX, XX, and YY?
    
    2.2. What are the initial $X$, $Y$, $Z$, and $XC$ abundances in this model, and how do they compare to those recommended by Asplund+09? 

3. (2ps) **ZAMS**: From your plots, identify the Zero-Age Main Sequence (ZAMS) stage, after the model has settled but before the core helium abundance starts to increase significantly. 

    3.1. What are the ZAMS radius $R_\star$, luminosity $L_\star$, and effective temperature $T_\mathrm{eff}$ of your model? What are the temperature and pressure values in the core, $T_c$ and $P_c$, respectively?

    3.2. Which zones are convective and which are radiative? Why? Specify your zones by mass enclosed $M(r)$.

    3.3. What is the star's primary energy source at this stage?

4. (6pts) **Lagrangian Scheme, outward**: Rewrite the numerical integration scheme using the Lagrangian equations with enclosed mass $m$ as an independent variable. Use $T(0) = T_c$ and $P(0) = P_c$ from your MESA-Web run as boundary conditions. Use [see code]() as an example for outward integration of the Euler equations using ODEint. Set up and run a scheme that integrates the Lagrange equations outward from the centre of the star to $m=0.5M_\star$. Plot the results (which?) as a function of $m$, but anticpation that you will combine this with #5. Additionally, record the values of $r$, $P$, $L$, $T$ at the fitting point for the inward integration.

5. (3pts) **Lagrangian Scheme, inward**: Write a second Lagrangian integration scheme that works inward from $M_\star$ to $m=0.5M_\star$. Use the surface values of $R_\star$ and $L_\star$ from your MESA-Web run as boundary conditions. Plot the results (which?) as a function of $m$. Additionally, record the values of $r$, $P$, $L$, $T$ at the fitting point for the inward integration. Combine your plot with #4.
