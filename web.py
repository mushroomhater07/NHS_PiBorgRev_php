# import PicoBorgRev3 as PicoBorgRev
import sys

# voltageIn = 12.0
# voltageOut = 6.0

# if voltageOut > voltageIn:
#     maxPower = 1.0
# else:
#     maxPower = voltageOut / float(voltageIn)
# PicoBorgRev.ScanForPicoBorgReverse()
# PBR = PicoBorgRev.PicoBorgRev()
# PBR.Init()
# PBR.ResetEpo()
# PBR.MotorsOff()

# print (PBR.busNumber)        # Reading parameters (after Init)           # Shows which I²C bus the board is connected on
# print (PBR.foundChip)                  # See if the board is found / not found

# website  
def for1():
    print("forward")
    # PBR.SetMotor1(+maxPower)
    # PBR.SetMotor2(+maxPower)

def back():
    print("backward")
    # PBR.SetMotor1(-maxPower)
    # PBR.SetMotor2(-maxPower)

def right():
    print("clockwise")
    # PBR.SetMotor1(+maxPower)
    # PBR.SetMotor2(-maxPower)

def left():
    print("anti-clockwise")
    # PBR.SetMotor1(-maxPower)
    # PBR.SetMotor2(+maxPower)

def stop():
    print("stop")
    # PBR.MotorsOff()

# call function
locals()[sys.argv[1]]()
#eval(sys.argv[1] + '()')
