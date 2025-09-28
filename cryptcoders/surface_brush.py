#surface brush
from hub import light_matrix, motion_sensor,port
import runloop,motor,motor_pair
turn_speed=100
async def mv_(deg,speed):
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,deg,speed,speed)
    return
def turn_right(d):
    motion_sensor.reset_yaw(0)
    while motion_sensor.tilt_angles()[0]>=-d:
        motor_pair.move_tank(motor_pair.PAIR_1,turn_speed,-turn_speed)
    motor_pair.stop(motor_pair.PAIR_1)
    return
def turn_left(d):
    motion_sensor.reset_yaw(0)
    while motion_sensor.tilt_angles()[0]>=d:
        motor_pair.move_tank(motor_pair.PAIR_1,-turn_speed,turn_speed)
    motor_pair.stop(motor_pair.PAIR_1)
    return
async def move_arm_degrees(deg,vel):
    await motor.run_for_degrees(port.C,deg,vel)
    return
async def move_arm_degrees_right(deg,vel):
    await motor.run_for_degrees(port.D,deg,vel)
    return

async def main():
    # write your code here
    motor_pair.pair(motor_pair.PAIR_1,port.A,port.F)
    turn_speed=100
    await mv_(1600,-1000)
    await mv_(1450,1000)
    turn_left(300)
    #await move_arm_degrees_right(1700,1200) #moves it down
    await mv_(650,-1000)
    turn_right(367)
    await mv_(-950,1000)
    turn_left(200)
    await mv_(-100,500)
    await move_arm_degrees(-1700,-1200)
    await move_arm_degrees(1900,-1500)
    #await mv_(-50,100)
    #await move_arm_degrees(950,-900)
    #await mv_(400,-500)
    #await move_arm_degrees(950,900)
    #await mv_(600,500)
runloop.run(main())
