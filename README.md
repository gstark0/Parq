# PARQ
#### AI-Powered parking spot detection based on CCTV footage

<img src="https://raw.githubusercontent.com/gstark0/Parq/master/images/logo.png" width="500">

🇺🇸 English | 🇵🇱 <a href="https://github.com/gstark0/Parq/blob/master/README_PL.md">Click here to see Polish readme</a>
### About
The main idea behind the project was to solve one of the most important issues in almost every modern city in the world - parking issue. You may think that parking sensors are the solution, but they also can get pretty expensive. Meanwhile, above all those parking spots, live CCTV footage from the security cameras is frequently transmitted to some WWW websites. This solution aims to use those kinds of cameras - that are open for public.

### Technology
In order to solve the issue, PARQ uses Deep Learning approach - Applying Convolutional Neural Networks to each parking spot, it is able to predict with 95% of accuracy (depending on the camera angle), which spot is occupied and which one is empty. Keras model (with TensorFlow backend) was trained on dataset retrieved from Polish open CCTV footage on shopping mall parking in Inowrocław. The server is based on Python Flask.

### Current progress
Data about all parking spots is saved in local database (currently updated manually by requesting /update page) and then loaded directly with HTML files or fetched by JS scripts. PARQ can display each spot in columns to let users know the exact location of empty spot. Each spot location has to be added with `add_spot.py`.

<img alt="Real parking image" src="https://raw.githubusercontent.com/gstark0/Parq/master/images/single_column_real.png" width="300"><img alt="PARQ representation" src="https://raw.githubusercontent.com/gstark0/Parq/master/images/single_column.png" width="300">

### Future
As of now, PARQ is limited to web service, but in the future it will also be available as iOS/Android app. Besides target platform, PARQ should be able to automatically detect each parking spot itself (currently coordinates of each one have to be added in `add_spot.py`).


![](https://raw.githubusercontent.com/gstark0/Parq/master/images/2.png) <img src="https://raw.githubusercontent.com/gstark0/Parq/master/images/mobile.png" width="300">
