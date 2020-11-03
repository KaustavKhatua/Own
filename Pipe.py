import os, time 
def child(pipeout):     
	zzz = 1     
	while 1:        
		print('A')
		# print('Entered child')
		time.sleep(2)                          # make parent wait
		os.write(pipeout, bytes(f'{zzz}', 'utf-8'))     # send to parent       
		print('Written to Pipeline')  
		zzz = (zzz+1)                        # goto 0 after 4 

def parent( ):     
	pipein, pipeout = os.pipe( )                  # make 2-ended pipe     
	if os.fork( ) == 0:                           # copy this process         
		child(pipeout)                             # in copy, run child     
	else:                                         # in parent, listen to pipe         
		while 1:             
			line = os.read(pipein, 32)           # blocks until data sent 
			# print('Read from Pipeline')
			line = line.decode('utf-8') 
			print(line)           
			time.sleep(1)
			# print(f'Parent {os.getpid()} got {line} at {time.time( )}')

parent( ) 

# https://flylib.com/books/en/2.726.1.48/1/