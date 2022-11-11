#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - loops infinitely.
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes.
 * Return: Always 0.
 * Description: For every zombie process created, it displays
 * "Zombie process created, PID: ZOMBIE_PID"
 */
int main(void)
{
	pid_t pid, i = 0;

	while (i < 5)
	{
		pid = fork();
		if (pid == -1)
		{
			printf("Error in forking");
			return (1);
		}
		else if (pid == 0) /* child process */
		{
			return (0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", pid);
			i++;
		}
	}

	infinite_while();
	return (0);
}
