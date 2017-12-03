# racial-segregation-schelling
Computer Simulation for the schelling model

Complex Network course
Group 8
Joao Rodrigues 78672
Pedro Ascensao 78961

## Dependencies
It is necessary to have installed the folowing packages: numpy, networkX and matplotlib

```
python -m pip install --user numpy matplotlib networkx
``` 

## Running
The following command runs the project:

 ```shell
python main.py
```

You can have additional arguments when running. Running the flag -h produces the following output:

```shell
python main.py -h 

usage: main.py [-h] [-tp TYPE] [-thold THRESHOLD] [-o ONES] [-t TWOS]
               [-d DIMENSION]

Computer simulation of the Schelling model

optional arguments:
  -h, --help            show this help message and exit
  -tp TYPE, --type TYPE
                        Type of the representation of the model (either matrix
                        or scalefree)
  -thold THRESHOLD, --threshold THRESHOLD
                        Threshold desired
  -o ONES, --ones ONES  Percentage of agents belonging to race one
  -t TWOS, --twos TWOS  Percentage of agents belonging to race two
  -d DIMENSION, --dimension DIMENSION
                        Percentage of agents belonging to race two
```

The defaults are : type=matrix, threshold=0.3, ones=0.4, twos=0.4, dimension=50. 
For either the matrix or the graph, the number of entries or nodes is given by dimension * dimension.
The percentages and the threshold must be between 0 and 1. 
