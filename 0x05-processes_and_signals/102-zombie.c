#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * forever_while - This is a function that repeats forever.
 * Return: 0 when return
 */

int forever_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Code starting zombie
 *
 * Return: Always 0 when return
 */
int main(void)
{
	int j;

	for (j = 0; j < 5; j++)
	{
		if (fork() == 0)
		{
			dprintf(1, "Zombie process created, PID: %d\n", getpid());
			return (0);
		}
	}
	forever_while();
	return (0);
}
