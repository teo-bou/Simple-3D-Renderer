import taichi as ti
import numpy as np
ti.init(arch=ti.metal) 

res = 512
pixels = ti.Vector.field(3, dtype=ti.f32, shape=(res, res))

@ti.func
def dot(a, b):
    return a.x * b.x + a.y * b.y

@ti.func
def perpendicular(a):
    return ti.Vector([a.y, -a.x])


@ti.kernel
def render_shader(a: ti.types.vector(2, ti.f32), b: ti.types.vector(2, ti.f32)):
    for i, j in pixels:
        x = (i / res) * 2 - 1
        y = (j / res) * 2 - 1

        p = ti.Vector([x, y])
        mid = (a - b)
        mid = perpendicular(mid)
        if dot(p, mid) > 0:
            pixels[i,j] = (1,1,1)
        else:
            pixels[i,j] = (0,0,0)
        

gui = ti.GUI("Simple renderer", res=(res, res))
t = 0.0
while gui.running:
    a = ti.Vector([0,0])
    b = ti.Vector([np.cos(t),np.sin(t)])
    render_shader(a,b)
    gui.set_image(pixels)
    t+=1/1000
    gui.show()
