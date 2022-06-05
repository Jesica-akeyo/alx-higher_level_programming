#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head address of the linked list
 * Return: 0 if it is not a palindrome
 * 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *cur = *head;
	int tab[2048], i = 0, j = 0;

	if (*head)
	{
		while (cur)
		{
			tab[i] = cur->n;
			cur = cur->next;
			i++;
		}

		while (j < i / 2)
		{
			if (tab[j] == tab[i - j - 1])
				j++;
			else
				return (0);
		}
	}
	return (1);
}
