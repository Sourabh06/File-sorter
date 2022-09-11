# Year wise sorter

If you want to sort files based on year given the file name has only one occurance of year and is easily identifiable(delimiter present)

### Note:
I've used this to sort only pdf files, hence the "*.pdf" in for loop

## Run
``` bash yrSorter.sh ``` in your desired directory.

## Walkthrough:

``` ${f//[^0-9]/} ``` - extracts the year
``` [ ! -d "$subdir" ] ``` - True if file doesn't exist and is a directory


## References

- [man bash](https://man7.org/linux/man-pages/man1/bash.1.html)
- [extract numbers from file name](https://stackoverflow.com/a/13248193). Also check BASH_REMATCH