#include "robot.h"
#include <Python.h>
#include <iostream>

Robot::Robot()
{
    // 1、初始化python接口
    Py_Initialize();
    if (!Py_IsInitialized())
    {
        std::cout << "python init failed" << std::endl;
    }

    // 2、初始化python系统文件路径，保证可以访问到 .py文件
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('/home/book/Myproject/script')");

    // 3、调用python文件名，不用写后缀
    PyObject *module = PyImport_ImportModule("Robot");
    if (module == nullptr)
    {
        std::cout << "module not found: test3" << std::endl;
    }
    // 4、获取类
    PyObject *cls = PyObject_GetAttrString(module, "Robot");
    if (!cls)
    {
        std::cout << "class not found: Person" << std::endl;
    }

    PyObject *args = PyTuple_New(0);

    obj = PyEval_CallObject(cls, args);

    // 3、调用python文件名，不用写后缀
    module = PyImport_ImportModule("Detect");
    if (module == nullptr)
    {
        std::cout << "module not found: test3" << std::endl;
    }
    get_Python();
    PyObject_CallObject(ini, nullptr);
}

void Robot::get_Python()
{
    init = PyObject_GetAttrString(obj, "init");
    location_init = PyObject_GetAttrString(obj, "location_init");
    is_move = PyObject_GetAttrString(obj, "is_move");
    rotate_150 = PyObject_GetAttrString(obj, "rotate_150");
    crawl_int = PyObject_GetAttrString(obj, "crawl_int");
    crawl = PyObject_GetAttrString(obj, "crawl");
    read = PyObject_GetAttrString(obj, "read");

    ini = PyObject_GetAttrString(module, "ini");
    mainfunc = PyObject_GetAttrString(module, "mainfunc");
}

Robot::~Robot()
{ // 9、结束python接口初始化
    Py_Finalize();
};

// 获取单例实例的静态方法
Robot &Robot::getInstance()
{
    static Robot instance; // 在第一次调用时初始化
    return instance;
}

//机械臂初始化
int Robot::rinit()
{
    PyObject_CallObject(init, nullptr);
    PyObject_CallObject(location_init, nullptr);
}
//抓取扫描仪的零件
void Robot::catch_scanner()
{
    // nihao
}
//抓取货架的零件
void Robot::catch_shelf()
{
    //旋转150°，准备开始抓取
    PyObject *args = PyTuple_New(1);
    PyTuple_SetItem(args, 0, Py_BuildValue("i", 1));
    PyObject_CallObject(rotate_150, args);
    //机械臂抓取初始化
    PyObject_CallObject(crawl_int, nullptr);
    //识别函数
    PyObject *ret = PyObject_CallObject(mainfunc, nullptr); // 调用 Python 函数，得到返回值
    //将返回的数据存入data中
    if (PyList_Check(ret))
    {
        int outerSize = PyList_Size(ret); // 获取外层列表的长度
        for (int i = 0; i < outerSize; ++i)
        {
            PyObject *innerList = PyList_GetItem(ret, i); // 获取外层列表的每个元素
            if (PyList_Check(innerList))
            {
                int innerSize = PyList_Size(innerList); // 获取内层列表的长度
                std::vector<int> innerVec;              // 创建一个内层 vector，用于存储内层列表的数据
                for (int j = 0; j < innerSize; ++j)
                {
                    PyObject *item = PyList_GetItem(innerList, j); // 获取内层列表的每个元素
                    // 这里假设内层列表的每个元素都是整数类型
                    if (PyLong_Check(item))
                    {
                        long value = PyLong_AsLong(item); // 将 Python 整数转换成 C++ long 型
                        innerVec.push_back(value);        // 将转换后的值存入内层 vector
                    }
                }
                // 将填充好的内层 vector 存入外层 vector
                data.push_back(innerVec);
            }
        }
    }
    //开始抓取,一共抓取vector容器的size次
    int index = 0;
    for (auto vec : data)
    {
        PyObject *list_obj = PyList_New(vec.size());
        for (size_t i = 0; i < vec.size(); ++i)
        {
            PyList_SetItem(list_obj, i, Py_BuildValue("i", vec[i]));
        }
        // 创建一个长度为 2 的元组
        PyObject *args = PyTuple_New(2);
        // 在第一个位置插入 vector<int> 数组
        PyTuple_SetItem(args, 0, list_obj);
        // 在第二个位置插入整数值
        PyTuple_SetItem(args, 1, Py_BuildValue("i", index));
        PyObject_CallObject(crawl_int, args);
        index++;
    }
    //旋转150°回去
    PyObject *args = PyTuple_New(1);
    PyTuple_SetItem(args, 0, Py_BuildValue("i", 0));
    PyObject_CallObject(rotate_150, args);
    // // i表示转换成int型变量。
    // // 在这里，最需要注意的是：PyArg_Parse的最后一个参数，必须加上“&”符号
    // PyArg_Parse(ret, "i", &result);
    // std::cout << "return is " << result << std::endl;
}
//放置一个零件到3D扫描台
void Robot::put_scanner()
{
}
//放置一个零件到货架
void Robot::put_shelf()
{
}
//返回机械臂的数据
void Robot::return_data()
{
}