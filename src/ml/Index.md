> #### AI is the field of study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals

##### ML is the study of computer algorithms that improve automatically through experience.

Older definition 
>  ####"the field of study that gives computers the ability to learn without being explicitly programmed." 
>-Arthur Samuel

Modern definition: 
 
>  ####"A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."
> Tom Mitchell

Example: playing checkers.

E = the experience of playing many games of checkers

T = the task of playing checkers.

P = the probability that the program will win the next game.

------------

## Learning Progress

- [Week1: Linear Regression & Matrix](./Basics.md)


## Useful Libs

    python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

#### Basic: 
- **numpy**:  numerical computation. Defines the numerical array & matrix types and basic operations on them.

- **scipy**:   numerical algorithms for signal processing, optimization, statistics etc for Scientific use
- **matplotlib**: graph plotting in 2d & 3D

#### Data and computation:

- **scikit-learn**  :is a collection of algorithms and tools for machine learning.- **ipython**

- **scikit-image** : is a collection of algorithms for image processing.
- **SymPy**  :for symbolic mathematics and computer algebra.
- **pandas** : providing high-performance, easy-to-use data structures.
- **h5py and PyTables**  can both access data stored in the HDF5 format.


#### Productivity and high-performance computing:

- **IPython**, a rich interactive interface, letting you quickly process data and test ideas.

 - **The Jupyter notebook** provides IPython functionality and more in your web browser, allowing you to document your computation in an easily reproducible form.

 - **Cython** extends Python syntax so that you can conveniently build C extensions, either to speed up critical code or to integrate with C/C++ libraries.

- **Dask, Joblib or IPyParallel** for distributed processing with a focus on numeric data.

#### Quality assurance:

- **nose**, a framework for testing Python code, being phased out in preference for pytest. 
- **numpydoc**, a standard and library for documenting Scientific Python libraries.