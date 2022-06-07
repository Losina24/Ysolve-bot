# Nombre: nav_to_waypoints.py
# Autor: Ysolve
# Descripción: Script con la lógica necesaria para que el robot se pueda desplazar entre distintos puntos definidos en el mapa

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped

 
class NavToPose(Node):
    '''
    Nodo que se encarga de navegar a varios puntos

    Atributes:
        self.follow_waypoints_client: Accion de FollowWaypoints
    '''

    def __init__(self):
        super().__init__('nav_to_waypoints_node')
        self.waypoint = 0
        self.get_logger().info('2')

        self.follow_waypoints_client = ActionClient(self, FollowWaypoints, '/FollowWaypoints')

    def followWaypoints(self, poses):
        '''
        Nodo que se encarga de navegar a varios puntos

        params:
            poses: Array de poses para followWaypoints
        '''
        # Sends a `FollowWaypoints` action request
        self.get_logger().info("Waiting for 'FollowWaypoints' action server")
        while not self.follow_waypoints_client.wait_for_server(timeout_sec=1.0):
            self.get_logger().info("'FollowWaypoints' action server not available, waiting...")

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = poses

        self.get_logger().info('Following ' + str(len(goal_msg.poses)) + ' goals.' + '...')
        send_goal_future = self.follow_waypoints_client.send_goal_async(goal_msg,
                                                                        self._feedbackCallback)
        rclpy.spin_until_future_complete(self, send_goal_future)
        self.goal_handle = send_goal_future.result()

        if not self.goal_handle.accepted:
            self.error('Following ' + str(len(poses)) + ' waypoints request was rejected!')
            return False

        self.result_future = self.goal_handle.get_result_async()
        return True

    def _feedbackCallback(self, msg):
        self.get_logger().info('Received action feedback message')
        self.feedback = msg.feedback
        return


def main(args=None):

    rclpy.init(args=args)
  
    action_client = NavToPose()
    goal_poses = []
    
    # Crear la posicion de tipo PoseStamped (para pasar al Goal de la accion NavigateToPose)
    goal_pose = PoseStamped()
    # Header
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = action_client.get_clock().now().to_msg()
    #Pose
    goal_pose.pose.position.x = 0.5
    goal_pose.pose.position.y = -1.2
    goal_pose.pose.orientation.w = 1.0
    goal_poses.append(goal_pose)

    goal_pose = PoseStamped()
    # Header
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = action_client.get_clock().now().to_msg()
    #Pose
    goal_pose.pose.position.x = 2.2
    goal_pose.pose.position.y = -2.0
    goal_pose.pose.orientation.w = 1.0
    goal_poses.append(goal_pose)
    
    action_client.followWaypoints(goal_poses)
    
    #rclpy.spin(action_client)
    


if __name__ == '__main__':
    main()
