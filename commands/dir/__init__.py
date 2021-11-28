def command(os, config, args, kwargs):
    if len(args) == 0:
        scan_dir = '.'
    else:
        scan_dir = args[0]
    
    for path in os.listdir(scan_dir):
        isDir = os.path.isdir(path)

        print('"' + path + '":', 'File' if not isDir else 'Directory')