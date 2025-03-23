def callStageTarget(all_stages, __prog_stage__, methodName, *value):
    if type(__prog_stage__) == type(False): return
    targetClass = all_stages[__prog_stage__]

    if hasattr(targetClass, methodName):
        getattr(targetClass, methodName)(*value)