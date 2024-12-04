import Code.globals as glb

if glb.PARAMETERS.ID.get('expEnv') == "BCM-EMU":
    import PythonToNSP.BlackRockUtils as bru

def markEvent(EventType: str, *args):
    # Get the event time using the global clock
    eventTime = glb.ABS_CLOCK.getTime()
    
    # Define event names based on EventType and additional arguments
    eventName = ""
    match EventType:
        case "taskStart":
            eventName = "Task Started"
        case "taskStop":
            eventName = "Task Ended Successfully"
        case "taskAbort":
            print("ABORTING TASK")
            eventName = "Task Aborted"

        case "stimulusStart":
            eventName = f"Stimulus {args[0]} Started"
        case "stimulusEnd":
            eventName = f"Stimulus {args[0]} Ended"
        case "intervalStart":
            eventName = f"Interval {args[0]} Started"
        case "intervalEnd":
            eventName = f"Interval {args[0]} Ended"

        case _:
            eventName = "UNKNOWN EVENT"

    glb.EVENTS.append((eventName, eventTime))

    # Additional environment-specific handling if needed
    if glb.PARAMETERS.ID.get('expEnv') == "BCM-EMU":
        match EventType:
            case "taskStart":
                bru.task_comment('start', glb.PARAMETERS.ID['emuSaveName'])
            case "taskStop":
                bru.task_comment('stop', glb.PARAMETERS.ID['emuSaveName'])
            case "taskAbort":
                bru.task_comment('kill', glb.PARAMETERS.ID['emuSaveName'])
            case _:
                bru.task_comment(eventName, glb.PARAMETERS.ID['emuSaveName'])