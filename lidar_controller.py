from controller import Robot, Lidar

# Inisialisasi robot
robot = Robot()
time_step = int(robot.getBasicTimeStep())

# Inisialisasi sensor LIDAR
lidar = robot.getDevice("lidar")
lidar.enable(time_step)
lidar.enablePointCloud()

# Motor penggerak robot
left_motor = robot.getDevice("left_motor")
right_motor = robot.getDevice("right_motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Fungsi utama
while robot.step(time_step) != -1:
    # Membaca data dari LIDAR
    lidar_data = lidar.getRangeImage()

    # Deteksi rintangan di depan
    obstacle_detected = False
    for i in range(len(lidar_data) // 3):  # Fokus ke data depan LIDAR
        if lidar_data[i] < 1.0:  # Jika jarak terlalu dekat (< 1 meter)
            obstacle_detected = True
            break

    # Mengendalikan robot berdasarkan deteksi rintangan
    if obstacle_detected:
        left_motor.setVelocity(-2.0)  # Mundur
        right_motor.setVelocity(-2.0)
    else:
        left_motor.setVelocity(2.0)  # Maju
        right_motor.setVelocity(2.0)
