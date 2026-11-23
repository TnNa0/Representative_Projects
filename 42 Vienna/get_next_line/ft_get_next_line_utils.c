/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_get_next_line_utils.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/07 12:43:08 by astoiber          #+#    #+#             */
/*   Updated: 2024/11/07 09:25:51 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>

char	*ft_strchr(const char *str, int c)
{
	size_t	i;

	i = 0;
	if (!str)
		return (NULL);
	while (i <= (size_t)ft_strlen((char *)str))
	{
		if (str[i] == (char)c)
			return ((char *)str + i);
		i++;
	}
	return (0);
}

char	*ft_strjoin(char *s1, char *s2)
{
	int		i;
	int		c;
	char	*new_str;

	i = 0;
	c = 0;
	if (!s1)
	{
		s1 = malloc(sizeof(char) + 1);
		if (!s1)
			return (NULL);
		s1[c] = '\0';
	}
	if (!s2)
		return (NULL);
	new_str = malloc(ft_strlen(s1) + ft_strlen(s2) + 1);
	if (!new_str)
		return (NULL);
	while (s1[c] != '\0')
		new_str[i++] = s1[c++];
	c = 0;
	while (s2[c] != '\0')
		new_str[i++] = s2[c++];
	new_str[i] = '\0';
	return (free(s1), new_str);
}

char	*ft_line_allocation(int fd, char *str)
{
	char	*buffer;
	ssize_t	result;

	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (NULL);
	result = 1;
	while (!(ft_strchr(str, '\n')) && result > 0)
	{
		result = read(fd, buffer, BUFFER_SIZE);
		if (result == -1)
		{
			free(buffer);
			return (NULL);
		}
		buffer[result] = '\0';
		str = ft_strjoin(str, buffer);
		if (!str)
			return (NULL);
	}
	free(buffer);
	return (str);
}

char	*ft_next_line(char *current_read)
{
	char	*new;
	int		i;
	int		c;

	i = 0;
	c = 1;
	while (current_read[i] && current_read[i] != '\n')
		i++;
	if (current_read[i] == '\n')
		c += 1;
	new = malloc(i + c);
	if (!new)
		return (NULL);
	i = 0;
	while (current_read[i] && current_read[i] != '\n')
	{
		new[i] = current_read[i];
		i++;
	}
	if (current_read[i] == '\n')
		new[i++] = '\n';
	new[i] = '\0';
	return (new);
}

char	*ft_rem_line(char *current_read)
{
	char	*new_line;
	int		i;
	int		j;

	i = 0;
	j = 0;
	while (current_read[i] && current_read[i] != '\n')
		i++;
	new_line = malloc((ft_strlen(current_read) - i) + 1);
	if (!new_line)
		return (NULL);
	if (current_read[i] == '\n')
		i++;
	while (current_read[i] != '\0')
	{
		new_line[j] = current_read[i];
		j++;
		i++;
	}
	new_line[j] = '\0';
	free(current_read);
	return (new_line);
}
