# RICE IMAGE CLASSIFICATION USING MACHINE LEARNING
![uncooked-organic-risotto-rice](https://github.com/user-attachments/assets/b6938377-af49-451b-bd83-61c094647217)


## Project overview
The Rice Image Classification project aims to develop a robust and efficient machine learning model to classify different types of rice grains based on their images. The primary goal is to automate the process of rice type identification, which is crucial for quality control, inventory management, and consumer information in the rice industry.

## Business problem
RiceMaster a rice marketing firm has been handling different varieties of rice grain from farmers. In the course of their duties, they have been faced with the challenge of differentiating rice grain from different farmers. This has led to poor quality control of the rice released in the market. This study seeks to automate the classification process using Convolutional Neural Network to improve efficiency and accuracy of rice packed. Additionally, the study aims to to ensure customer satisfaction is improved and market standards are attained.

## Motivation
Ensuring the quality and type of rice is crucial for both farmers and consumers. High-quality rice ensures consumer satisfaction and adherence to market standards. Automating the classification process can significantly reduce labor costs and increase efficiency and accuracy. This topic is important for enhancing food security and quality control in the agricultural domain. Automated classification systems can also assist in identifying potential quality issues early in the supply chain, preventing large-scale distribution of substandard products.

## Image variables
a. area: The number of pixels in the image region or the total area covered by the rice grain.

b. perimeter: The total length of the boundary of the rice grain.

c. major_axis: The length of the longest diameter of the rice grain.

d. minor_axis: The length of the shortest diameter of the rice grain.

e. eccentricity: A measure of how much the shape of the rice grain deviates from being circular. It ranges from 0 (a perfect circle) to 1 (a line segment).

f. EQDIASQ: Equivalent Diameter, which is the diameter of a circle with the same area as the rice grain.

g. solidity: The ratio of the area of the rice grain to the area of its convex hull (the smallest convex shape that can contain the grain).

h. convex_area: The area of the convex hull of the rice grain.

i. extent: The ratio of the area of the rice grain to the area of its bounding box (the smallest rectangle that can contain the grain).

j. aspect_ratio: The ratio of the major axis to the minor axis of the rice grain.

## Colour and texture features

k. StdDevLABA: The standard deviation of the 'A' channel in the LAB color space, which indicates variations in the color component representing the red/green balance.

l. skewLABA: The skewness of the 'A' channel in the LAB color space, which measures the asymmetry of the color distribution.

m. kurtosisLABA: The kurtosis of the 'A' channel in the LAB color space, indicating the "tailedness" of the color distribution.

n. entropyLABA: The entropy of the 'A' channel in the LAB color space, representing the randomness or complexity of the color information.

o. meanLABB: The mean value of the 'B' channel in the LAB color space, representing the average color component for blue/yellow balance.

p. StdDevLABB: The standard deviation of the 'B' channel in the LAB color space, indicating variations in the color component representing the blue/yellow balance.

q. skewLABB: The skewness of the 'B' channel in the LAB color space, measuring the asymmetry of the color distribution.

l. kurtosisLABB: The kurtosis of the 'B' channel in the LAB color space, indicating the "tailedness" of the color distribution.

m. entropyLABB: The entropy of the 'B' channel in the LAB color space, representing the randomness or complexity of the color information.

## Classification feature

n. Class: The label or category assigned to each rice grain image, indicating the type or variety of rice (e.g., Arborio).

# **Table of contents**

1. Business understanding
2. Data understanding
3. Data preparation
4. Modelling
5. Evaluation
6. Deployment
7. Conclusion
8. Recommendation

# **Model evaluation**
Of the 3 models evaluated, ResNet50V2 tuned model had the best scores at a validation accuracy of 0.988 and test loss 0.03. This means that:

- Validation accuracy 0.988: 98.8% of the time, the model correctly classified the images in the validation dataset. A high validation accuracy suggests that the model has learned the distinguishing features of the rice varieties effectively.
- Test Loss of 0.03: The model had a loss value of 0.03 on the test set. Loss is a measure of the error in the model's predictions; a lower loss indicates better performance. A test loss of 0.03 is quite low, suggesting that the model makes very few errors on the test data.

# Deployment
The deployed model can be accesssed at https://mybinder.org/v2/gh/KirigoY/dsc-phase-5-capstone-project.git/HEAD


# **Conclusion**
**Limitations**
1. The dataset could have had more rice categories
2. 


# **Recommendations**
1. Scaleability: The dataset could be enhanced with additional rice grain variants in future to cater for other varieties like Bomba, Calasparra, Valencia etc currently not 
   classified.
2. Intergration with other systems: Integrate the classification system with existing agricultural or inventory management systems for broader application.
3. Incremental Learning: Implement incremental learning to update the model with new data without retraining from scratch.







