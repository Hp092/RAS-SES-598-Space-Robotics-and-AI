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



# Assignment 2

## Cart-Pole Optimal Control Report

### Introduction
The objective of this project is to implement and tune a Linear Quadratic Regulator (LQR) for the cart-pole system. The goal is to achieve optimal stabilization of the cart-pole system by fine-tuning the state and control cost matrices. The cart-pole is a classic control problem where the challenge lies in maintaining the balance of the pole while controlling the cart's position within safe operational limits.
Video link : https://drive.google.com/file/d/1sq_10H28Zj4IffBJ_FvbGADUjBKDwZxp/view?usp=sharing

### System Overview
The cart-pole system is a classic control problem involving a cart that can move horizontally and a pole hinged to the cart, which must be balanced upright. The system's dynamics are nonlinear, and LQR is used to design a feedback controller that minimizes a quadratic cost function.

### Parameters and Justifications

#### State Cost Matrix (Q)
The state cost matrix `Q` penalizes deviations from the desired state. The diagonal matrix used is:


```markdown
Q = | 15.0   0     0     0   |
    | 0     10.0   0     0   |
    | 0      0    45.0   0   |
    | 0      0     0    25.0 |
```

Justifications:

- **x (Cart Position) — 15.0:** A moderate penalty to maintain the cart near the desired position without overly restricting its movement.
- **ẋ (Cart Velocity) — 10.0:** A lower penalty allows the cart to gain necessary momentum while keeping excessive speeds in check.
- **θ (Pole Angle) — 45.0:** The highest penalty ensures the pole remains upright, which is critical for stability.
- **θ̇ (Pole Angular Velocity) — 25.0:** A significant penalty reduces rapid swings of the pole, promoting smoother control.

Control Cost Matrix (R)
The control cost matrix R penalizes the use of control effort.
```markdown
R = | 0.05 |
```
Results

The chosen `Q` and `R` matrices resulted in:
- **Stable Pole Balancing:** The pole remained upright but exhibited noticeable oscillations, particularly under dynamic conditions.
- **Cart Movements:** The cart experienced more prominent fluctuations but stayed within safe operational limits.
- **Increased Control Effort:** The control force displayed higher variability, indicating a more aggressive control strategy to handle disturbances.


![lqr_performance](https://github.com/user-attachments/assets/9414bbea-8247-41c6-a8f5-c2ae79eee2fc)

Graph Analysis:

1. **Cart Position (Top Plot):**
   - The cart position fluctuates within ±0.4 m, staying within the defined safe limits.
   - Increased oscillations around the 10 to 30-second mark suggest the system's response to varying disturbances.

2. **Pendulum Angle (Middle Plot):**
   - The pendulum angle shows frequent excursions approaching the ±4° stability threshold.
   - Despite the higher oscillations, the pole remains within the safe bounds, maintaining system stability.

3. **Control Force (Bottom Plot):**
   - The control force exhibits a higher magnitude and frequency of changes, peaking above ±40 N.
   - This aggressive control ensures the system handles disturbances but results in a less smooth control effort.

Conclusion

The updated `Q` and `R` matrices maintain system stability while handling dynamic disturbances. The more aggressive control approach leads to increased oscillations in both cart position and pendulum angle but keeps them within safe limits. Although the control force is more variable, it effectively stabilizes the system under fluctuating conditions, as reflected in the new simulation results.
