# Assignment 1
## First order boustrophedon navigator
The following PID gain values were fine-tuned to optimize the performance of the Boustrophedon coverage path planner for the given simulation environment. The tuning was done iteratively to minimize oscillations, improve stability, and maintain smooth transitions between waypoints.
| Parameter     | Original Value | Final Value | Justification for Change                                                                 |
|---------------|----------------|-------------|-------------------------------------------------------------------------------------------|
| Kp_linear     | 10.0           | 11.0        | Increased to make the robot more responsive in following the desired trajectory. |
| Kd_linear     | 0.1            | 0.3         | Increased to provide better damping, preventing excessive oscillations while tracking the path. |
| Kp_angular    | 5.0            | 8.0         | Increased to enhance turning accuracy.    |
| Kd_angular    | 0.2            | 0.01        | Reduced to prevent over-damping, allowing the robot to turn more efficiently without sluggish corrections. |


### Original path


![Screenshot from 2025-01-27 21-54-02](https://github.com/user-attachments/assets/7814b2c6-4ac1-4760-849e-2bfb596108af)

### Final path 


![Screenshot from 2025-01-28 00-26-26](https://github.com/user-attachments/assets/e2451f54-c1f7-477b-a687-a7c83333e7d1)



### Tuning Methodology

The tuning methodology for this project involved adjusting key parameters to optimize the robot's performance. The primary goal was to achieve a balance between responsiveness, accuracy, and stability. The following approach was taken for tuning:

1. **Parameter Identification:**
   The first step was to identify the key parameters that influence the robot’s motion, which included the proportional (Kp) and derivative (Kd) gains for both linear and angular motion.

2. **Linear Motion Tuning:**
   - **Kp_linear** was adjusted to make the robot more responsive in following the desired trajectory. By increasing this value from 10.0 to 11.0, the robot's linear motion became more responsive, reducing lag in the path-following behavior.
   - **Kd_linear** was increased from 0.1 to 0.3 to improve damping and prevent oscillations. This adjustment helped stabilize the robot’s linear motion, especially when changing directions.

3. **Angular Motion Tuning:**
   - **Kp_angular** was increased from 5.0 to 8.0 to improve the robot’s turning accuracy. This change reduced the deviation from the desired orientation, making the robot’s turns more precise.
   - **Kd_angular** was reduced from 0.2 to 0.01 to prevent over-damping. The lower value allowed for faster and more efficient turns without sluggish corrections.


The methodology followed a trial-and-error approach, where each parameter was adjusted incrementally, and the robot's performance was observed and evaluated after each change. This iterative process helped ensure that the final parameters provided optimal performance across all motion aspects.


 
