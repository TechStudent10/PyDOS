def command(os, config, args, kwargs):
    if len(args) <= 0:
        print("cd: changes directory")
    
    new_path = args[0]
    if new_path == '..':
        if len(config['path_structure']) != 1:
            config['path_structure'].pop()
    else:
        if new_path in os.listdir():
            if os.path.isdir(new_path):
                os.chdir(new_path)
                config['path_structure'].append(new_path)
            else:
                print("Path is not a directory")
