#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
void get_shell(){
system("/bin/sh");
}
void check()
{
char buf[16];
scanf("%s", buf);
if (!strcmp(buf, "250382"))
printf("Password OK :)\n");
else
printf("Invalid Password!\n");
}
int main(int argc, char *argv[])
{
setreuid(geteuid(), geteuid());
printf("Pwn basic\n");
printf("Password:");
check();
return 0;
}
