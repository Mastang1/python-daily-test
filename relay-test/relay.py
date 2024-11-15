import os, sys, subprocess
curPath = os.path.dirname(os.path.abspath(__file__))
cmdPath = os.path.join(curPath, 'CommandApp_USBRelay')

cmdSuccess = 0
cmdFailure = 1

class TfcRelay(object):
    
    def commandProc(self, sn, cmd, channel):
        strCmd = cmdPath + ' ' + sn.strip() + ' ' + cmd + ' ' + str(channel)
        print(strCmd)
        ret = os.system(strCmd)
        print(ret)
        # subprocess.Popen(strCmd)

if __name__ == '__main__':
    
    TfcRelay().commandProc('QAAMZ', sys.argv[1], 255)