def command(os, config, args, kwargs):
    if len(args) <= 0:
        print("del: deletes stuff i guess")
    
    path = args[0]
    if path in os.listdir():
        if input(f'Are you sure you want to delete {path} (y/n) ').lower() == 'y':
            if os.path.isdir(path):
                os.rmdir(path)
            else:
                os.remove(path)
