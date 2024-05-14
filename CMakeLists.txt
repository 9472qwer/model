# CMakeList.txt: Demo 的 CMake 项目，在此处包括源代码并定义
# 项目特定的逻辑。
#
cmake_minimum_required (VERSION 3.8)

project ("Demo")
set(CMAKE_C_FLAGS "$ENV{CFLAGS} -O2 -Wall -pthread")
set(CMAKE_CXX_FLAGS "$ENV{CFLAGS} -O2 -Wall -pthread -std=c++11")
set(CMAKE_INCLUDE_CURRENT_DIR ON)

file(GLOB_RECURSE mqtt_c ${CMAKE_CURRENT_SOURCE_DIR}/mqtt/*.cpp)
file(GLOB_RECURSE rob_c ${CMAKE_CURRENT_SOURCE_DIR}/rob/*.cpp)

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/mqtt)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/rob)
include_directories(
    /home/aa/miniconda3/envs/study/include/python3.8
)

set(ALL_COMPILE_SRC
    ${mqtt_c}
    ${rob_c}
)
link_directories(usr/local/lib)

# 将源代码添加到此项目的可执行文件。
# add_executable (mqttsend "mqttsend.cpp" ${ALL_COMPILE_SRC})
# add_executable (mqttrecv "mqttrecv.cpp" ${ALL_COMPILE_SRC})
add_executable (main "main.cpp" ${ALL_COMPILE_SRC})

# target_link_libraries(mqttsend -lpthread -lpaho-mqtt3a -lpaho-mqtt3as -lpaho-mqtt3c -lpaho-mqtt3cs -lssl -lcrypto)
# target_link_libraries(mqttrecv -lpthread -lpaho-mqtt3a -lpaho-mqtt3as -lpaho-mqtt3c -lpaho-mqtt3cs -lssl -lcrypto)
target_link_libraries(main -lpthread -lpaho-mqtt3a -lpaho-mqtt3as -lpaho-mqtt3c -lpaho-mqtt3cs -lssl -lcrypto
            /home/aa/miniconda3/envs/study/lib/libpython3.8.so
)
# TODO: 如有需要，请添加测试并安装目标。
