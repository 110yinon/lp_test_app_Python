config.runner.json:
    change the 'isBinFolder' value to true (cli flow been checked on CL-8)
    rename to 'expectPass' from 'expect'

IqdvtCliFlowActivator.py:
    now gets isBinFolder and installLocation
    staion and flow now gets relative path to 'flows' and 'stations' folders
    rename to IqdvtCliFlowActivator.Execute() from IqdvtCliFlowActivator.ExecuteReturnOutput()
    checks the status of execution for failed
    prints the tracback in case of exception
    