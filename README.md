# PhotoDataLab

The idea behind this project is to create a graphic user interface for a series of modules written in Python and used for  scientific data analysis.
The project philosophy is that it should integrate data importing, treatment and visualization, based on some concepts:
- The data workflow should be graphically programmed making use of boxes and connectors
- Plots of publisheable quality, with interactive features, should be produced in real-time as result
- The underlying data should be saved in a simple, ordered and uniform csv format
- It should be possible to save a workflow as a new "box" (a new function), that can be used in other workflows
- It should be possible to export a workflow as a standalone program that can work on files in folders
Above all, the most important feature should be simplicity. Extreme simplicity. Basically (unfortunately) most of "lab" scientist don't even want to hear the word "coding", to the point that they prefer spending hours in copy-pasting data between several softwares and manually applying mathematical transformations, than writing simple code in any of the plethora of existing softwares.
The idea here is to substitute coding with graphical programming, in an intuitive way, with clear use of every module exaustively explained in an easy to access documentation.

The starting point should be simple 2D data plotting and treatment, with the aim to integrate in a second time numerical simulations and fit. The "module" approach should be focused on the possibility for users to build and share their own modules in an easy way, both through regular or graphic programming, allowing the program to be naturally developed by users rather than from a single person or team.
The software will be open source and freely distributed to anyone, with no charges and no possibilty of commercial exploitation.

#Personal goal in the project

As a personal note, I am totally new to Python (although many of the functions of the program in the ideal 1.0 version, focused
on the type of data treatment I need in my regular job as a photochemist, have already been written by me in bash) and this project is also for me a way to learn (as it was for the choice of using bash, clearly a poor choice for that type of job, but that allowed me to learn the basic commands to use a linux system), so you can consider this project as part of my self-teaching activity.
This implies that there could be similar solutions, surely even more advanced solutions, offering features I don't even plan
to put in the project right now, and surely there are better plotting softwares, better data analysis one, better programming languages for very efficient computing. A lot of people out there is able to do all this way better than me, and my goal is not to replace any of these solutions.
I believe the real novelty would be the integration of several simple tools that are generally obtained thorugh the use of
several softwares in a single one, in the most user-friendly way one can think about, and distribute it as a free software. I don't know what the result will be, but I think it is a good thing to try.

Luca Ravotto (ottovan)

#Updates

I'll use the following space to update what I consider the main goal at the moment:
- Rewrite in python just one of the simple routines I have developed in bash. Something like Import Data --> Normalize in a point --> Produce a plot of the data (possibly something slightly more elaborated in case it is needed).
- Build the GUI and try to implement all the functions using this simple sequence

This would allow to focus on various aspects, such as how a module should be written to be properly integrated, before expanding the module library and thus the capabilities of the software.

