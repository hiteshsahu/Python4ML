### [MatLab Operators](https://in.mathworks.com/help/matlab/operators-and-elementary-operations.html?s_tid=CRUX_lftnav)

- Arithmetic Operations
- Relational Operations
- Logical Operations
- Set Operations
- Bit-Wise Operations

## Arithmetic Operators

> #### +,-,*,/,^,()

 Order of Operation 
        
 > ####  ()>^>*,/>+-


###Notes: 

- A*b  multiply all elements of A with scalar b

- ### A^n
> A to the power n

- ### A.^n
> Multiply  Each Element of Vector by nth power

- #### A.*B
> Multiply Consecutive elements of Matrix A & B

- #### Matrix multiplication (A*B )
 
       A(mXn) is &  B(nXo) then A*B = C is (m*o) matrix 
       Where C(i,j)= A(i,k)*B(k,j).


- #### Dot product/ Inner Product of Vector(A.B)

       RowVector(1*n)* Column Vector(n*1) = Scalar()1*1
       
- #### Outer Product of Vector (A⊗B)

      Column Vector(n*1)*  RowVector(1*n) = Matrix(n*n)



<div align="center">
  <a href="https://www.youtube.com/watch?v=aRSkNpCSgWY"><img 
  src="https://img.youtube.com/vi/aRSkNpCSgWY/0.jpg" 
  alt="Everything Is AWESOME" style="width:100%;"></a>
</div>


- #### RightDivide (./)

 > A./B : divide all elements of A with corresponding elements of B 
>
 > A./b : divide all elements of A with vector b



- #### Left Divide (.\)

 > A.\B : divide all elements of B with corresponding elements of A 
>
 > b.\B : divide all elements of B with vector b
>
-------------
### [Relational Operators](https://in.mathworks.com/help/matlab/relational-operators.html)

> ### <, > , <=, >=, ==, ~=


- A>B -  return array of 1,0 by comparing each elements of A with B
 -A*b -  return array of 1,0 by comparing each elements in A & b
 
 #### Complex Numbers
 
-  \>, <, >= <=  compare only the real part
-  == , ~= test both real and imaginary parts.

#####  Undefined values: 

- Inf == other Inf values.
 -NaN ~= numeric value, including other NaN values.
- NaT ~= datetime value, including other NaT values.
- Undefined ~= any other categorical value, including other undefined elements.

-------------

### [Logical Operators](https://in.mathworks.com/help/matlab/logical-operations.html)

 -   Assert: true, false
 -   Logic : |, &, ~, xor
 -   Short Circuit: ||, &&, 
 -   Logical : islogical, logical
 -    find, all, any
 
 
         x = v1(v1<4 & v1>2)
         x = all value of v1 between 2 & 4


- L = logical(A) converts A into an array of logical values. 
- Any nonzero element of A is converted to logical 1 (true) and zeros are converted to logical 0 (false). 
- Complex values and NaNs cannot be converted to logical values and result in a conversion error.