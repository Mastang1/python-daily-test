import pyvisa
import pyvisa.shell
# rm = pyvisa.ResourceManager('@py')
# instru_list = rm.list_resources()
# print(instru_list)

# inst = rm.open_resource(instru_list[0])
# print(inst.query("*IDN?"))

pyvisa.shell.VisaShell(library_path='@py').cmdloop()