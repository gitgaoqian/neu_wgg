cmake_minimum_required(VERSION 2.8.3)
project(neu_wgg)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  message_runtime
  roscpp
  rospy

)
add_message_files(
  FILES
  env.msg
  angle.msg
  location.msg
  env_and_angle.msg


)


add_service_files(
   FILES
call.srv
call3.srv
#   Service2.srv
)

generate_messages(
   DEPENDENCIES
   std_msgs  # Or other packages containing msgs
)


catkin_package(

)


include_directories(
  ${catkin_INCLUDE_DIRS}
)





