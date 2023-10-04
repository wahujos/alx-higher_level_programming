#include "lists.h"
/**
 * insert_node - function that inserts a number
 * into a sorted single linked list
 * @head: a double pointer, a pointer to a pointer for the head
 * @number: interger type, the data
 * Return: a pointer to the inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *temp, *current, *previous;

	if (head == NULL)
	{
		return (NULL);
	}

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
	{
		return (NULL);
	}
	temp->n = number;
	temp->next = NULL;
	
	if (*head == NULL || number < (*head)->n)
	{
		temp->next = *head;
		*head = temp;
		return (temp);
	}
	current = *head;
	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}
	previous->next = temp;
	temp->next = current;

	return (temp);
}
