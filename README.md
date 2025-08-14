# Behavioral_Clonning_model_for_steering_Control

## Behavioral Cloning Project

This repository contains an implementation of a behavioral cloning model for autonomous driving based on the NVIDIA End-to-End Learning for Self-Driving Cars research paper. The model is trained to predict steering angles from camera images using deep learning.

## Repository Structure

```
photos/                            # Dataset images used for training/testing
models/
├── Behavioral_clonning_model.h5                  # Pre-trained behavioral cloning model
├── Behavioral_clonning_model_my_data(1).h5
├── Behavioral_clonning_model_my_data_3.h5
├── Behavioral_clonning_model_my_data_4.h5
├── Behavioral_clonning_model_my_data.h5
└── drive.py                                       # Script to run the trained model in the simulator
README.md
simulator-linux/ 

```

## Project Description

This project uses a Convolutional Neural Network (CNN) to learn steering commands from images taken from a front-facing camera on a virtual car.
The architecture is inspired by NVIDIA's paper:

End to End Learning for Self-Driving Cars — M. Bojarski et al., NVIDIA, 2016.
Paper Link



## Training the Model

### Prepare your dataset

  Collect driving data using the simulator in training mode.

  The dataset should be stored in the photos/ directory (or update the notebook path accordingly).

### Open the training notebook

  jupyter notebook Behavioral_cloning_project.ipynb


### Run the cells in the notebook to:

  Load and preprocess the data

  Train the CNN model based on NVIDIA's architecture (with small modifications)

### Save the trained model to the models/ folder

  Test your newly trained model in the simulator by running:
```
    python models/drive.py models/<your_model>.h5
```


## ⚠️ Disclaimer

The simulator in the simulator-linux folder is not my work — it is part of Udacity's Self-Driving Car Simulator and is included here only for testing purposes. All copyrights belong to their respective owners.

The core model architecture is based on NVIDIA's research paper mentioned above. This implementation is for educational and research purposes only.

## 📌 References

NVIDIA: End to End Learning for Self-Driving Cars, 2016. arXiv:1604.07316

Udacity Self-Driving Car Simulator: GitHub Link
