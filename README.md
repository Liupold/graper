# graper
Tired of plotting graphs by hand? 😥 (Forced by teachers?)

Relax, There is a Better way. 😉

~~if there is a will there is a way~~ (only if you are lazy enough).

## How graper works ? (Introduction)

Install from pip `pip install graper` (😃soon.).
* Well before we start we need to make sure these are installed.
  - [numpy](https://pypi.org/project/numpy/)
  - [click](https://pypi.org/project/click/)
  - [PyYAML](https://pypi.org/project/PyYAML/)
  - [Pillow](https://pypi.org/project/Pillow/)

  Done? Good!
* Copy the `graper`folder to your work folder. (you can try out the example).
  - copy `graper` into `example`.

* `graper` Forces you to be organized.(🧹).
  - each pair of (x, y) will have a separate file. This will be ref as `datafile`.
  - For example, example has three data files `data1.csv`,`data2.txt`,`data3.dat`
  - yes we can have different type of files. 😍
  - each file must have either two rows or two columns.

* writing the `YAML`.
  - create a new `<name>.yaml` file or use the one provided in example.
  - Yaml is broken down into three parts `info`, `plots`, `graphs`.

  An example is available in

        example/example.yaml
* once the yaml file is written your work is done.
* you can do the magic using the following command.
        replace `example.yaml` with your file name. make sure you have `graper `
        folder is coppied where your example.yaml file is present.

        python3 -m grapher example.yaml

* If done correctly you will have your graph ready. Just print them out and done!.
* check `example` for sample graph output! cheers.
