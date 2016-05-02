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

    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        print command
        if command[0] == "push":
            ptmp = new_matrix()
            for c in range len(stack[len(stack) - 1]):
                for r in range len(stack[len(stack) - 1][c]):
                    ptmp[c][r] = stack[len(stack) - 1][c][r]
            stack.append(ptmp)
        elif command[0] == "pop":
            stack.pop()
        elif command[0] == "move":
            stmp = make_translate(command[1],command[2],command[3])
            matrix_mult(stmp,stack[len(stack) - 1])
        elif command[0] == "rotate":
            if command[1] == "x":
                stmp = make_rotX(command[2])
                matrix_mult(stmp,stack[len(stack) - 1])
            elif command[1] == "y":
                stmp = make_rotY(command[2])
                matrix_mult(stmp,stack[len(stack) - 1])
            else:
                stmp = make_rotZ(command[2])
                matrix_mult(stmp,stack[len(stack) - 1])
        elif command[0] == "box":
            add_box(screen,command[1],command[2],command[3],command[4],command[5],command[6])
        elif command[0] == "sphere":
            add_sphere(screen,command[1],command[2],command[3],command[4])
        elif command[0] == "torus":
            add_torus(screen,
