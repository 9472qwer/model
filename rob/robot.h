#include <vector>

class Robot
{
public:
    static Robot &getInstance();

    // 将拷贝构造函数和拷贝赋值运算符声明为私有，以防止复制对象
    Robot(Robot const &) = delete;
    void operator=(Robot const &) = delete;

    //机械臂初始化
    int rinit();
    //抓取扫描仪的零件
    void catch_scanner();
    //抓取货架的零件
    void catch_shelf();
    //放置一个零件到3D扫描台
    void put_scanner();
    //放置一个零件到货架
    void put_shelf();
    //返回机械臂的数据
    void return_data();
    //返回python函数
    void get_Python();

private:
    //将构造函数声明为私有，以防止外部代码创建新实例
    Robot();
    ~Robot();
    // 6、根据类名实例化对象
    PyObject *obj;

    PyObject *init;
    PyObject *location_init;
    PyObject *is_move;
    PyObject *rotate_150;
    PyObject *crawl_int;
    PyObject *crawl;
    PyObject *read;
    //识别到的零件的位置数组
    std::vector<std::vector<int>> data;
};