#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int tuple[999999], i = 0, j = 0, conf = 0;
	listint_t *head2 = *head;

	if (head2 == NULL)
		return (1);
	for (; head2 != NULL; i++, head2 = head2->next)
		;
/**
 *	tuple = malloc(sizeof(tuple) * i);
 */
	for (i = 0, head2 = *head; head2 != NULL; i++, head2 = head2->next)
	{
		tuple[i] = head2->n;
	}
	i--;
	conf = cpalin(tuple, i, j);
/**
 *	free(tuple);
 */
	return (conf);
}

/**
 * cpalin - checks for palindrome
 * @s: the string
 * @j: the counter in reverse
 * @i: the counter
 *
 * Return: 1 is palindrome 0 is not
 */

int cpalin(int *s, int j, int i)
{
	int r = 0;

	if (s[j] == s[i])
	{
		j--;
		i++;
		if (i > j)
			return (1);
		r = cpalin(s, j, i);
	}
	else
		return (0);
	return (r);
}
