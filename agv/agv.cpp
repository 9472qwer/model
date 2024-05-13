#include "agv.h"

// 获取唯一实例的静态方法
AGV &AGV::getInstance()
{
    static AGV instance; // 声明静态实例
    return instance;
}

// 移动到point点
int AGV::move(int point)
{
    // 实现移动功能
    return 0;
}

// 返回AGV的数据
int AGV::return_Data()
{
    // 返回AGV的数据
    return 0;
}
