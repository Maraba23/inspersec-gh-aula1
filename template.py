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
    local_player = 0x18AC00

class Offsets:
    health = 0xEC
    current_ammo = 0x140

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

        local_player_ptr = pm.r_int(proc, base + Pointer.local_player)
        health_ptr = pm.r_int(proc, local_player_ptr + Offsets.health)
        current_ammo_ptr = pm.r_int(proc, local_player_ptr + Offsets.current_ammo)
        if (health_ptr < 100):
            pm.w_int(proc, local_player_ptr + Offsets.health, 100)
        if (current_ammo_ptr < 30):
            pm.w_int(proc, local_player_ptr + Offsets.current_ammo, 30)

        pm.end_drawing()



if __name__ == "__main__":
    main()