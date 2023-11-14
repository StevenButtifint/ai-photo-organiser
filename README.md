# AI Photo Organiser


### Demo Video
<p align="middle">
<img src="https://github.com/stevenbuttifint/ai-photo-organiser/blob/main/demo/demo_video.gif?raw=true" width=49% height=100%>
</p>


### Description
The AI Photo Organiser enabled automatic organisation of your photo collections using artificial intelligence. I developed this desktop application using the Electron framework and Python.

### How it works
1. The user selects a folders containing an unsorted set of photos.
2. Each photo gets a classification based on its contents and distinct features.
3. Similar classifications get grouped together to form clusters.   
4. The clusters define which subfolder a photo gets sorted into.
5. The use now has their photos sorted into subfolders.

### Design Decisions
I used a convolutional neural network for the initial photo classification, selecting the EfficientNet B3 model to minimize operation time while maintaining high accuracy, due to the user environment having minimal computing power.
The photo classifications get clustered using a linkage matrix created with WordNet from the Natural Language Toolkit (NLTK). You can pre-download WordNet for the neural network classes to minimize operation time. This ensures the approach is versatile, regardless of the set of photo classifications produced in any given scenario.
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
- How to make looping animations using the Adobe Creative Suite.
- How to create a linkage matrix to cluster words from a wordnet.



---

[Back To The Top](#ai-photo-organiser)
