import os
os.environ['TCL_LIBRARY'] = "C:\\Program Files (x86)\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files (x86)\\Python35-32\\tcl\\tk8.6"
import cx_Freeze


executables = [cx_Freeze.Executable("trace.py")]

cx_Freeze.setup(
    name="trace car",
    options={"build_exe": {"packages":["pygame"],"include_files":['racecar_trans_small.png', 'racecar_crash_trans_small.png', 'racecar_trans_small_move.png', 'myIcon.png', 'edge_left.png', 'edge_right.png', "crash_sound.wav", "button_sound.wav", 'guiji_jaychou.mp3']}},                      
    executables = executables

    )
