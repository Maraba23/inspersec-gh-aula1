import sys
import pyMeow as pm
import keyboard

try:
    proc = pm.open_process("ac_client.exe")
    base = pm.get_module(proc, "ac_client.exe")["base"]
    print(f"Base Address: {hex(base)}")
except Exception as e:
    sys.exit(e)

class Pointer:
    local_player = 0 # na aula vamos pegar nosso local player

class Offsets:
    pass

class Colors:
    cyan = pm.get_color("cyan")
    orange = pm.get_color("orange")
    white = pm.get_color("white")
    black = pm.get_color("black")

def main():
    pm.overlay_init(target="AssaultCube", fps=144, trackTarget=True)
    while pm.overlay_loop():
        pm.begin_drawing()
        pm.draw_fps(10, 10)

        # Aqui vamos escrever nosso hack

        pm.end_drawing()



if __name__ == "__main__":
    main()