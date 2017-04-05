#!/usr/bin/python
__Author__ = 'Julen Dieguez'

import argparse, psutil, subprocess, shlex, pygame, time, sys

pygame.init()

pcsx2Process = None
userWantsQuit = False
selectButton = 0
startButton = 3

def exit_program():
	pygame.quit()
	sys.exit()

def check_joysticks():
	if pygame.joystick.get_count() == 0:
		print("No controller found")
		exit_program()
	else:
		joystick = pygame.joystick.Joystick(0)
		joystick.init()

#Launch pcsx2 
def launch_pcsx2():
	process_id = subprocess.Popen(shlex.split(args.pcsx2), shell=False).pid
	global pcsx2Process
	pcsx2Process = psutil.Process(pid=process_id)
#kill pcsx2
def kill_pcsx2():
	#Iterate all subprocesses to kill them
	for s in pcsx2Process.children(recursive=True):
		s.terminate()
	pcsx2Process.terminate()
	global userWantsQuit
	userWantsQuit = True

check_joysticks()
joystick = pygame.joystick.Joystick(0)

#Argument that defines the process to launch and kill
parser = argparse.ArgumentParser(description='Emulationstation pcsx2 handler')
parser.add_argument('--pcsx2', help='Path to pcsx2 + ROM path')
args = parser.parse_args()

if args.pcsx2:
	launch_pcsx2()
else:
	print("no process defined...")
	exit_program()

#Program Loop
while userWantsQuit == False:
	#Check if start and select buttons are pressed simultaneously
	if joystick.get_button(startButton) and joystick.get_button(selectButton):
		kill_pcsx2()
	# loop through events, if window shut down, quit program
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit_program()
	time.sleep(0.25)
exit_program()
