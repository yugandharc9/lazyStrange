import platform,os,getpass

if platform.system()=='Linux':
 PATH=os.path.join('/home',getpass.getuser(),'watcher/')
 DOCPATH=os.path.join('/home',getpass.getuser(),'docs/')
 INSTALLPATH=os.path.join('/home',getpass.getuser(),'watchdog','lazyStrange/')
 SAFEPATH=os.path.join('/home',getpass.getuser(),'quarantine/')


if platform.system()=='Windows':
 PATH=os.path.join('D:','watcher')
 DOCPATH=os.path.join('D:','docs')
 INSTALLPATH=os.path.join('C:','watchdog','lazyStrange')
 SAFEPATH=os.path.join('D:','quarantine')


