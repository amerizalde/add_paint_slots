# add_paint_slots
Blender Addon

## Installation
You can use the "Install from file" option in the user preferences for this .py file. Works fine.

## What?

This is a simple addon that implements a way to add empty image textures to a material while in Texture Paint mode, in Cycles, instead of having to go into the UV editor, create an image, and go into the node editor to add them.

You still have to decide how you want to use the texture by hooking it up in the node editor and adding bump nodes, normal nodes, etc...

## Why?

https://gfycat.com/BriskLimpingChimpanzee

I felt that there was a need for this based on the confusion I had and that I found others had when I searched on google, specifically questions like http://blender.stackexchange.com/questions/50647/missing-add-texture-paint-slot.

Again, you still need to have some knowledge of Blender to know how to hook up bump maps and normal maps correctly, but this will hopefully solve that particular UI disaster.


### Someone's TODO:

Find a way to add other node setups on a button push with an image texture ready to go. i.e. Texture Coordinate --> Image Texture --> Bump Node --> Normal Node
