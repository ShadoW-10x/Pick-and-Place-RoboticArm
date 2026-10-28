import pybullet as p, pybullet_data, time
p.connect(p.GUI)##Starts the simulator and opens the 3d window
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.loadURDF("plane.urdf")
p.loadURDF("r2d2.urdf", [0, 0, 2])
while True:
    p.stepSimulation()
    time.sleep(1/240)