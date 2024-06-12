from colors import colors
from BF import bruteforce
from BM import bm_match
from KMP import KMPSolve
from datetime import datetime
from process_titles import find_titles
import os, platform

# Clear the screen
if platform.system() == "Windows":
	os.system("cls")
else:
	os.system("clear")

# Input prompt
istring: str = input(f"{colors.YELLOW}Keywords to find{colors.END} {colors.BOLD}{colors.RED}(Case-Sensitive){colors.END}: ")

# start_url can be changed to something else like "https://informatika.stei.itb.ac.id/~rinaldi.munir/Matdis/matdis.htm"
# if you want to use this tool for searching titles in the IF2120 Matematik Diskrit course
start_url: str = "https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/stmik.htm"
target_pattern = r".*[Mm]akalah.*\.htm$"

titles = find_titles(start_url, target_pattern)

print(f"{colors.PURPLE}Title containing the keyword{colors.END} \"{colors.RED}{istring}{colors.END}\":")
for title, link in titles:
	if bm_match(title, istring):
		colored_title = title.replace(istring, f"{colors.BOLD}{colors.RED}{istring}{colors.END}")
		print(colored_title, end=f"\n{colors.YELLOW}{link}{colors.END}\n\n")

# Benchmark
print(f"{colors.PURPLE}Benchmark{colors.END}:")
startTime = datetime.now()
for title, link in titles:
	if bruteforce(title, istring):
		pass
endTime = datetime.now()
print(f"Brute Force time taken: {(endTime-startTime).total_seconds()*1000} ms")

startTime = datetime.now()
for title, link in titles:
	if KMPSolve(title, istring):
		pass
endTime = datetime.now()
print(f"KMP time taken: {(endTime-startTime).total_seconds()*1000} ms")

startTime = datetime.now()
for title, link in titles:
	if bm_match(title, istring):
		pass
endTime = datetime.now()
print(f"BM Time taken: {(endTime-startTime).total_seconds()*1000} ms")
