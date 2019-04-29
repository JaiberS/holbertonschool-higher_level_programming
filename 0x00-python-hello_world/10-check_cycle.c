#include "lists.h"

/**
 * check_cycle -  finds the loop in a linked list.
 * @list: the list
 *
 * Return:  0 if no cycle, 1 if cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast && fast == list)
		{
			return (1);
		}
		if (slow == fast && fast != list)
		{
			list = list->next;
			slow = list;
			fast = list;
		}
	}
	return (0);
}
