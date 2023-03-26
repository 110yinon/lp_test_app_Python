demo.py:
    breaking the test's iterate in case of install test in failed

IqdvtCliHelpActivator.py:
    updates the IqdvtCliHelpActivator - now accepts isBinFolder and installLocation
    so then IqdvtCliHelpActivator ctor is now able to handle this args to determine the relevant install location
    also checks for the execution status of the calling 'iqdvt-cli.exe --help'
    