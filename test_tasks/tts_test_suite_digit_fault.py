import time, os, sys, logging
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
variantInstPath = os.path.join(projectPath, "variant_instruments")
sys.path.append(projectPath)
sys.path.append(variantInstPath)
from tcs_magician import Magician as MG

from variant_instruments import *
from variant_instruments import VARIANT_STUB

class TcsTestSuiteCANFault(MG):
    def tcs_test_Digi_phy_break(self):
        """
            {   "用例名称": "tcs_test_Digi_phy_break", \
            "用例编号": "TC001", \
            "功能": "模拟数字信号故障注入器通道1的断路故障", \
            "故障类型":"物理层", \
            "参数": "chan=2",\
            "持续时间": "30s"}
        """
        dll_path = os.path.join(AMC9727_DLL_DIR, "AMC9727A.dll")
        with VARIANT_AMC9727(dll_path, "TCPIP0::192.168.1.121::inst0::INSTR") as amc9727:
            if amc9727.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return

            time.sleep(2)
            amc9727.if_reset()
            amc9727.if_set_resis_chan()
            amc9727.if_set_wire_broken()
            amc9727.if_start_fault()
            time.sleep(30)
            amc9727.if_stop_fault()

    def tcs_test_Digi_phy_bridge(self):
        """
            {   "用例名称": "tcs_test_Digi_phy_bridge", \
            "用例编号": "TC002", \
            "功能": "模拟数字信号故障注入器通道6和10的桥接故障", \
            "故障类型":"物理层", \
            "参数": "chan=6-10",\
            "持续时间": "30s"}
        """
        dll_path = os.path.join(AMC9727_DLL_DIR, "AMC9727A.dll")
        with VARIANT_AMC9727(dll_path, "TCPIP0::192.168.1.121::inst0::INSTR") as amc9727:
            if amc9727.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return

            amc9727.if_self_test()
            amc9727.if_reset()
            time.sleep(5)
            amc9727.if_set_bridge_chans(6, 10, 100)
            amc9727.if_start_fault()
            time.sleep(30)
            amc9727.if_stop_fault()
        return STATE_SUCCESS
    
    def tcs_test_Digi_elec_5v(self):
        """
            {   "用例名称": "tcs_test_Digi_elec_5v", \
            "用例编号": "TC003", \
            "功能": "模拟数字信号故障注入器通道电压输出", \
            "故障类型":"电气层", \
            "参数": "chan=0/1/15",\
            "持续时间": "30s"}
        """
        dll_path = os.path.join(AMC9727_DLL_DIR, "AMC9727A.dll")
        with VARIANT_AMC9727(dll_path, "TCPIP0::192.168.1.121::inst0::INSTR") as amc9727:
            if amc9727.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return

            time.sleep(2)
            amc9727.if_reset()
            chan_list = [0]*64

            chan_list[0] = 1
            chan_list[1] = 1
            chan_list[15] = 1
            amc9727.if_set_chan_con_or_reverse(chan_list)
            amc9727.if_set_val_con_or_reverse(mode=1)
            amc9727.if_set_pwr_chon_or_reverse()
            amc9727.if_start_fault()
            time.sleep(30)
            amc9727.if_stop_fault()