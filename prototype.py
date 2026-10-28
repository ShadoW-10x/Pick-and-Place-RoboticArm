import pybullet as p, pybullet_data, time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
arm = p.loadURDF(r"C:\armproject\arm6dof_v2.urdf", useFixedBase=True)

sliders = {}
gripper_idx = None
follower_idx = None

for i in range(p.getNumJoints(arm)):
    info = p.getJointInfo(arm, i)
    if info[2] == p.JOINT_FIXED:
        continue
    name = info[1].decode()

    if name == "j6_gripper_follower":
        follower_idx = i          # no slider for this one
        continue
    if name == "j6_gripper":
        gripper_idx = i

    sliders[i] = p.addUserDebugParameter(name, info[8], info[9], 0)

while True:
    for i, s in sliders.items():
        value = p.readUserDebugParameter(s)
        p.resetJointState(arm, i, value)
        if i == gripper_idx:
            p.resetJointState(arm, follower_idx, value)  # follower copies gripper
    time.sleep(1 / 60)