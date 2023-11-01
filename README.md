# AI Photo Organiser


### Demo Video
<p align="middle">
<img src="https://github.com/stevenbuttifint/backup-manager/blob/main/demo/demo_video.gif?raw=true" width=49% height=100%>
</p>


### Description
The AI Photo Organiser enabled automatic organisation of your photo collections using artificial intelligence. I developed this desktop application using the Electron framework and Python.

### How it works
1. The user selects a folders containing an unsorted set of photos.
2. A neural network classifies each photo based on its contents.
3. Similarities between image contents are identified.
4. Groups get created using closely related classifications and high similarity features in the images.
5. The photos get organised into subfolders based on the group their classifications and similarities fall under.

### Design Decisions
I used a convolutional neural network for the initial image classification, selecting the EfficientNet B3 model to minimize operation time while maintaining high accuracy, due to the user environment having minimal computing power.
For the front-end development, I chose the Electron framework because of its robust cross-platform compatibility, and the ability to create a highly customizable UI/UX design using HTML, CSS, and JavaScript.
Python was my choice for the backend due to its strong cross-platform compatibility and extensive support for computer vision libraries.

### Tech Stack

- Front End
  - Electron Framework
  - JavaScript
  - HTML
  - CSS
  

- Back End
  - Python
  - Torchvision
  
### What I Learned
- How to use the Electron Framework to create a desktop application UI using HTML, CSS and Javascript.
- How to run backend python functions on separate background threads.
- How to use affordance in UI and UX design to make them more intuitive.



---

[Back To The Top](#ai-photo-organiser)