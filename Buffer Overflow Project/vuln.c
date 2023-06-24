//vuln.c
#include <stdio.h> 
#include <string.h>

int exploitable(char *arg);

int main(int argc, char **argv) {     		//argc: 1 argv: 0x7fffffffdd08 
	// Make some stack information     		//*argv: 0x7fffffffe074 address of vuln.c
											//and **argv: 47 address of '/'

//callstack: main(int argc, char ** argc)
	char a[100], b[100], c[100], d[100];    //declares 4 char arrays 
											//a is a pointer to a character array that 
											//has 8 bit or 1 byte, meaning that a is 800 bits long 
											//the same goes for b-d
											//this means on a 64-bit machine, we have 13 blocks of data 
											//for 832 bits in total allocation		
	// Call the exploitable function     
	exploitable(argv[1]);     				//creates buffer char array with 10 elements 
											//we have to use 2 blocks of data 128 bits for this allocation
											//this is where we will most likely want to overload
											//because the return is to follow
											//the typical stack as described in Stack Smashing:
											//[buffer][sfp][return][local variables]
											//we are looking to access the return address so that we can 
											//run a shell, this means we should be away from the return address by 
											//return = &buffer + sizeof(buffer) + sizeof(sfp) 
											
	// Return: everything is OK     
	return(0); 
}

int exploitable(char *arg) {  
	// Make some stack space
	char buffer[10];  
	// Now copy the buffer  
	strcpy(buffer, arg);  											//this allows for a major vulnerability
																	//we should be using strncpy so that we have a restriction of how much we can copy
	printf("The buffer says .. [%s/%p].\n", buffer, &buffer);  
	// Return: everything fun  
	return(0); 
}

