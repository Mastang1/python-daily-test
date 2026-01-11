import time, os, sys, logging
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
variantInstPath = os.path.join(projectPath, "variant_instruments")
sys.path.append(projectPath)
sys.path.append(variantInstPath)
from tcs_magician import Magician as MG

from variant_instruments import *
from variant_instruments import VARIANT_STUB

class TcsTestSuiteCANFault(MG):
    
    def tcs_test_CAN_phy_p_break(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_p_break", \
            "用例编号": "TC001", \
            "功能": "模拟正信号线断路故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "无",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.P_SIGNAL_BREAK.value,0)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS

    def tcs_test_CAN_phy_n_break(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_n_break", \
            "用例编号": "TC002", \
            "功能": "模拟负信号线断路故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "无",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.N_SIGNAL_BREAK.value,0)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS

    def tcs_test_CAN_phy_pn_short(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_pn_short", \
            "用例编号": "TC003", \
            "功能": "模拟CAN总线正负信号短路故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "无",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.P_N_SHORT.value,0)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS

    def tcs_test_CAN_phy_p_resister_120(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_p_resister_120", \
            "用例编号": "TC004", \
            "功能": "模拟CAN总线正信号串接电阻故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "120Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.P_SIGNAL_RESISTER.value,120)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_CAN_phy_p_resister_200(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_p_resister_200", \
            "用例编号": "TC005", \
            "功能": "模拟CAN总线正信号串接电阻故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "200Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.P_SIGNAL_RESISTER.value,200)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_CAN_phy_n_resister_120(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_n_resister_120", \
            "用例编号": "TC006", \
            "功能": "模拟CAN总线负信号串接电阻故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "120Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.N_SIGNAL_RESISTER.value,120)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_CAN_phy_n_resister_200(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_n_resister_200", \
            "用例编号": "TC007", \
            "功能": "模拟CAN总线负信号串接电阻故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "200Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.N_SIGNAL_RESISTER.value,200)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_CAN_phy_pn_resister_120(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_pn_resister_120", \
            "用例编号": "TC008", \
            "功能": "模拟CAN总线+-信号串接电阻故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "120Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.P_SIGNAL_RESISTER.value,120)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_CAN_phy_pn_resister_200(self):
        """
                {   "用例名称": "tcs_test_CAN_phy_pn_resister_200", \
            "用例编号": "TC009", \
            "功能": "模拟CAN总线+-信号串接电阻故障模式", \
            "故障类型":"CAN总线物理层故障", \
            "参数": "200Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9730_DLL_DIR, "AMC9730.dll")
        with VARIANT_AMC9730(dll_path, "TCPIP0::192.168.1.30::inst0::INSTR") as amc9730:
            if amc9730.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9730.set_log_level("DEBUG")
            amc9730.if_reset()
            ret = amc9730.if_set_phy_fault_mode(AMC9730_PHY_FUAULT_ENUM.P_SIGNAL_RESISTER.value,200)
            amc9730.if_delay_ms(15000)
            if ret == STATE_ERROR:
                amc9730.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
# start set CAN electric fault mode test case:


