## MatLab (MATrix LABoratory)

<img src = ../../assets/img/Matlab_Logo.png" width="50">

> doc fn = document for function n

#### Precision of WOrkSpace

> format long  // 12 + decimal places
>
> format short // Upto 4 decimal places

#### Variable:

- starts with alphabets
- contain a_z, A_Z , 0..9, & _
- MatLab automatically show suggestion for incorrect variables
- Can see data value by entering variable name

####  Saving & Loading Variables

Save all Variables in MAT File
> save \<filename\>.mat 

Save Single variable in MAT file
> save \<filename>.mat \<variableName>
 
Load Saved Variables
>load \<filename>.mat    
 
Load Single Saved Variables
>load \<filename>.mat \<variableName>

 Empty WorkSpace 
 > clear 


#### Creating Arrays & Matrix
    x = [7 9]      // row array or row vector [element  element]
    x= x'          // Transpose Into column vector
    
    x = 1:4          // Shortcut create Row Vector [1,2,3,4]
    x= 1: 0.5 :5     // shortcut create Row Vector 1 to 5 step 0.5 [1,1.5,2,2.5, 3,3.5,4,4.5 5]
    x= (1: 0.5 : 5)' // shortcut create Column Vector 1 to 5 step 0.5 

    x = linspace(start,end,space)   // equidistance  rowvector 
    x = linspace(start,end,space)'  //  equidistance columnn vector

    x = [7,9]       // row array [element , element]
    x = [7;9]       // column array [element ; element]
    x = [4,5 ; 7,9] // 2d Matrix [ROW; ROW]
    
    x = rand(n)    // Generate  nxn matrix with random number
    x = rand(n,m)  // Generate  nxm matrix with random number
    x = zeros(n,m) // Generate  nXm matrix with zero elements
    
##   Reading 

- Indexing starts with 1

         size(A)                // size of matrix
         [dr, dc] = size(A)     // Size in dr,dc
         [vMax, ivMax]= max(A)   // Max Value and its Index
        
         A(i)     // ith element of Vector
         A(n:m)   // All elements from n to m index of Vector

         A(i,j)    // ith row, jth column of Matrix 
         A(end,j)  // last row j column 
         A(n, :)  // Get all elements of nth Row
         A(:, n)   // Get all elements of nth Column
         A(:, end-1:end) // all elements of last 2 column
         

## Update

     A(i) = b      // modify A(i) to b
     A(i,j) = b    // modify A(i,j) to b 

     A + b        // Add Scaler b to all elements of Matrix A
     A / b        // Divide Scaler b to all elements of Matrix A
     fn(A)        // Math fn on all elements of Matrix A eg sqrt
     
      A + B        // Add A+ B
      A.*B         // Multiply A.*B
