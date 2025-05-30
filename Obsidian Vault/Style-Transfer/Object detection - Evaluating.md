## Precision-recall curve
- The general idea is to visualize the precision and the recall of the model at each threshold of confidence.
- Moving the threshold has an impact on precision and on recall:
	- If T is close to 1 :  Precision will be high, but the recall will be low.
	- If T is close to 0 : Precision will be low, but the recall will be high.
- ![[Pasted image 20250517083257.png]]

## Average precision and mean average precision
- **Average precision** (AP) corresponds to the area under the curve. Since it is always contained in a one-by-one rectangle, AP is always between 0 and 1
- **mean Average Precision** (mAP): This corresponds to the mean of the average precision for each class. If the dataset has 10 classes, we will compute the average precision for each class and take the average of those numbers
![[Pasted image 20250517083751.png]]
!!! how do you decide when a prediction and the ground truth are matching? A common metric is the Jaccard index, which measures how well two sets overlap. Also known as<mark style="background: #FFF3A3A6;"> Intersection over Union (IoU)</mark>
![[Pasted image 20250517083726.png]]
Why compute such a fraction and not just use the intersection? While the intersection would provide a good indicator of how much two sets/boxes overlap, this value is absolute and not relative. Therefore, two big boxes would probably overlap by many more pixels than two small boxes. This is why this ratio is used

