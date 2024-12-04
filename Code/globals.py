from psychopy import core, prefs, visual

from Code.Classes.Parameters import Parameters 

# Set hardware preferences
prefs.hardware['audioLib'] = ['sounddevice', 'pygame']
prefs.hardware['audioLatencyMode'] = '3'

# Load parameters globally
PARAMETERS = Parameters()

if PARAMETERS.ID['expEnv'] == "BCM-EMU":
    import PythonToNSP.BlackRockUtils as bru

    emuNum, subjID, log_file= bru.get_next_log_entry()
    PARAMETERS.ID.update({'emuRunNum': emuNum})
    PARAMETERS.ID.update({'name': subjID})
    emuSaveName = bru.make_EmuSaveName(emuNum, subjID, PARAMETERS.exp['name'])
    PARAMETERS.ID.update({'emuSaveName': emuSaveName})


PARAMETERS.generate_output_dest()
PARAMETERS.save()

ABS_CLOCK = core.Clock()
REL_CLOCK = core.Clock()

# Global UI Window creation
# UI_WIN = visual.Window(size=PARAMETERS.window['size'], fullscr=PARAMETERS.screen['fullscr'], screen = PARAMETERS.screen['number'],
UI_WIN = visual.Window(fullscr=PARAMETERS.screen['fullscr'], screen = PARAMETERS.screen['number'],
                       units=PARAMETERS.window['units'], color=PARAMETERS.window['bgColor'], colorSpace='rgb255')

PARAMETERS.window.update({'size': UI_WIN.size})

EVENTS = []
ABORT = False

def abort():
    global ABORT
    ABORT = True