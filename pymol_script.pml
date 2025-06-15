#How to run 
#{Pathtopymol}/pymol -c script.pml

#load the best model
load
bg_color white
show cartoon, all 
spectrum b, blue_white_red, chain A

#AlphaFold color code 
set_color n0, [0.051, 0.341, 0.827]
set_color n1, [0.416, 0.796, 0.945]
set_color n2, [0.996, 0.851, 0.212]
set_color n3, [0.992, 0.490, 0.302]
color n0, b < 100; color n1, b < 90
color n2, b < 70;  color n3, b < 50
#
#
#
# Optimize View: center, orient, and zoom for a nice figure
center
orient
zoom


png
save




