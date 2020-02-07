## ML Types

[SLIDED 📑](https://d3c33hcgiwev3.cloudfront.net/_974fa7509d583eabb592839f9716fe25_Lecture1.pdf?Expires=1581120000&Signature=hVUnVKn7gh3xSqQeduUD8IiimmsUWXaCNTVXo91bp5Zy8I9LKVieNMAGmg8S6-LZiwfc7PxatxVEPjXQlG3UMNzye7iLiIr3370ClIPeQYrCJQLJ6OU-wbVrEcT0njE~iUKQpZbN6QjlJRAH6yIAqaM6yEiXnl602kRrdfEq1wc_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

#### Supervised learning
  - Test Data have lables
  - We are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.
  - Eg. Cancer detection based on Cancer data base

 1. **Regression**: predict results within a continuous output, meaning that we are trying to map input variables to some continuous function. 

 2. **Classification** we are instead trying to predict results in a discrete output. In other words, 
we are trying to map input variables into discrete categories eg true false.

#### Unsupervised learning
 - Test Data have no labels.
 - Automatically find Cluster, group & Pattern in input data
 
  **Clustering Algorithm:** Group customer in market segment, group friends in FB, group news.
  **Cocktail Party Algorithm:** Seperation of voice from music
  
  ------------------
  
### Training Set

Training Set is the Data that is feed to Leaning Algorithm. Learning function outputs a hypothesis function 

     X = input (Size of House)
     Y = output (Price)
    (X,Y) = Row in Training Set: single training example
    (Xi,Yi) = ith training example
     m = Number of Training Examples

> h maps X to Y, For a given size of House h will predict Price of House)

###How to represent h

#### Linear Regression with 1 Variable X OR Uni variable Linear Regression
   
Linear regression is method of finding a Continues Liner relationship between Y and X        

         hΘ(x) = Theta0+Theta1(X)x
         => y= y0 + mx
         where  Theta0 = y offset (Y0) 
                Theta1 = slope (m) form x Axis
                
- Theta0 = 0  means y= mx, pass through origin
- Theta1 = 0  means Horizontal Line parallel to X axis               
               
 #### Squared Error Cost Function:  
> - Goal of the algorithm is to choose Theta0 & Theta1 such that h(X) come close to Y . Minimize J(Theta0, Theta1)thus minimize Error                         
> - Squared error cost function work well for most regression programs

          J(Theta0, Theta1) =  1/2m(Sum((predicted-actual)**2))              
                            =  1/2m(Sum((h(xi)-y(i))**2)) 
                            =  1/2number of dataSet(Sum of Deviation from actual)**Squared to remove negative
            
  
  ![CostFunction](../../doc/assets/Goal.png)

                     
- Plot of  J(Theta0, Theta1) vs Theta1 is Parabola
- Plot of  J(Theta0, Theta1) vs Theta0,Theta1 is 3D Parabola    

   ![surfaceplot](../../doc/assets/surfaceplot.png)

### Contour Figure/ Plot 2D Plot of 3D  surface    

Contour plot is seeing surface plot passing through a horizontal 2D clip plane

- X axis in Contour Figure = Theta0 =  Y Intercept of Hypothesis in X,Y Plot
- Y axis in Contour Figure =  Slope =  Slope of Hypothesis Line  in X,Y Plot   
                            
  ![contourPlot](../../doc/assets/contour.png)
                   
-----

## Gradient Descent
> Algorithm used to reduce Cost function J(Theta0, Theta1) and other functionsJ (Theta0, Theta1,Theta1....Thetai) in ML, where
- Just like going down from a hill.
- Look around and find local minima and keep on going down repeat till find optimal solution.
- **Multiple minima  can be found**

 ![gradientDescent](../../doc/assets/gradient.png)
 
**Steps:** 
 - For feature index j=0,1, repeat until convergence
 
   ![descentFormula](../../doc/assets/descentFormula.png)
 - Simultaneous compute Theta(0), Theta (1) and store in temp values
 - Simultaneous Update  Theta(0), Theta (1)
 
 **Operator**

       := Assignment Operation eg a= a+1
       =  Truth Assertion eg a==a
       α  Learning Rate, How big steps we take down hill
       d(CostFn)/d(Theta) the sensitivity to change of the function value with respect to a change in its argument.


Alpha defines rate of Learning

 - Low Alpha: slow learning rate
 - Big Alpha: big steps can diverge from minima
       
![descentFormula](../../doc/assets/alpha.png)

Derivative term converge Theta towards its local minima. Derivative automatically takes small step when it starts to converge towards local minimal. Having a fixed alpha helps      
       
![descentFormula](../../doc/assets/Derivative.png)
        

