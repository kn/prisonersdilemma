# Prisoner's Dilemma Simulator

This script simulates Prisoner's Dilemma game described in [The Evolution of Cooperation (1981), R Axelrod, WD Hamilton](http://science.sciencemag.org/content/211/4489/1390.short).

## Usage

```
python main.py <file path to population file> <number of iteration>
```

For example:
```
python main.py data/mix.csv 10
```

## Population File

You can find sample population files in `data` directory.

Population file is a CSV file that lists strategy and its population size.
Listed strategies have to be implemented in `strategies.py` file.
```
<strategy one>,<population size>
...
```
