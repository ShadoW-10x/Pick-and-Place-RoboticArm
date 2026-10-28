import pybullet as p,pybullet_data,time

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")
arm=p.loadURDF(r"C:\armproject\arm6dof.urdf",useFixedBase=True)

sliders={}
for i in range(p.getNumJoints(arm)):
    info=p.getJointInfo(arm,i)
    if info[2]!=p.JOINT_FIXED:
        name=info[1].decode()
        sliders[i]=p.addUserDebugParameter(name,info[8],info[9],0)
while True:
    for i,s in sliders.items():
        p.resetJointState(arm,i,p.readUserDebugParameter(s))
    time.sleep(1/60)