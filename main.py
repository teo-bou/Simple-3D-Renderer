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

@ti.func
def distance(a, b):
    return (a - b).norm()

@ti.func
def over(p, a, b):
    p = ti.Vector([p.x - a.x, p.y - a.y])
    mid = (a - b)
    mid = perpendicular(mid)
    return dot(p, mid) > 0
       



@ti.kernel
def render_shader(a: ti.types.vector(2, ti.f32), b: ti.types.vector(2, ti.f32), c: ti.types.vector(2, ti.f32), color: ti.types.vector(3, ti.f32)):
    for i, j in pixels:
        x = (i / res) * 2 - 1
        y = (j / res) * 2 - 1

        
        p = ti.Vector([x, y])

        if over(p, a, b) & over(p, b, c) & over(p, c, a):
            pixels[i,j] = color


        if distance(p, a) < 0.1 or distance(p, b) < 0.1 or distance(p, c) < 0.1:
            pixels[i,j] = (1,0,0)

        
        

gui = ti.GUI("Simple renderer", res=(res, res))
t = 0.0
while gui.running:
    a = ti.Vector([-0.5, 0.5])  # Top Left
    b = ti.Vector([ 0.5, 0.5])  # Top Right
    c = ti.Vector([ 0.2, -0.2]) # Bottom Right
    d = ti.Vector([-0.2, -0.2]) # Bottom Left

    red = ti.Vector([1.0, 0.0, 0.0])
    green = ti.Vector([0.0, 1.0, 0.0])

    render_shader(b, a, c, red)
    render_shader(a, d, c, green)

    gui.set_image(pixels)
    t+=1/1000
    gui.show()
