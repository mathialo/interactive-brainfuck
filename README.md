# Interactive BrainFuck
An interactive BrainFuck interpreter written in Bython. Why not?

To install from source, you must first build the Bython source into a Python package:
``` bash
$ make build
```
Then, you move to the `python` folder, and run the setup script:
``` bash
$ cd python
$ sudo -H pip3 install .
```

After installation, you run an interactive session with the `ibf` command:
```
$ ibf 
Interactive BrainFuck - ibf v0.1

ibf is licensed under the permissive MIT license. Full license and
copyright information is available at the project's GitHub repository.

[Input] +[------->++<]>-.------------.--[--->+<]>--.+.+++[->+++<]>.+++++++++++++.[-->+++++<]>+++.[-->+++++++<]>.++.---.------------.-[--->+<]>----.+++[->+++<]>++.--[--->+<]>--.+.-----------.+++++.-------------.--[--->+<]>-.-----.+++.>++++++++++.
master procrastinator
```

Everything you input is interpreted as BrainFuck code, except for the following
reserved keywords:

| Command    | Description                                                                       |
|------------|-----------------------------------------------------------------------------------|
| tape       | Prints the current status of the tape (data cells), with the current cell in bold |
| pos        | Prints the current position on the tape                                           |
| quit       | Quits the session                                                                 |
| run <file> | Run code from a file                                                              |


You can also run prewritten BrainFuck code, either as a standalone program, or
in an interactive session:
```
$ ibf test.bf
Hello World!
$ ibf 
Interactive BrainFuck - ibf v0.1

ibf is licensed under the permissive MIT license. Full license and
copyright information is available at the project's GitHub repository.

[Input] run test.bf
Hello World!
```

The `run` command always runs programs _inline_, ie the code is run on the
current tape and with the current tape position as starting position. Thus,
after running a program you can inspect the final state of the tape:

```
[Input] tape
 0 1  2   3  4  5  6 7 8
 0 0 72 100 87 33 10 0 0
```


For more help, type `ibf -h` or view the manual page by running `man ibf`.