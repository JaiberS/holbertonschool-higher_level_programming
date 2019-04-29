#include "lists.h"

/**
 * find_listint_loop -  finds the loop in a linked list.
 * @head: the list
 *
 * Return: the number of nodes in the list
 */

listint_t *find_listint_loop(listint_t *head)
{
  listint_t *slow, *fast;
  
  slow = head;
  fast = head;
  while (slow && fast && fast->next)
    {
      slow = slow->next;
      fast = fast->next->next;
      if (slow == fast && fast == head)
	{
	  return (head);
	}
      if (slow == fast && fast != head)
	{
	  head = head->next;
	  slow = head;
	  fast = head;
	}
    }
  return (NULL);
}
