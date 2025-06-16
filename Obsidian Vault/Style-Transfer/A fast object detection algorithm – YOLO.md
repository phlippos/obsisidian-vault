## Strengths and limitations of YOLO
- YOLO is known for its speed
- YOLO struggles with smaller objects
- As with most deep learning models, it also struggles to properly detect objects that deviate too much from the training set
## YOLO's main concepts
- YOLO revolutionized object detection by transforming it into a single, efficient regression problem.
- 1. The Single Pass Approach
	- Unlike traditional methods that scan images multiple times with sliding windows, YOLO processes the entire image in a **single forward pass** through a neural network - hence the name "You Only Look Once."
- 2. Grid System
	- The input image is divided into a **w × h grid** (typically something like 7×7 or 13×13)
	- Each grid cell is responsible for detecting objects whose center falls within that cell
	- This spatial division is the foundation of YOLO's approach
- 3. Bounding Box Predictions
	- For each grid cell, YOLO predicts:
		- **B bounding boxes** (typically 2-5 boxes per cell)
		- For each box:
			- (x, y) coordinates of the box center (relative to the grid cell)
			- Width and height of the box (relative to the entire image)
			- Objectness score (confidence that an object exists in this box)
- 4. Class Predictions
	- Each grid cell also predicts **class probabilities** (what object is present)
	- This is independent of the number of bounding boxes
	- Final detection combines box confidence with class probabilities
- 5. The Regression Problem
	- YOLO frames all these predictions as a single regression task:
		- The network outputs a tensor with dimensions: w × h × [B × (5 + C)]
			- Where 5 = (x, y, width, height, confidence)
			- And C = number of classes
		- This is trained end-to-end with a single loss function
- 6. Prediction Processing
	- Bounding boxes with high confidence scores are kept
	- Non-maximum suppression removes duplicate detections
	- Final output contains position, size, and class of detected objects
![[Pasted image 20250517090246.png]]
## The YOLO backbon
![[Pasted image 20250517085859.png]]
## Introducing anchor boxes
- <mark style="background: #FFB86CA6;">if most of the objects in the train dataset are big, the network will tend to predict w and h as being very large. And when using the trained model on small objects, it will often fail.</mark> To fix this problem, YOLO v2 introduced anchor boxes.
- Anchor boxes (also called priors) are a set of bounding box sizes that are decided upon before training the network.
- For instance, when training a neural network to detect pedestrians, tall and narrow anchor boxes would be picked.,
- ![[Pasted image 20250517093240.png]]
- A set of anchor boxes is usually small—from 3 to 25 different sizes in practice. As those boxes cannot exactly match all the objects, the network is used to refine the closest anchor box.
## How YOLO refines anchor boxes
- ![[Pasted image 20250517093532.png]]
- **Prediction Mechanism**: The network doesn't predict absolute coordinates directly, but rather adjustments to these anchor boxes:

- **Position adjustments**: The network outputs t_x and t_y, which are transformed to determine the center coordinates
- **Size adjustments**: The network outputs t_w and t_h, which scale the anchor dimensions
- ![[Pasted image 20250517093656.png]]
- Where:
	- The sigmoid function constrains the box center to be within the grid cell
	- The exponential function allows scaling the anchor box dimensions
- ![[Pasted image 20250517093709.png]]
- ## Benefits of Anchor Boxes
	1. **Handles Multiple Objects**: Allows a single grid cell to detect multiple objects of different shapes
	2. **Improves Detection of Objects with Extreme Aspect Ratios**: Better at finding very tall, very wide, or unusually shaped objects
	3. **Stabilizes Training**: Provides better initialization for the network's bounding box predictions
	4. **Reduces Learning Complexity**: The network only needs to learn adjustments to predefined shapes

![[Pasted image 20250517094501.png]]

## Post-Processing Bounding Boxes in YOLO
- After YOLO predicts raw bounding boxes, we need to filter and refine these predictions. Here's a clear explanation of the post-processing pipeline:
- Step 1: Calculate Final Class Scores
	- For each predicted box, YOLO outputs:
		- `box_confidence`: Probability that an object exists in this box (0-1)
		- `classes_scores`: Array of probabilities for each class (e.g., [dog: 0.7, airplane: 0.8, ...])
		- To get the final score for each class:

```python
final_scores = box_confidence * classes_scores
```
In the example with `box_confidence = 0.5`:

- Dog: 0.5 × 0.7 = 0.35
- Airplane: 0.5 × 0.8 = 0.4
- Bird: 0.5 × 0.001 = 0.0005
- Elephant: 0.5 × 0.1 = 0.05
### Step 2: Apply Confidence Threshold

We only want to keep predictions with high confidence:

```python
OBJECT_THRESHOLD = 0.3
filter = final_scores >= OBJECT_THRESHOLD
filtered_scores = final_scores * filter
```
This creates a mask that zeros out low-confidence predictions:

- Dog: 0.35 (kept, above threshold)
- Airplane: 0.4 (kept, above threshold)
- Bird: 0.0005 (zeroed, below threshold)
- Elephant: 0.05 (zeroed, below threshold)
### Step 3: Select the Highest Scoring Class

If any class passes the threshold, we select the one with the highest score:

```python
if np.max(filtered_scores) > 0:
    class_id = np.argmax(filtered_scores)
    class_label = CLASS_LABELS[class_id]
```
In our example, the highest score is 0.4 for "airplane", so this box would be classified as an airplane.

### Step 4: Final Detection Result

The final output for this bounding box is:

- Box coordinates and dimensions (from earlier in the pipeline)
- Class: "airplane"
- Confidence score: 0.4

This process is repeated for all predicted boxes, followed by Non-Maximum Suppression (NMS) to remove overlapping detections.
![[Pasted image 20250517100547.png]]


## NMS (Non Maximum Suppression)
- The idea of NMS is to remove boxes that overlap the box with the highest probability.
- To do so, we sort all the boxes by probability, taking the ones with the highest probability first. Then, for each box, we compute the IoU with all the other boxes.
- After computing the IoU between a box and the other boxes, we remove the ones with an IoU above a certain threshold (the threshold is usually around 0.5-0.9)
- ![[Pasted image 20250518010708.png]]
- ![[Pasted image 20250518010752.png]]
