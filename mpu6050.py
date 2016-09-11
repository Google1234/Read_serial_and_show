Gravity=9.78
x_AccOff=-0.214893
x_GyroOff=-26.320611
y_AccOff=0.063274
y_GyroOff=-1.687023
z_AccOff=-0.448887
z_GyroOff=-1.679389
def data_decode(string):
    #
    data=[ord(c) for c in string]
    x_AccOut=(data[0]<<8)+data[1]
    y_AccOut=(data[2]<<8)+data[3]
    z_AccOut=(data[4]<<8)+data[5]
    x_GyroOut=(data[6]<<8)+data[7]
    y_GyroOut=(data[8]<<8)+data[9]
    z_GyroOut=(data[10]<<8)+data[11]
    #
    x_Acc=(x_AccOut)/16384.0*Gravity+x_AccOff
    x_Gyro=(x_GyroOut)/131.0+x_GyroOff
    y_Acc=(y_AccOut)/16384.0*Gravity+y_AccOff
    y_Gyro=(y_GyroOut)/131.0+y_GyroOff
    z_Acc=(z_AccOut)/16384.0*Gravity+z_AccOff
    z_Gyro=(z_GyroOut)/131.0+z_GyroOff
    return [x_Acc,y_Acc,z_Acc,x_Gyro,y_Gyro,z_Gyro]