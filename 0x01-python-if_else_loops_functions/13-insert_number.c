#include "lists.h"

/**
 * insert_node - adds a new node at index of a listint_t list.
 * @number: new data
 * @head: first node
 *
 * Return: the address of the new element, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *head2, *ant;
	unsigned int i = 0;

	if (head == NULL)
		return (0);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{		free(new);
		return (NULL);	}
	if (*head == NULL)
	{		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);	}
	head2 = *head;
	new->n = number;
	for (; new->n > head2->n && head2 != NULL; ant = head2,
		     head2 = head2->next, i++)
	{
		if (head2->next == NULL)
			break;	}
	if (head2->next != NULL)
	{
		if (i != 0)
		{
			ant->next = new;
			new->next = head2;		}
		else
		{
			new->next = *head;
			*head = new;
		}
	}
	else
	{
		head2->next = new;
		new->next = NULL;
	}
	return (new);
}
