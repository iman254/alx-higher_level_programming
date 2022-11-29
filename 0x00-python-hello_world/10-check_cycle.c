#include "lists.h"

/**
* check_cycle _ checks if a linked list contains a cycle
*@list: linked to check
*
* Return: 1 if the list has a cycle, o if it doesn't
*/

int chech_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;
	if (!list)
		return (0):

	while (slow && fast && faat ->nex)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
