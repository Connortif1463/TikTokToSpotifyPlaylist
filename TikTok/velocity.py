get_library('https://cdn.rawgit.com/PERLMSU/physutil/master/js/physutil.js')
 
#Window setup
scene.width = 1024
scene.height = 768
scene.center = vector(600,0,0)
 
#Objects
cliff = box(pos=vector(-100,0,0), size=vec(200,800,0), color=color.white)
ravine = box(pos=vector(245,-200, 0), size=vec(490,400,0), color=color.white)
lake = box(pos=vector(940, -200, 0), size=vec(900,400,0), color=color.blue)
runawaycraft = sphere(pos=vector(-200,400,0), radius=10, color=color.red)

#Parameters and Initial Conditions
g = vector(0,-9.81,0)
b = 0  #Drag coefficient

runawaycraftm = 1500
runawaycraftv = vector(10,0,0)
runawaycraftp = runawaycraftm*runawaycraftv

#Time and time step
t=0
tf=5
dt = 0.01

#MotionMap/Graph
runawaycraftMotionMap = MotionMap(runawaycraft, tf, 5, markerScale=1, labelMarkerOrder=False, markerColor=color.orange)

#Calculation Loop
while runawaycraft.pos.x < 900:
    rate(500)

    Fgrav = runawaycraftm*g
    Fground = -Fgrav
    Fnet = Fgrav + Fground
 
    runawaycraftp = runawaycraftp + Fnet*dt
    runawaycraft.pos = runawaycraft.pos + (runawaycraftp/runawaycraftm)*dt

    runawaycraftMotionMap.update(t, runawaycraftp/runawaycraftm)

    t = t + dt