from CPS import CPSClient
import time

class Robot():
    def __init__(self):
        pass
    #机械臂设置初始化
    def init(self):
        self.cps = CPSClient()
        result = []
        IP = "192.168.15.150"
        port = 10003
        ret = self.cps.HRIF_Connect(0, IP, port)
        print(ret)

        # 需要设置的速度比
        dOverride = 0.6
        # 设置当前速度比
        nRet = self.cps.HRIF_SetOverride(0, 0, dOverride)

    #机械臂位置初始化
    def location_init(self):
        point = [30, 400, 150, -180, 0, -180]
        # 定义关节目标位置
        RawACSpoints = [0, 0, 90, 0, 90, 0]
        # 定义工具坐标变量
        sTcpName = "TCP"
        # 定义用户坐标变量
        sUcsName = "Base"
        # 定义运动速度
        dVelocity = 50
        # 定义运动加速度
        dAcc = 50
        # 定义过渡半径
        dRadius = 50
        # 定义是否使用检测 DI 停止
        nIsSeek = 0
        # 定义检测的 DI 索引
        nIOBit = 0
        # 定义检测的 DI 状态
        nIOState = 0
        # 执行路点运动
        nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                                   nIOBit, nIOState, '0')
        self.is_move()

    #判断机械臂是否在移动中
    def is_move(self):
        # result = []
        # nRet = self.cps.HRIF_ReadRobotState(0, 0, result)
        # # 读取状态
        # flag = result[0]
        # print(flag)
        # while 1:
        #     time.sleep(1)
        #     nRet = self.cps.HRIF_ReadRobotState(0, 0, result)
        #     if result[0] == "0":
        #         break;
        while True:
            result = []
            nRet = self.cps.HRIF_ReadRobotState(0, 0, result)
            if result and result[0] == "0":
                return False
            time.sleep(1)

    #机械臂转150度，1逆时针转过去，0顺时针转回来
    def rotate_150(self,i):
        nRet = self.cps.HRIF_MoveRelJ(0, 0, 0, i, 150)
        self.is_move()

    #机械臂抓取初始化
    def crawl_int(self):
        point = [-139, -346.5, 150, -180, 0, 0]
        # 定义关节目标位置
        RawACSpoints = [0, 0, 90, 0, 90, 0]
        # 定义工具坐标变量
        sTcpName = "TCP"
        # 定义用户坐标变量
        sUcsName = "Base"
        # 定义运动速度
        dVelocity = 50
        # 定义运动加速度
        dAcc = 50
        # 定义过渡半径
        dRadius = 50
        # 定义是否使用检测 DI 停止
        nIsSeek = 0
        # 定义检测的 DI 索引
        nIOBit = 0
        # 定义检测的 DI 状态
        nIOState = 0
        # 定义路点 ID
        stdCmdID = "1"
        # 执行路点运动
        nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                              nIOBit, nIOState, '0')
        self.ismove()

    def crawl(self,point, n_times):
        # Point = [ -50, -380, 60, -180, 0, 0]
        # point = [ -50, -380, 300, -180, 0, 0]
        # 松开东西
        nRet = self.cps.HRIF_WriteEndHoldingRegisters(0, 0, 0x09, 0x10, 0x03E8, 0x0003, [0x0009, 0xFF00, 0xFFFF])
        time.sleep(5)
        # 定义关节目标位置
        RawACSpoints = [0, 0, 90, 0, 90, 0]
        # 定义工具坐标变量
        sTcpName = "TCP"
        # 定义用户坐标变量
        sUcsName = "Base"
        # 定义运动速度
        dVelocity = 50
        # 定义运动加速度
        dAcc = 50
        # 定义过渡半径
        dRadius = 50
        # 定义是否使用检测 DI 停止
        nIsSeek = 0
        # 定义检测的 DI 索引
        nIOBit = 0
        # 定义检测的 DI 状态
        nIOState = 0
        # 定义路点 ID
        stdCmdID = "1"
        # 执行路点运动
        nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                              nIOBit, nIOState, '0')
        self.is_move()

        point[2] = 53
        nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                              nIOBit, nIOState, '0')
        self.is_move()

        # 夹东西
        nRet = self.cps.HRIF_WriteEndHoldingRegisters(0, 0, 0x09, 0x10, 0x03E8, 0x0003, [0x0009, 0x0000, 0xFFFF])
        print(nRet)
        time.sleep(2)

        point[2] = 125
        nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                              nIOBit, nIOState, '0')
        self.is_move()

        self.crawl_int()
        self.is_move()
        nRet = self.cps.HRIF_MoveRelJ(0, 0, 0, 0, int(120 + 20 * n_times))
        self.is_move()
        # 定义返回值空列表
        result = []
        # 读取当前实际位置信息
        nRet = self.cps.HRIF_ReadActPos(0, 0, result)
        time.sleep(1)
        point = [result[6], result[7], 30, result[9], result[10], result[11]]
        global my_global_arrays
        my_global_arrays.append(point)
        # point = [-230, 293, 30, -180, 0, int(-(120+20*n_times))]
        # 定义关节目标位置
        RawACSpoints = [0, 0, 0, 0, 0, 0]
        # 定义工具坐标变量
        sTcpName = "TCP"
        # 定义用户坐标变量
        sUcsName = "Base"
        # 定义运动速度
        dVelocity = 50
        # 定义运动加速度
        dAcc = 50
        # 定义过渡半径
        dRadius = 50
        # 定义是否使用检测 DI 停止
        nIsSeek = 0
        # 定义检测的 DI 索引
        nIOBit = 0
        # 定义检测的 DI 状态
        nIOState = 0
        # 定义路点 ID
        stdCmdID = "1"
        # 执行路点运动
        nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                              nIOBit, nIOState, '0')
        self.is_move()
        # 松开东西
        nRet = self.cps.HRIF_WriteEndHoldingRegisters(0, 0, 0x09, 0x10, 0x03E8, 0x0003, [0x0009, 0xFF00, 0xFFFF])
        time.sleep(3)

        # 向上移动避免撞到了
        point = [result[6], result[7], 150, result[9], result[10], result[11]]
        # point = [-230, 293,150, -180, 0, int(-(120+20*n_times))]
        nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                              nIOBit, nIOState, '0')
        self.is_move()

        # 转回去，准备继续抓
        nRet = self.cps.HRIF_MoveRelJ(0, 0, 0, 1, int(120 + 20 * n_times))
        self.is_move()

        # 放东西
        def put(self, point):
            point[2] = 130
            # 松开东西
            nRet = self.cps.HRIF_WriteEndHoldingRegisters(0, 0, 0x09, 0x10, 0x03E8, 0x0003, [0x0009, 0xFF00, 0xFFFF])
            time.sleep(5)
            # 定义关节目标位置
            RawACSpoints = [0, 0, 90, 0, 90, 0]
            # 定义工具坐标变量
            sTcpName = "TCP"
            # 定义用户坐标变量
            sUcsName = "Base"
            # 定义运动速度
            dVelocity = 50
            # 定义运动加速度
            dAcc = 50
            # 定义过渡半径
            dRadius = 50
            # 定义是否使用检测 DI 停止
            nIsSeek = 0
            # 定义检测的 DI 索引
            nIOBit = 0
            # 定义检测的 DI 状态
            nIOState = 0
            # 定义路点 ID
            stdCmdID = "1"
            # 执行路点运动
            nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                                       nIOBit, nIOState, '0')
            self.ismove()

            point[2] = 30
            nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                                       nIOBit, nIOState, '0')
            self.ismove()

            # 夹东西
            nRet = self.cps.HRIF_WriteEndHoldingRegisters(0, 0, 0x09, 0x10, 0x03E8, 0x0003, [0x0009, 0x0000, 0xFFFF])
            print(nRet)
            time.sleep(2)

            point[2] = 125
            nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                                       nIOBit, nIOState, '0')
            self.ismove()
            nRet = self.cps.HRIF_MoveRelJ(0, 0, 0, 1, 120)
            self.ismove()
            # 定义返回值空列表
            result = []
            # 读取当前实际位置信息
            nRet = self.cps.HRIF_ReadActPos(0, 0, result)
            time.sleep(1)
            point = [result[6], result[7], 30, result[9], result[10], result[11]]

            # point = [-230, 293, 30, -180, 0, int(-(120+20*n_times))]
            # 定义关节目标位置
            RawACSpoints = [0, 0, 0, 0, 0, 0]
            # 定义工具坐标变量
            sTcpName = "TCP"
            # 定义用户坐标变量
            sUcsName = "Base"
            # 定义运动速度
            dVelocity = 50
            # 定义运动加速度
            dAcc = 50
            # 定义过渡半径
            dRadius = 50
            # 定义是否使用检测 DI 停止
            nIsSeek = 0
            # 定义检测的 DI 索引
            nIOBit = 0
            # 定义检测的 DI 状态
            nIOState = 0
            # 定义路点 ID
            stdCmdID = "1"
            # 执行路点运动
            nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                                       nIOBit, nIOState, '0')
            self.ismove()
            # 松开东西
            nRet = self.cps.HRIF_WriteEndHoldingRegisters(0, 0, 0x09, 0x10, 0x03E8, 0x0003, [0x0009, 0xFF00, 0xFFFF])
            time.sleep(3)

            # 向上移动避免撞到了
            point = [result[6], result[7], 150, result[9], result[10], result[11]]
            # point = [-230, 293,150, -180, 0, int(-(120+20*n_times))]
            nRet = self.cps.HRIF_MoveL(0, 0, point, RawACSpoints, sTcpName, sUcsName, dVelocity, dAcc, dRadius, nIsSeek,
                                       nIOBit, nIOState, '0')
            self.ismove()

            # 转回去，准备继续抓
            nRet = self.cps.HRIF_MoveRelJ(0, 0, 0, 0, 120)
            self.ismove()

    def read(self):
        # 定义返回值空列表
        result = []
        # 读取关节实际电流
        nRet = self.cps.HRIF_ReadActJointCur(0, 0, result)
        # 读取关节实际电流变量
        dJ1 = float(result[0])
        dJ2 = float(result[1])
        dJ3 = float(result[2])
        dJ4 = float(result[3])
        dJ5 = float(result[4])
        dJ6 = float(result[5])
        return result