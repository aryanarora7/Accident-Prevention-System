Exercise 3 - Implementation of Shared memory and Inter-process communication using 
pipes
Practice programs
Program 1: Implementation of IPC Using Shared Memory Through I/O System Calls
a) iosys1.c
#include <unistd.h>
#include <fcntl.h>
int main()
{
size_t filedesc = open("test.txt", O_WRONLY | O_APPEND);
if(filedesc < 0)
return 1;
if(write(filedesc,"This will be output to test.txt\n", 32) != 32)
{
write(2,"There was an error writing to test.txt\n",39);
return 1;
}
return 0;
}
b) iosys2.c
#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#define BUFFERSIZE 1024
int main(void)
{
char sbuf[BUFFERSIZE];
int fd;
if((fd=open("test.txt",0660))==-1)
{
printf("Cannot open file!\n");
exit(1);
}
read(fd,sbuf,BUFFERSIZE);
printf("%s\n",sbuf);
close(fd);
}
OUTPUT:
$ cc iosys1.c
$ ./a.out test.txt
$ cat test.txt
This will be output to test.txt
$cc iosys2.c
$./a.out
This will be output to test.txt
Program 2: Implementation of IPC Using Shared Memory Through Pipes System Calls
#include<stdio.h> 
#include<stdlib.h>
#include<unistd.h>
int main() 
{
int pid,pfd[2],n,a,b,c;
if(pipe(pfd)==-1)
{ 
printf("\nError in pipe connection\n");
exit(1);
}
pid=fork();
if(pid>0)
{
printf("\nParent Process");
printf("\n\n\tFibonacci Series");
printf("\nEnter the limit for the series:"); 
scanf("%d",&n); 
close(pfd[0]);
write(pfd[1],&n,sizeof(n)); 
close(pfd[1]); 
exit(0);
}
else
{
close(pfd[1]); 
read(pfd[0],&n,sizeof(n));
printf("\nChild Process"); 
a=0;
b=1; 
close(pfd[0]); 
printf("\nFibonacci Series is:"); 
printf("\n\n%d\n%d",a,b); 
while(n>2)
{
c=a+b;
printf("\n%d",c); a=b; b=c; n--;
}
}
printf(“\n”);
}
OUTPUT
c3104068@rmk-desktop:~$ g++ ipc.c
c3104068@rmk-desktop:~$ ./a.out
Parent Process
Fibonacci Series
Enter the limit for the series:8
Child Process
Fibonacci Series is: 0 1 1 2 3 5 8 13
Program 3:. Implementation of IPC Using Message Passing System Calls
(2 terminals)
3 a) CHAT PROGRAM – 1
#include<stdio.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<unistd.h>
#include<string.h>
int main()
{
int mid;
char mess[20];
printf("\n\n ENTER PROCESS COMMUNICATION USING MESSAGE QUEUE...");
mid=msgget(27,IPC_CREAT|0777);
if(mid==-1)
{
printf("\n\t invalid message id,,");
exit(1);
}
printf("\n\t Enter the message text:");
scanf("%s",mess);
msgsnd(mid,mess,strlen(mess),0);
printf("\n\n Message has been sent..\n");
printf("\n The sent message is:%s\n",mess);
return 0;
}
OUTPUT:
ENTER PROCESS COMMUNICATION USING MESSAGE QUEUE…
Enter the message text: Hello
Message has been sent..
The sent message is : Hello
3 b) CHAT PROGRAM – 2
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>
#include<unistd.h>
#include<string.h>
int main()
{
int mid;
char mess[20];
printf("\n\n PROCESS COMMUNICATION USING MESSAGE QUEUE...");
mid=msgget(27,IPC_CREAT|0777);
if(mid==-1)
{
printf("\n\t invalid message id....");
exit(1);
}
msgrcv(mid,mess,100,0,0);
printf("\n The received message is:%s\n",mess);
return 0;
}
OUTPUT:
PROCESS COMMUNICATION USING MESSAGE QUEUE….
The received message is : hai
Program 4: Inter Process Communication Using Message Queues /Pipes
(2 terminals)
4 a) Writer Process
// C Program for Message Queue (Writer Process)
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#define MAX 10
// structure for message queue
struct mesg_buffer {
long mesg_type;
char mesg_text[100];
} message;
int main()
{
key_t key;
int msgid;
// ftok to generate unique key
key = ftok("progfile", 65);
// msgget creates a message queue
// and returns identifier
msgid = msgget(key, 0666 | IPC_CREAT);
message.mesg_type = 1;
printf("Write Data : ");
fgets(message.mesg_text,MAX,stdin);
// msgsnd to send message
msgsnd(msgid, &message, sizeof(message), 0);
// display the message
printf("Data send is : %s \n", message.mesg_text);
return 0;
}
4 b) Reader process
// C Program for Message Queue (Reader Process)
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
// structure for message queue
struct mesg_buffer {
long mesg_type;
char mesg_text[100];
} message;
int main()
{
key_t key;
int msgid;
// ftok to generate unique key
key = ftok("progfile", 65);
// msgget creates a message queue
// and returns identifier
msgid = msgget(key, 0666 | IPC_CREAT);
// msgrcv to receive message
msgrcv(msgid, &message, sizeof(message), 1, 0);
// display the message
printf("Data Received is : %s \n",message.mesg_text);
// to destroy the message queue
msgctl(msgid, IPC_RMID, NULL);
return 0;
}
Exercise 4 - Implement multi-threading using the Pthread library
Practice programs
Program 1: Program to demonstrate the basic pthread functions
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> //Header file for sleep(). 
#include <pthread.h>
// A normal C function that is executed as a thread
// when its name is specified in pthread_create()
void *myThreadFun(void *vargp)
{
sleep(5);
printf("Printing GeeksQuiz from Thread \n");
return NULL;
}
int main()
{
pthread_t thread_id;
printf("Before Thread\n");
pthread_create(&thread_id, NULL, myThreadFun, NULL);
pthread_join(thread_id, NULL);
printf("After Thread\n");
exit(0);
}
Program 2: C program to show multiple threads with global and static variables
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
// Let us create a global variable to change it in threads
int g = 0;
// The function to be executed by all threads
void *myThreadFun(void *vargp)
{
// Store the value argument passed to this thread
int *myid = (int *)vargp;
// Let us create a static variable to observe its changes
static int s = 0;
// Change static and global variables
++s; ++g;
// Print the argument, static and global variables
printf("Thread ID: %d, Static: %d, Global: %d\n", *myid, ++s, ++g);
}
int main()
{
int i;
pthread_t tid;
// Let us create three threads
for (i = 0; i < 3; i++)
pthread_create(&tid, NULL, myThreadFun, (void *)&tid);
pthread_exit(NULL);
return 0;
}
Program 3: Multithreading Using Pthreads library
// To calculate the sum of non-negative integer values.
#include<pthread.h>
#include<stdio.h>
int sum;
/* This ‘sum’ is shared by the thread(s) */
void *runner(void *param);
/* threads call this function */
int main(int argc, char *argv[]){
pthread_t tid;
/* the thread identifier */
pthread_attr_t attr;
/* set of thread attributes */
if (argc != 2){
fprintf(stderr,"usage: a.out");
return -1;
}
if (atoi(argv[1]) < 0){
fprintf(stderr,"%d must be >= 0",atoi(argv[1])); 
return -1;
}
/* get the default attributes */
pthread_attr_init(&attr);
/* create the thread */
pthread_create(&tid,&attr,runner,argv[1]);
/* wait for the thread to exit */
pthread_join(tid,NULL);
printf("sum = %d",sum);
}
/* The thread will begin handle in this function */
void *runner(void *param){
int i, upper = atoi(param);
sum = 0;
for (i = 1; i <= upper; i++)
sum += i;
pthread_exit(0);
}