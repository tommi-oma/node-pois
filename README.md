* Node-pois

    The name is from Finnish, slightly incorrect in that it means "*remove node*" while it actually removes `node_modules`.

A simple Python code to get rid of `node_modules` directories from the filesystem. Can remove multiple starting from any given directory, it does a recursive search to all sub directories starting from the one given. 

```
$ python3 nodepois.py --help
usage: nodepois.py [-h] [-q] DIR

Delete node_modules.

positional arguments:
  DIR          root directory for the walk

optional arguments:
  -h, --help   show this help message and exit
  -q, --quiet  quiet mode, default interactive
```

So for example `python3 nodepois.py -q ~/codes/js/react` would remove all the `node_module` directories starting from the given one.

Obviously you can modify the code to make it more to your liking if need be.