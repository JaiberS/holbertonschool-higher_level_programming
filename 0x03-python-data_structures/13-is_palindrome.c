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
	int *tuple, i = 0, j = 0, conf = 0;
	listint_t *head2 = *head;

	if (head2 == NULL)
		return (1);
	for (; head2 != NULL; i++, head2 = head2->next)
		;
	tuple = malloc(sizeof(tuple) * i);
	for (i = 0, head2 = *head; head2 != NULL; i++, head2 = head2->next)
	{
		tuple[i] = head2->n;
/**
 *		if (head2->next != NULL)
 *			tuple = _realloc(tuple, i + 1, i + 2);
 */
	}
	i--;
	conf = cpalin(tuple, i, j);
	free(tuple);
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

/**
 * _realloc - reallocates a memory block
 * @ptr: initial pointer
 * @old_size: initial size
 * @new_size: new size
 * Return: pointer to array
 */
int *_realloc(int *ptr, unsigned int old_size, unsigned int new_size)
{
	int *clone, *relloc, *aux;
	unsigned int i;

	if (ptr != NULL)
		clone = ptr;
	else
	{
		aux = malloc(sizeof(int) * new_size);
		return (aux);
	}
	if (new_size == old_size)
		return (ptr);
	if (new_size == 0 && ptr != NULL)
	{ free(ptr);
		return (0); }
	relloc = malloc(sizeof(int) * new_size);
	if (relloc == NULL)
		return (0);
	for (i = 0; i < old_size; i++)
	{
		*(relloc + i) = clone[i];
	}
	*(relloc + i) = '\0';
	free(ptr);
	return (relloc);
}
