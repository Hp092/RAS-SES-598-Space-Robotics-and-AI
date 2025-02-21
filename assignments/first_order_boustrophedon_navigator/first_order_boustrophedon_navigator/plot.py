import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import matplotlib.pyplot as plt
import numpy as np

class DataLogger(Node):
    def __init__(self):
        super().__init__('data_logger')
        
        # Subscribers to the topics
        self.pose_x_subscriber = self.create_subscription(
            Float64, '/turtle1/pose/x', self.pose_x_callback, 10)
        self.pose_y_subscriber = self.create_subscription(
            Float64, '/turtle1/pose/y', self.pose_y_callback, 10)
        self.linear_velocity_subscriber = self.create_subscription(
            Float64, '/turtle1/cmd_vel/linear/x', self.linear_velocity_callback, 10)
        self.angular_velocity_subscriber = self.create_subscription(
            Float64, '/turtle1/cmd_vel/angular/z', self.angular_velocity_callback, 10)
        self.cross_track_error_subscriber = self.create_subscription(
            Float64, '/cross_track_error', self.cross_track_error_callback, 10)
        
        # Lists to store the data
        self.pose_x_data = []
        self.pose_y_data = []
        self.linear_velocity_data = []
        self.angular_velocity_data = []
        self.cross_track_error_data = []
        
    def pose_x_callback(self, msg):
        self.pose_x_data.append(msg.data)
        
    def pose_y_callback(self, msg):
        self.pose_y_data.append(msg.data)
        
    def linear_velocity_callback(self, msg):
        self.linear_velocity_data.append(msg.data)
        
    def angular_velocity_callback(self, msg):
        self.angular_velocity_data.append(msg.data)
        
    def cross_track_error_callback(self, msg):
        self.cross_track_error_data.append(msg.data)

    def plot_data(self):
        # Create subplots for the data
        fig, axs = plt.subplots(3, 2, figsize=(12, 10))
        time = np.arange(len(self.pose_x_data))
        
        # Plot position (pose)
        axs[0, 0].plot(time, self.pose_x_data, label='Position X')
        axs[0, 0].set_title('Turtle1 Position X')
        axs[0, 0].set_xlabel('Time (s)')
        axs[0, 0].set_ylabel('Position X')
        
        axs[0, 1].plot(time, self.pose_y_data, label='Position Y')
        axs[0, 1].set_title('Turtle1 Position Y')
        axs[0, 1].set_xlabel('Time (s)')
        axs[0, 1].set_ylabel('Position Y')
        
        # Plot velocities
        axs[1, 0].plot(time, self.linear_velocity_data, label='Linear Velocity')
        axs[1, 0].set_title('Turtle1 Linear Velocity')
        axs[1, 0].set_xlabel('Time (s)')
        axs[1, 0].set_ylabel('Linear Velocity (m/s)')
        
        axs[1, 1].plot(time, self.angular_velocity_data, label='Angular Velocity')
        axs[1, 1].set_title('Turtle1 Angular Velocity')
        axs[1, 1].set_xlabel('Time (s)')
        axs[1, 1].set_ylabel('Angular Velocity (rad/s)')
        
        # Plot cross track error
        axs[2, 0].plot(time, self.cross_track_error_data, label='Cross Track Error')
        axs[2, 0].set_title('Cross Track Error')
        axs[2, 0].set_xlabel('Time (s)')
        axs[2, 0].set_ylabel('Error (m)')
        
        # Hide the empty subplot
        axs[2, 1].axis('off')
        
        # Show the plot
        plt.tight_layout()
        plt.show()

def main(args=None):
    rclpy.init(args=args)
    node = DataLogger()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
    node.plot_data()  # Plot the data once the program ends
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
