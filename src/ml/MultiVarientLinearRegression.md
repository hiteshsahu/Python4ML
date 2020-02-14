
## Introduction to MatLab:

> MatLab is the Language of Mathematical Computation

<img src = "../../assets/img/Matlab_Logo.png" width="100">
                                                       
- [Certificate MatLab 📑](../../assets/certificate/MatLab.pdf)
- [Study Notes MatLab 📑](../matlab/MathLab.md)

<div align="center">
  <a href="https://www.youtube.com/watch?v=ROonhizDeFQ"><img 
  src="https://img.youtube.com/vi/ROonhizDeFQ/0.jpg" 
  alt="Everything Is AWESOME" style="width:100%;"></a>
</div>

---

## Multi Variant Linear Regression

####Linear regression with multiple variables is also known as "multivariate linear regression".



Suppose y is function of multiple variables x then

>#### X<sub>column</sub><sup>(row)</sup> : X(i, j)
>  - **m**  = number of training example
> - **n**  =  number of feature in training example
> - **x<sup>(i)</sup>** = i<sup>th</sup> row in training example/ feature in example
> - **x<sub>j</sub><sup>(i)</sup>** = i<sup>th</sup> row , j<sup>th</sup> column in training example
>  

Linear Regression for Hypothesis for n features :   

> h<sub>Θ</sub>(x) =  Θ<sub>0</sub>X0 +Θ<sub>1</sub>X1 +Θ<sub>1</sub> X2+ Θ<sub>1</sub> X3+ ...Θ<sub>n</sub>Xn
> 
>Assume X0= 1 for convenience
>
> h<sub>Θ</sub>(x) =  Θ<sub>0</sub>X0 +Θ<sub>1</sub>X1 +Θ<sub>1</sub> X2+ Θ<sub>1</sub> X3+ ...Θ<sub>n</sub>Xn
> 
> ###h<sub>Θ</sub>(x) = Θ<sup>T</sup>X
>  #####Inner Product of RowVector0(1*n)* Column VectorX(n*1) = Scalar()1*1 Hypothesis

Notes:

-  Θ<sup>T</sup> is a 1 by (n+1) matrix and not an (n+1) by 1 matrix 
- **x<sub>0</sub><sup>(i)</sup>** =1  for matrix multiplication 

------------------

### Simple Linear Regression

#### Cost function: 
  ![CostFunction](../../assets/img/Goal.png)
  
       J(Theta0, Theta1) =  1/2m(Sum((predicted-actual)**2))              
                         =  1/2m(Sum((h(xi)-y(i))**2)) 
                         =  1/2number of dataSet(Sum of Deviation from actual)**Squared to remove negative
                

  
#### Gradient Descent:  
  **Steps:** 
 - For feature index j= 0,1, repeat until convergence
 
   ![descentFormula](../../assets/img/descentFormula.png)
 - Simultaneous compute Theta(0), Theta (1) and store in temp values
 - Simultaneous Update  Theta(0), Theta (1)
 
  
### Multi variant Linear Regression  

#### Cost Function

      J(Theta0, Theta1, Theta.....Thetam) =  1/2m(Sum((predicted-actual)**2))              
                             =  1/2m(Sum((h(xi)-y(i))**2)) 
                             =  1/2number of dataSet(Sum of Deviation from actual)**Squared to remove negative
                    
   
> J(Theta) =  1/2m(Sum((predicted-actual)**2))              
    
           
  ![CostFunction](../../assets/img/cost_fn_MultLR.png)


#### Gradient Descent:  

 **Steps:** 
 - For feature index j= 0,1,....n repeat until convergence
 
   ![descentFormula](../../assets/img/Descent_MVLR.png)
   
 - Simultaneous compute Theta(0), Theta (1), .... Theta (n)  and store in temp values
 - Simultaneous Update  Theta(0), Theta (1) .... Theta (n) 
 
-----

## Feature scaling

> Make sure feature are on same scale other wise contour will be skew elliptical(2000/5).
> Gradient descent on skew Eclipse  take long time to reach local minima


 > ##### xi = (xi--min(X))/(max(X)-min(X))


-  Try to get feature into -1<= xi<= 1. Long gape will not fully scaled. Idellay should be withing range -3 to +3.

Feature scaling is way to avoid creating skew ellipse:

   ![Feature scaling](../../assets/img/featureScaling.png)
   
### Mean Normalization   

Use mean and max range to normalize x values

 > ##### xi = (xi-Avg(X))/(max(X)-min(X))

   ![Mean Normalization](../../assets/img/meanScale.png)


 > ##### xi = (xi-Avg(X))/(max(X)-min(X))

### Debugging gradient descent using Learning Rate

>  plot the cost function, J(θ) over the number of iterations of gradient descent. If J(θ) ever increases, then you probably need to decrease α.


- If α is too small: slow convergence.

- If α is too large: ￼may not decrease on every iteration and thus may not converge.

   ![Mean Normalization](../../assets/img/learningRate.png)
   
--------------------------


## Polynomial Regression


> Sometimes by defining a new feature you might get a better Model that requires less computation

for example house price can defined by calculating area instead of creating 2 variable equation we can define one variable equation :

   ![creatingFeature](../../assets/img/creatingFeature.png)
   
- Sometimes prediction fits Polynomial equation instead of linear equation
- Scaling of feature becomes crucial in Polynomial Regression
- Some algo can choose feature to fit polynomial curves

![creatingFeature](../../assets/img/polynomial.png)

   
   
