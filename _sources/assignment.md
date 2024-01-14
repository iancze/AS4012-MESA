# Assignment

Many questions ask for narrative text to explain your results. Write at most 3 sentences for each sub-question.

For more information, there is the very helpful textbook [Stellar structure and Evolution](https://sta.rl.talis.com/link?url=https%3A%2F%2Fdoi-org.ezproxy.st-andrews.ac.uk%2F10.1007%2F978-3-642-30304-3&sig=fdcd1071b225a1cf90b44eda5279280c95987ab43c127ec62127524cf667c523) by Kippenhahn et al., available through the StA library as an E-Textbook. Highly relevant sub-chapters are 1.1, 1.2, 10.1, 11.1, 11.2, 12.1, and 12.2.

## Part I: Stellar structure and evolution with MESA

1. (2pts) **Abundances**: Read [Asplund et al. 2009ARA&A..47..481A](https://ui.adsabs.harvard.edu/abs/2009ARA%26A..47..481A/abstract), paying particular attention to Section 1, Section 3, Tables 1 and 3, and the definition of logarithmic abundances in S3.0. What are the recommended values for *mass fractions* $X$ (H), $Y$ (He), $Z$ (all elements except H and He), and $X_\mathrm{C}$ (just C) for the protosun, how do they differ from the present day values, and why?

2. (2pts) **MESA run**: Choose one initial stellar mass from the set of {0.8, 0.9, 1.0, 1.1, 1.2} $M_\odot$ and submit a MESA-Web [calculation](http://user.astro.wisc.edu/~townsend/static.php?ref=mesa-web-submit). Leave all other parameters at their default values. Download the run output when completed. Before continuing, review the MESA-Web [output documentation](http://user.astro.wisc.edu/~townsend/static.php?ref=mesa-web-output).
    
    2.0. View the `.mp4` movie. What does each frame in the movie represent? Does the movie play linearly with time? Why or why not?
    
    2.1. What calculations did MESA perform? What is represented by each `profileXX.data` file?

    2.2 Use `trimmed_history.data` to plot $L$ vs. $T_\mathrm{eff}$ for all timesteps in the model. You may wish to use either a scatter plot or `plt.plot` with `markerstyle="."` to show the timesteps.

    2.3. Use `trimmed_history.data` and the `plot_abundances` routine to create a plot of the mass fractions $X$, $Y$, $Z$, and $X_\mathrm{C}$ of the star as a function of time. How do the initial mass fractions compare to the Asplund+09 values for the protosun?
    
3. (2pts) **ZAMS**: From your plot, identify the time step $i$ (integer) and Age (yr) corresponding to the start of the Zero-Age Main Sequence (ZAMS), after the model has settled but before the core helium abundance starts to increase significantly. 

    3.1. Read `trimmed_history.data` at this time step $i$ to determine the ZAMS radius $R_\star$, luminosity $L_\star$, effective temperature $T_\mathrm{eff}$, as well as the temperature and pressure values in the core, $T_c$ and $P_c$, respectively.

    3.2. Use the `profiles.index` file to map time step index $i$ to appropriate `profileXX.data` file. Read the correct `profileXX.data` file for your time step and plot quantities $\nabla$ ?? vs. mass enclosed coordinate $m$ to answer which zones are convective and which are radiative? Why?

    3.3. What is the star's primary energy source at this stage? How do you know?

## Part II: Solving the stellar structure equations yourself using the shooting method (Schwarzchild)

As you saw in Part I, the shooting method of solving the equations of stellar structure ([Schwarzchild 1958](https://encore.st-andrews.ac.uk/iii/encore/record/C__Rb3087134__Sstructure%20and%20evolution%20of%20stars__Orightresult__U__X7?lang=eng&suite=def)) has been eclipsed by modern partial differential equation solvers. However, its implementation is simple enough to expose you to the numerical techniques used in stellar structure calculations. 

As you work through this part, reference the equations of stellar structure and their Eulerian/Lagrangian formulations as presented in Lectures 2 & 3.

1. Start from the template code in `template/example.py`. Use the routines in `as4012_sstr.properties` to set up your `odeint` call. Rewrite the numerical integration scheme using the Lagrangian equations with enclosed mass $m$ as an independent variable.

2. (6pts) **Lagrangian Scheme, outward**:  Use $T(0) = T_c$ and $P(0) = P_c$ from your MESA-Web run as boundary conditions. Use XX as an example for outward integration of the Euler equations using ODEint. Set up and run a scheme that integrates the Lagrange equations outward from the centre of the star to $m=0.5M_\star$. Plot the results (which?) as a function of $m$, but anticipate that you will combine this with #5. Additionally, record the values of $r$, $P$, $L$, $T$ at the fitting point for the inward integration.

5. (3pts) **Lagrangian Scheme, inward**: Write a second Lagrangian integration scheme that works inward from $M_\star$ to $m=0.5M_\star$. Use the surface values of $R_\star$ and $L_\star$ from your MESA-Web run as boundary conditions. Plot the results (which?) as a function of $m$. Additionally, record the values of $r$, $P$, $L$, $T$ at the fitting point for the inward integration. Combine your plot with #4.



