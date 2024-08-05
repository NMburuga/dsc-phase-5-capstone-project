RICE IMAGE CLASSIFICATION BASED ON DEEP LEARNING

!![image](https://github.com/user-attachments/assets/2cc73418-d147-496e-bcb5-b3e953636658)

                                   Authors: 
Jane Martha,Yvonne Mwangi, Bethuel Maruru, Loise Mburuga,Sonia Ojay,Faith Mwenda 



                             PROJECT  OVERVIEW

 The project focuses on leveraging a dataset of Rice images to develop machine learning models capable of
 accurately identifying quality rice. The dataset sourced from Kaggle, comprises of images classified into 5 categories:
 arbori,basmati,ipsala,jasmine,karacadag. This project aims to build and optimize convolutional neural network(CNN) models to achieve high quality classification accuracy.

 
![image](https://github.com/user-attachments/assets/b58185b5-7d4f-44d3-97f2-48b99f782b53)

                          PROBLEM STATEMENT

                          
Rice is a staple food for more than half of the world's population, making its quality and type assessment crucial for both consumers and producers. Traditional methods of rice classification are labor-intensive, time-consuming, and prone to human error. With the advent of machine learning and image processing technologies, there is a significant opportunity to automate and improve the accuracy of rice classification processes.

                           DATA UNDERSTANDING


Source: Kaggle's Rice Image Classification dataset. Structure: The dataset icontains five rice varieties namely arbori,basmati,ipsala,jasmine,karacadag with 75,000 images.
 directories: train: Contains the following Class names and their indices:
Arborio: 0
Basmati: 1
Ipsala: 2
Jasmine: 3
Karacadag: 4

Class names:
['Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

                            OBJECTIVES


The primary objective of this project is to develop a machine learning model capable of accurately classifying different types of rice grains based on their images. The classification will be performed using a dataset comprising various rice types, each with distinct visual characteristics.


                            Methodology

  This project encompassed the following tasks:

Data Acquisition and Preprocessing: Collection and preprocessing of a diverse set of rice grain images to ensure the dataset is suitable for model training and evaluation.
Model Development: Design and implementation of machine learning models using techniques such as Convolutional Neural Networks (CNNs) to classify the rice images.
Model Evaluation: Evaluation of the model's performance using appropriate metrics (e.g., accuracy, precision, recall, F1-score) to ensure its reliability and robustness.
Optimization: Fine-tuning the model to enhance its performance and reduce computational costs.
Deployment: Development of a user-friendly interface for practical applications, enabling end-users to upload rice images and receive classification results.


                           Expected Outcomes
The expected outcomes of this project include:

A trained machine learning model capable of classifying rice types with high accuracy.
A comprehensive analysis of the model's performance and potential areas for improvement.
A deployable application that facilitates easy and accurate rice classification for end-users.
By addressing these objectives and challenges, this project aims to contribute to the advancement of agricultural technologies and improve the efficiency and accuracy of rice classification processes.

                        Models Categories

1: General-purpose CNN Model(CNN)
2:Tuned General-purpose CNN Model
3:ResNet50V2 Mode
4:tuning on the ResNet50V2 Model



                         OUTPUT

![image](https://github.com/user-attachments/assets/10e5953d-a131-4f17-af76-94fc75680daf)


We also Checked Class Balance to ensure that all classes had a similar number of instances. We confirmed that our dataset was balanced because all classes had equal number of instances


                       MODEL ARCHITECTURE

VGG-16 CNN Model Architecture

Model summary after compilation:
Model: "functional_22"
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
┃ Layer (type)                         ┃ Output Shape                ┃         Param # ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩
│ input_layer_5 (InputLayer)           │ (None, 128, 128, 3)         │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ vgg16 (Functional)                   │ (None, 4, 4, 512)           │      14,714,688 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ global_average_pooling2d_1           │ (None, 512)                 │               0 │
│ (GlobalAveragePooling2D)             │                             │                 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_6 (Dense)                      │ (None, 128)                 │          65,664 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dropout_3 (Dropout)                  │ (None, 128)                 │               0 │
├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤
│ dense_7 (Dense)                      │ (None, 5)                   │             645 │
└──────────────────────────────────────┴─────────────────────────────┴─────────────────┘
  Total params: 14,780,997 (259.02)
 Trainable params: 66,309 (259.02 KB)
 Non-trainable params: 14,714,688 (56.13 MB)
 

The baseline model architecture comprises a total of 14,780,997 parameters, with all parameters being trainable. The model's size is approximately 250.02 MB. There are no non-trainable parameters in this architecture, showing that all parameters are updated during the training process


                Classification Report:

              precision    recall  f1-score   support

     Arborio       0.96      0.98      0.97     15000
   Karacadag       0.97      0.99      0.98     15000
     Jasmine       0.98      1.00      0.99     15000
      Ipsala       0.98      0.94      0.96     15000
     Basmati       0.98      0.97      0.98     15000

    accuracy                           0.98     75000
   macro avg       0.98      0.98      0.98     75000
weighted avg       0.98      0.98      0.98     75000





                                               Summary:
                                               
The classification report indicates a very well-performing model with high precision, recall, and F1-scores for all classes, and an overall accuracy of 98%. The macro and weighted averages confirm that the model’s performance is robust across all classes and that the class distribution doesn't skew the performance metrics significantly.


![image](https://github.com/user-attachments/assets/3208df45-a813-48a8-bb53-a7e2cc567fd0)

Overall, the model performs robustly, accurately identifying the majority of instances across all classes, with only a few notable misclassifications primarily involving Ipsala.

![image](https://github.com/user-attachments/assets/94358a51-d04f-4eb4-a650-71d7d5526ff2)

The ROC curves and AUC values demonstrate that the model performs exceptionally well for all classes, with nearly perfect classification for Arborio, Ipsala, Karacadag, Basmati and Jasmine (AUC = 1.00).

![image](https://github.com/user-attachments/assets/6a69702b-a454-49a1-8f23-008796df8b1a)

The validation accuracy consistently being higher or very close to the training accuracy is a positive sign of good generalization While The close tracking of validation loss with the training loss further confirms the model's strong generalization performance.


                           Conclusion
                           
The rice image classification project demonstrates the potential of using advanced machine learning techniques to automate and improve the accuracy of rice type identification. By leveraging convolutional neural networks (CNNs) and image processing technologies, we have developed a robust model capable of distinguishing between various types of rice grains based on their visual characteristics.

                         Recommendations


 Future enhancements to this project could include expanding the dataset to include a wider variety of rice types and further fine-tuning the model using advanced techniques such as ensemble learning. Additionally, integrating more sophisticated image preprocessing steps and exploring the use of other deep learning architectures could yield even better performance.
                           
                        

                        

                        

                            
                             
