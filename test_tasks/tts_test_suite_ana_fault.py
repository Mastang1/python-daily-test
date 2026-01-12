import time, os, sys, logging
projectPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
variantInstPath = os.path.join(projectPath, "variant_instruments")
sys.path.append(projectPath)
sys.path.append(variantInstPath)
from tcs_magician import Magician as MG

from variant_instruments import *
from variant_instruments import VARIANT_STUB

class TcsTestSuiteAnaFault(MG):
    
    def tcs_test_ana_phy_p_break(self):
        """
                {   "用例名称": "tcs_test_ana_phy_p_break", \
            "用例编号": "TC001", \
            "功能": "模拟正信号线断路故障模式", \
            "故障类型":"模拟信号物理层故障", \
            "参数": "通道1",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_phy_fault(0, AMC9726_PHY_FUAULT_ENUM.P_SIGNAL_BREAK.value, 0)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS

    def tcs_test_ana_phy_n_break(self):
        """
                {   "用例名称": "tcs_test_ana_phy_n_break", \
            "用例编号": "TC002", \
            "功能": "模拟负信号线断路故障模式", \
            "故障类型":"模拟信号物理层故障", \
            "参数": "通道1",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:

            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_phy_fault(0, AMC9726_PHY_FUAULT_ENUM.N_SIGNAL_BREAK.value, 0)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_phy_pn_break(self):
        """
                {   "用例名称": "tcs_test_ana_phy_pn_break", \
            "用例编号": "TC003", \
            "功能": "模拟负信号线断路故障模式", \
            "故障类型":"模拟信号物理层故障", \
            "参数": "通道1",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_phy_fault(0, AMC9726_PHY_FUAULT_ENUM.P_N_SIGNAL_BREAK.value, 0)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_phy_pn_short(self):
        """
                {   "用例名称": "tcs_test_ana_phy_pn_short", \
            "用例编号": "TC004", \
            "功能": "模拟负信号线正负线短路故障模式", \
            "故障类型":"模拟信号物理层故障", \
            "参数": "通道1",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_phy_fault(0, AMC9726_PHY_FUAULT_ENUM.P_N_SHORT.value, 0)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_phy_p_resister(self):
        """
                {   "用例名称": "tcs_test_ana_phy_p_resister", \
            "用例编号": "TC005", \
            "功能": "模拟负信号线正信号线串接电阻", \
            "故障类型":"模拟信号物理层故障", \
            "参数": "通道1, 电阻值为1000Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_phy_fault(0, AMC9726_PHY_FUAULT_ENUM.P_SIGNAL_RESISTER.value, 0)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_phy_n_resister(self):
        """
                {   "用例名称": "tcs_test_ana_phy_n_resister", \
            "用例编号": "TC006", \
            "功能": "模拟负信号线正信号线串接电阻", \
            "故障类型":"模拟信号物理层故障", \
            "参数": "通道1, 电阻值为1000Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_phy_fault(0, AMC9726_PHY_FUAULT_ENUM.n_SIGNAL_RESISTER.value, 0)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_phy_pn_resister(self):
        """
                {   "用例名称": "tcs_test_ana_phy_pn_resister", \
            "用例编号": "TC007", \
            "功能": "模拟+-信号线并接电阻故障模式", \
            "故障类型":"模拟信号物理层故障", \
            "参数": "通道1, 电阻值为1000Ω",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_phy_fault(0, AMC9726_PHY_FUAULT_ENUM.P_N_RESISTER.value, 0)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set phy fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
#electronic fault test case
    def tcs_test_ana_elec_dc(self):
        """
            {   "用例名称": "tcs_test_ana_elec_dc", \
            "用例编号": "TC008", \
            "功能": "DC波形信号输出,频率值10KHz", \
            "故障类型":"模拟信号电气层故障", \
            "参数": "通道1, 频率10KHz,幅度±5V",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_elec_fault(0, 5, 10000, 0, 0, AMC9726_WAVE_FORM_ENUM.DC.value)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set electric fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_elec_sine(self):
        """
            {   "用例名称": "tcs_test_ana_elec_sine", \
            "用例编号": "TC009", \
            "功能": "正弦波形信号输出,频率值10KHz", \
            "故障类型":"模拟信号电气层故障", \
            "参数": "通道1, 频率10KHz,幅度±5V",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_elec_fault(0, 5, 10000, 0, 0, AMC9726_WAVE_FORM_ENUM.SINE.value)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set electric fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_elec_square(self):
        """
            {   "用例名称": "tcs_test_ana_elec_square", \
            "用例编号": "TC010", \
            "功能": "矩形波形信号输出,频率值10KHz", \
            "故障类型":"模拟信号电气层故障", \
            "参数": "通道1, 频率10KHz,幅度±5V",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_elec_fault(0, 5, 10000, 0, 0, AMC9726_WAVE_FORM_ENUM.SQUARE.value)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set electric fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_elec_triangle(self):
        """
            {   "用例名称": "tcs_test_ana_elec_triangle", \
            "用例编号": "TC011", \
            "功能": "三角波形信号输出,频率值10KHz", \
            "故障类型":"模拟信号电气层故障", \
            "参数": "通道1, 频率10KHz,幅度±5V",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_elec_fault(0, 5, 10000, 0, 0, AMC9726_WAVE_FORM_ENUM.TRIANGLE.value)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set electric fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_elec_pulse(self):
        """
            {   "用例名称": "tcs_test_ana_elec_pulse", \
            "用例编号": "TC012", \
            "功能": "脉冲信号形信号输出,频率值10KHz", \
            "故障类型":"模拟信号电气层故障", \
            "参数": "通道1, 频率10KHz,幅度±5V",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_elec_fault(0, 5, 10000, 0, 0, AMC9726_WAVE_FORM_ENUM.PULSE.value)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set electric fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS
            
    def tcs_test_ana_elec_rising_ramp(self):
        """
            {   "用例名称": "tcs_test_ana_elec_rising_ramp", \
            "用例编号": "TC013", \
            "功能": "上斜波形信号输出,频率值10KHz", \
            "故障类型":"模拟信号电气层故障", \
            "参数": "通道1, 频率10KHz,幅度±5V",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_elec_fault(0, 5, 10000, 0, 0, AMC9726_WAVE_FORM_ENUM.RISING_RAMP.value)

            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set electric fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS


#synchronization fault test case
    def tcs_test_ana_sync_sine(self):
        """
            {   "用例名称": "tcs_test_ana_sync_sine", \
            "用例编号": "TC015", \
            "功能": "双通道正弦波形信号输出,频率值10KHz", \
            "故障类型":"模拟信号电气层故障", \
            "参数": "通道1, 频率10KHz,幅度±5V",\
            "持续时间": "15s"}
        """
        dll_path = os.path.join(AMC9726_DLL_DIR, "AMC9726A-S03.dll")
        with VARIANT_AMC9726S3(dll_path, "TCPIP0::192.168.1.120::inst0::INSTR") as amc9726:
            if amc9726.is_connected() == STATE_ERROR:
                print("Connected to instrument failed.")
                return
            amc9726.set_log_level("DEBUG")
            amc9726.if_reset()
            ret = amc9726.if_set_elec_fault(0, 5, 10000, 0, 0, AMC9726_WAVE_FORM_ENUM.SINE.value)
            amc9726.if_set_sysch_mode()
            amc9726.if_start_fault()
            amc9726.if_delay_ms(15000)
            amc9726.if_stop_fault()
            if ret == STATE_ERROR:
                amc9726.vi_log("ERROR", "set electric fault mode error")
                return STATE_ERROR
            else:
                return STATE_SUCCESS