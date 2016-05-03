import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return
    points = []
    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        print command
        if command[0] == "push":
            ptmp = new_matrix()
            for c in range(4):
                for r in range(4):
                    ptmp[c][r] = stack[len(stack) - 1][c][r]
            stack.append(ptmp)
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "move":
            stmp = make_translate(command[1],command[2],command[3])
            matrix_mult(stack[len(stack) - 1],stmp)
            stack[len(stack) - 1] = stmp
        elif command[0] == "rotate":
            angle = command[2] * ( math.pi / 180 )
            if command[1] == 'x':
                stmp = make_rotX( angle )
            elif command[1] == 'y':
                stmp = make_rotY( angle )
            else:
                stmp = make_rotZ( angle )
            matrix_mult(stack[len(stack) - 1], stmp)
            stack[len(stack) - 1] = stmp
        elif command[0] == "scale":
            stmp = make_scale(command[1],command[2],command[3])
            matrix_mult(stack[len(stack) - 1],stmp)
            stack[len(stack) - 1] = stmp
        elif command[0] == "box":
            add_box(points,command[1],command[2],command[3],command[4],command[5],command[6])
            matrix_mult(stack[len(stack) - 1], points)
            draw_polygons(points, screen, color)
            points = []
        elif command[0] == "sphere":
            add_sphere(points,command[1],command[2],command[3],command[4],5)
            matrix_mult(stack[len(stack) - 1], points)
            draw_polygons(points, screen, color)
            points = []
        elif command[0] == "torus":
            add_torus(points,command[1],command[2],command[3],command[4],command[5],5)
            matrix_mult(stack[len(stack) - 1], points)
            draw_polygons(points, screen, color)
            points = []
        elif command[0] == "line":
            add_edge(points,command[1],command[2],command[3],command[4],command[5],command[6])
            matrix_mult(stack[len(stack) - 1], points)
            draw_lines(points, screen, color)
            points = []
        elif command[0]=='save':
            save_extension(screen, command[1])
        elif command[0]=='display':
            display(screen)
