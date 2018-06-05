import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

class CreateProjectF2272():

	def __init__(self, project_path):

		# project_path is the whole path of the project
		# i.e. C:\MSP430F2272\Lab01
	    # folder and files need to be created in folder Lab01
	    # folder - .settings - *.prefs file (no modification needed)
	    # file   - .ccsproject (no modification needed)
	    # file   - .cdtproject (no modification needed)
	    # file   - lnk_msp430f2272.cmd (no modification needed)
	    # file   - MSP430F2272.ccxml (no modification needed)
	    # file   - UART.h (no modification needed)
	    # file   - UARTFuncs.c (no modification needed)
	    # file   - .cdtbuild (replace string "Lab0" to "project_name")
	    # file   - .cproject (replace string "Lab0" to "project_name")
	    # file   - .project (replace string "Lab0" to "project_name")
	    # file   - user_newproject.c -> user_<project_name>.c
		
		self.project_path = project_path + "\\"
		self.project_name = project_path.split("\\")[-1]

		# the path of .setting folder
		self.setting_path = self.project_path + ".settings\\"

		self.project_path_exist = None

		# create project folder and the .setting folder within the project folder
		if os.path.exists(self.setting_path):
			# warning of similar project has been created!

			messagebox.showwarning("Invalide Project name", "Project " + self.project_name.upper() + " or " + \
				                   self.project_name.lower() +  " or similar has been used! " + \
				                  "Please choose another project name!")

			self.project_path_exist = True
			"""
			print("Project " + self.project_name.upper() + " or " + \
				  self.project_name.lower() +  
				  " or similar has been used! Please choose another project name!")
			"""
		else:
			self.project_path_exist = False
			os.makedirs(self.setting_path)
			print(self.project_name + " project folder has been created successfully!")

	def copy_prefs_file(self):
		prefs_path = "/DefaultProjects/F2272DefaultProject/.settings"
		prefs_path = os.path.dirname(__file__) + '/' + '../' + prefs_path
		prefs_path = os.path.abspath(prefs_path)
		prefs_path = prefs_path + '\\org.eclipse.cdt.managedbuilder.core.prefs'
		shutil.copy(prefs_path, self.setting_path)
		print(".\\setting\\*.prefs file is created successfully!")

	# copy no modificatin files
	def copy_project_files(self):

		# file   - .ccsproject (no modification needed)
	    # file   - .cdtproject (no modification needed)
	    # file   - lnk_msp430f2272.cmd (no modification needed)
	    # file   - MSP430F2272.ccxml (no modification needed)
	    # file   - UART.h (no modification needed)
	    # file   - UARTFuncs.c (no modification needed)

	    src_dir = os.path.dirname(__file__) + '/' + '../' + "/DefaultProjects/F2272DefaultProject" 
	    src_dir = os.path.abspath(src_dir)

	    ccsproject_path = src_dir + "\\.ccsproject"
	    cdtproject_path = src_dir + "\\.cdtproject"
	    lnk_msp430f2272_path = src_dir + "\\lnk_msp430f2272.cmd"
	    MSP430F2272_path = src_dir + "\\MSP430F2272.ccxml"
	    UART_path = src_dir + "\\UART.h"
	    UARTFuncs_path = src_dir + "\\UARTFuncs.c"

	    shutil.copy(ccsproject_path, self.project_path)
	    shutil.copy(cdtproject_path, self.project_path)
	    shutil.copy(lnk_msp430f2272_path, self.project_path)
	    shutil.copy(MSP430F2272_path, self.project_path)
	    shutil.copy(UART_path, self.project_path)
	    shutil.copy(UARTFuncs_path, self.project_path)

	    print(".ccsproject file is created successfully!")
	    print(".cdtproject file is created successfully!")
	    print("lnk_msp430f2272.cmd file is created successfully!")
	    print("MSP430F2272.ccxml file is created successfully!")
	    print("UART.h file is created successfully!")
	    print("UARTFuncs.c file is created successfully!")


	def create_project_files(self):

		# file   - user_newproject.c -> user_<project_name>.c
		# file   - .project (replace string "Lab0" to "project_name")
	    # file   - .cdtbuild (replace string "Lab0" to "project_name")
	    # file   - .cproject (replace string "Lab0" to "project_name")

	    src_dir = os.path.dirname(__file__) + '/' + '../' + "/DefaultProjects/F2272DefaultProject" 
	    src_dir = os.path.abspath(src_dir)

	    user_src_c_path = src_dir + "\\user_newproject.c" 
	    user_dst_c_path = self.project_path + "user_" + self.project_name + ".c"
	    shutil.copy(user_src_c_path, user_dst_c_path)
	    print("user_" + self.project_name + ".c file is created successfully!")

	    # copy and modify .project file
	    project_file_path = src_dir + "\\.project"
	    shutil.copy(project_file_path, self.project_path)
	    with open(self.project_path + "\\.project", "r") as proj_f:
	    	project_file_content = proj_f.read().replace('Lab0', self.project_name)
	    with open(self.project_path + "\\.project", "w") as proj_f:
	    	proj_f.write(project_file_content)
	    print(".project file is created successfully!")

	    # copy and modify .cdtbuild file
	    cdtbuild_path = src_dir + "\\.cdtbuild"
	    shutil.copy(cdtbuild_path, self.project_path)
	    with open(self.project_path + "\\.cdtbuild", "r") as cdtbuild_f:
	    	cdtbuild_content = cdtbuild_f.read().replace('Lab0', self.project_name)
	    with open(self.project_path + "\\.cdtbuild", "w") as cdtbuild_f:
	    	cdtbuild_f.write(cdtbuild_content)
	    print(".cdtbuild file is created successfully!")

	    # copy and modify .cproject file
	    cproject_path = src_dir + "\\.cproject"
	    shutil.copy(cproject_path, self.project_path)
	    with open(self.project_path + "\\.cproject", "r") as cproject_f:
	    	cproject_content = cproject_f.read().replace('Lab0', self.project_name)
	    with open(self.project_path + "\\.cproject", "w") as cproject_f:
	    	cproject_f.write(cproject_content)
	    print(".cproject file is created successfully!")


	def create_project(self):

		if not self.project_path_exist:
			self.create_project_files()
			self.copy_project_files()
			self.copy_prefs_file()
			print("All done!\n")
		





		
		
