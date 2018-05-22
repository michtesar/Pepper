from robot import *

pepper = Pepper("10.37.1.227")

pepper.set_volume(50)
answer = pepper.ask_wikipedia()
pepper.say(answer)

"""
print("[PIPELINE]: Setting the robot")
pepper.set_awareness(False)
pepper.set_volume(50)
pepper.set_security_distance(0.01)
pepper.tablet_show_web("https://www.ciirc.cvut.cz/cs/")
pepper.start_animation("Hey_1")

print("[PIPELINE]: Pick a volunteer")
pepper.pick_a_volunteer()
pepper.say("Look at me please")
pepper.get_face_properties()

print("[PIPELINE]: Play sound")
pepper.tablet_show_image("https://goo.gl/4Xq6Bc")
"""
