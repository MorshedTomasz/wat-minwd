# PuLP

PuLP is an LP modeler written in Python. A few different solvers can be used in PuLP.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PuLP.

```bash
$ pip install pulp
```

## Requriments
PuLP requires Python 2.6 or above.

## Example
Import needed packages.
```python
from pulp import *
```

Create problem using LpProblem() and specifies method.
```python
prob = LpProblem("problem", LpMinimize)
```


Create variables using LPVariable(). This creates variable 'x' which is in range from 0 to 3.
``` python
x = LpVariable("x", 0, 3)
```

Combine variables to create expressions and constraints, then add them to the problem.

``` python
prob += x + y <= 2
```

Solve with the default included solver.
``` python
prob.solve()
```

List of another solvers is available in documentation.
Example:

``` python
prob.solve(GLPK(msg = 0))
```


Display the status of the solution.

``` python
 LpStatus[status]
 'Optimal'
```
You can get the value of the variables using value(). ex:
``` python
  value(x)
 2.0
```


## Running the example
To run example open termina/cmd/powershell in folder where file example.py exist and write:
``` bash 
$ python example.py
```


## Documentation
Documentation is found on [official website](https://pythonhosted.org/PuLP/).

