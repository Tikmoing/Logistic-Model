# Logistic Model

The Logistic model is an important example of bifurcation and chaos proposed by mathematical ecologist R. May in the British "Nature" in 1976.This code is for study the properties of this model.

This repository have only code file: [LogisticModel.py](https://github.com/Tikmoing/Logistic-Model/blob/main/LogisticModel.py),which has  5 functions.

+ ```python
  #logistic(mu,initialValue,times)
  ```

  This is a function which will return the iteration result while the model with the mu and initialValue for times iterating.

+ ```python
  #iterationDiagram(mu,initialValue,times)
  ```

  A function which draw a diagram to represent the iteration.For example 

  ```python
  iterationDiagram(3.6,0.6,100)
  ```

  ![iteration diagram](https://raw.githubusercontent.com/Tikmoing/Logistic-Model/main/png/iteration%20diagram.png)

+ ```python
  #bifurcationDiagram(muRange = [2.6,4],initialValue = 0.6,times = 250,stepLength = 0.00001,color = 'b')
  ```

  A function which draw the bifurcation diagram of this model. For example

  ```python
  bifurcationDiagram()
  ```

  ![bifurcation diagram](C:\Users\86177\Desktop\DataAnlysis\PydataFiles\chaos\bifurcation diagram.png)

+ ```python
  #lyapunovExponent(mu,initialValue,times)
  ```

  A function return the lyapunov exponent

+ ```python
  #lyapunovExponentDiagram(muRange=[3,4],initialValue = 0.6,times = 250 , stepLength = 0.00001 , color = 'b')
  ```

  A function which draw the diagram between mu and its lyapunov exponent. For example,

  ```python
  lyapunovExponentDiagram(color="#7bbfea")
  ```

  ![lyapunov exponent diagram](C:\Users\86177\Desktop\DataAnlysis\PydataFiles\chaos\lyapunov exponent diagram.png)

