import random

from psychopy import core, event

import Code.globals as glb
from Code.markEvent import markEvent
import Code.stimuli as stim

def run_experiment():
    textStimuli = ...
    with open('Files/stimuli.txt') as stimuliFile:
        textStimuli = [line.strip() for line in stimuliFile]
        random.shuffle(textStimuli)

    phdTime = glb.PARAMETERS.timing['photodiode']
    stimTime = glb.PARAMETERS.timing['stimuliDurS'] - phdTime
    interTime = glb.PARAMETERS.timing['intervalDurS'] - phdTime
    

    markEvent("taskStart")
    for idx, textStimulus in enumerate(textStimuli):
        markEvent("stimulusStart", idx+1)
        stim.draw_text(textStimulus)
        stim.PHOTODIODE.draw()
        glb.UI_WIN.flip()
        core.wait(phdTime)

        stim.draw_text(textStimulus)
        glb.UI_WIN.flip()
        willQuit = event.waitKeys(keyList = ['escape'], maxWait=stimTime)
        print(willQuit)
        if willQuit != None:
            markEvent("taskAbort")
            break
        
        stim.PHOTODIODE.draw()
        glb.UI_WIN.flip()
        core.wait(phdTime)

        glb.UI_WIN.flip()
        core.wait(interTime)

    markEvent("taskStop")




        


