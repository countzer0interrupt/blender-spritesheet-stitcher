# blender-spritesheet-stitcher
Automatic spritesheet creator for Blender 

Wrote this helpful script when using Blender as the base for spritesheet art in a pro bono project a few years back. Now using it for some homebrew game creation. Right now, it is just a basic script but I am planning on converting it into a proper Blender extension soon.

## Prerequisites
You need Blender 3.9 and above and normal read/write permissions on the filesys.

## Instructions
1. Open up the Scripting Tab in Blender, drop in the .py file. You're now ready to go.
2. You will need to do some basic set up in your scene - if you want multiple camera angles, set up multiple cameras and name them appropriately (i.e. front, back, side etc).
3. Arrange your animations as actions, name and number them appropriately (so you can predict where they'll be stitched on the spritesheet)
4. Ensure that you've set the appropriate dimensions within the editor, composites etc whatever it is you want to do. If you're looking for some good pixel tutorials check out the tutorial on BlenderNation here - https://www.blendernation.com/2020/04/06/blender-how-to-make-pixel-art/). 
5. By default, the script will try to create Normal & Albedo maps. It uses Cycles and MatCap views to do so, ensure that your Blender scene has MatCap set up under Cycles by default (probably should automate this in future iterations of the script). If you don't need normals, just change the settings at the top of the script.
6. Once you're ready to go, go to the Scripting Tab and press 'Run'
