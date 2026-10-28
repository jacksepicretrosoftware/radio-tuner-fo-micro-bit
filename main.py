def on_gesture_screen_up():
    serial.write_line("LOCAL_FM")
    basic.show_string("RADIO HARTLEPOOL 102.4")
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_screen_down():
    serial.write_line("LOCAL_AM")
    basic.show_string("TALK SPORT AM")
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

basic.show_string("HARTLEPOOL RADIO")