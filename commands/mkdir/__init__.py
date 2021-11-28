def command(os, config, args, kwargs):
    if len(args) <= 0:
        print("mkdir: makes a directory")

    dir_name = args[0]
    os.mkdir(dir_name)