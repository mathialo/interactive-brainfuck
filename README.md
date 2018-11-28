# Interactive BrainFuck
An interactive BrainFuck interpreter written in Bython. Why not?

After installation, you run an interactive session with the `ibf` command:
```
$ ibf
> +[------->++<]>-.------------.--[--->+<]>--.+.+++[->+++<]>.+++++++++++++.[-->+++++<]>+++.[-->+++++++<]>.++.---.------------.-[--->+<]>----.+++[->+++<]>++.--[--->+<]>--.+.-----------.+++++.-------------.--[--->+<]>-.-----.+++.>++++++++++.
master procrastinator
```

Everything you input is interpreted as BrainFuck code, except for the following
reserved keywords:

| Command    | Description                                        |
|------------|----------------------------------------------------|
| tape       | Prints the current status of the tape (data cells) |
| pos        | Prints the current position on the tape            |
| quit       | Quits the session                                  |
| run <file> | Run code from a file                               |


You can also run prewritten BrainFuck code, either as a standalone program, or
in an interactive session:
```
$ ibf test.bf
Hello World!
$ ibf
> run test.bf
Hello World!
```
The `run` command always runs programs _inline_, ie the code will not get an 
empty tape to begin with, and it will leave the tape mangled-up:
```
> tape
 0 1  2   3  4  5  6 7 8
 0 0 72 100 87 33 10 0 0
```