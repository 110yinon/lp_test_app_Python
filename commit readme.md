demo.py:
    start reading from the config.runner.json file in demo.py file
    parse the isBinFolder and installLocation and pass them to IqdvtInstallActivator
    installLocation key is now optional in the config.runner.json
    means that demo is claver enough to set a default value path if it not exist

executions folder:
    added 'executions' folder that contains the relevant exe installation files

ExecutableActivator, IqdvtInstallActivator:
added try/except to IqdvtInstallActivator and ExecutableActivator and prints
the traceback if exception if raised

IqdvtInstallActivator, IqdvtUninstallActivator:
    checks for result value from ExecutableActivator in IqdvtInstallActivator and IqdvtUninstallActivator

ExecutableActivator:
    changes the self.Execute to ExecutableActivator.Execute(self) if order to fix potential bug
    if calls the Execute from derived method with the same Execute name