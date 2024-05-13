#ifndef AGV_H
#define AGV_H

class AGV
{
public:
    // 获取唯一实例的静态方法
    static AGV &getInstance();

    // 移动到point点
    int move(int point);

    // 返回AGV的数据
    int return_Data();

private:
    // 私有构造函数
    AGV() {}

    // 禁止复制构造函数和赋值运算符
    AGV(const AGV &) = delete;
    AGV &operator=(const AGV &) = delete;
};

#endif // AGV_H
