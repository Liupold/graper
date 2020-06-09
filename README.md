# graper
Tired of plotting graphs by hand? 😥 (Forced by teachers?)

Relax, There is a Better way. 😉

~~if there is a will there is a way~~ (only if you are lazy enough).

## How graper works ? (Introduction)

~~Install from pip `pip install graper`~~ (😫 Not there yet).
* Well before we start we need to make sure these are installed.
  - [numpy](https://pypi.org/project/numpy/)
  - [click](https://pypi.org/project/click/)
  - [PyYAML](https://pypi.org/project/PyYAML/)
  - [Pillow](https://pypi.org/project/Pillow/)

  Done? Good!
* Copy the `graper`folder to your work folder. (you can try out the example).
  - copy `graper` into `example`.

* Grapher Forces you to be organized.(🧹).
  - each pair of (x, y) will have a seprate file. This will be ref as `datafile`.
  - For example, example has three data files `data1.csv`,`data2.txt`,`data3.dat`
  - yes we can have different type of files. 😍
  - each file must have either two rows or two columns.

* writing the `YAML`.
  - create a new `<name>.yaml` file or use the one provided in example.
  - Yaml is broken down into three parts `info`, `plots`, `graphs`.

  ```yaml
  info:
        # This is a comment
        # here we will provide the info for our project.
        # This section is currently not being used for anything.
        name: Hello Graper
        about: Just a simple intro
  plots:
        # Here we will define data for plots
        x_linear:
        # ^- lables can be anything you want.
                datafile: data1.csv # file name relative to the yaml file.
                delimiter: ","  # value seprator
        x_square:
        # ^- labels will be refered in graph section.
                datafile: data2.txt # file name relative to the yaml file.
                delimiter: "  "  # "" are important.
        x_cube:
        # ^- labels will be refered in graph section.
                datafile: data3.dat # This files are available in example dir, take a look.
                delimiter: "-"  # "" are important.
  graphs:
        # Here we will define how to draw the graphs.
        graph1:
        # ^- lables can be anything you want.
                # telling which type of graph we want. (mm is only available for now)
                type: mm
                # ploting our plots (this must be defined in plots section above)
                plots: x_linear, x_square
                # telling where to save.
                save: graph1.png

                # this options bellow are optional
                color: black #this will make all plot points black.
                # we might want to make out graph beautiful using empty space around
                # We can specify that using padding.
                padding_bottom: 20 # 20 small div from bottom
                padding_top: 10 # 10 small div from top will be empty
                #defaults: left=10,right=0,top=0,bottom=10

        graph2:
                # telling which type of graph we want. (mm is only available for now)
                type: mm
                # ploting our plots (this must be defined in plots section above)
                plots: x_linear, x_cube
                # telling where to save.
                save: graph2.png

                # this options bellow are optional
                color: red, purple #this will make 1st plot red and second plot purple
                # hex code will also work.

                # we might want to make out graph beautiful using empty space around
                # We can specify that using padding.
                padding_bottom: 20 # 20 small div from bottom
                #defaults: left=10,right=0,top=0,bottom=10

        graph2:
                # telling which type of graph we want. (mm is only available for now)
                type: mm
                # ploting our plots (this must be defined in plots section above)
                plots: x_linear, x_cube, x_square
                # telling where to save.
                save: graph3.png

                # this will randomly generate color for the plots.
  ```
  - 😭 so big! (Not really most of the file is comment a version wihout comments is
  avilable in

        example/example.yaml
* once the yaml file is writen your work is done.
* you can do the magic using the following command.
        replace `example.yaml` with your file name. make sure you have `graper `
        folder is coppied where your example.yaml file is present.

        python3 -m grapher example.yaml

* If done correctly you will have your graph ready. Just print them out and done!.
* check `example` for sample graph output! cheers.
