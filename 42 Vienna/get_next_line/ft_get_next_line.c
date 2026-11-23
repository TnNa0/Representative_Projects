/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_get_next_line.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/10/17 13:38:47 by astoiber          #+#    #+#             */
/*   Updated: 2024/11/07 09:28:31 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"
#include <stdio.h>

int	ft_strlen(const char *str)
{
	int	i;

	i = 0;
	if (!str)
		return (0);
	while (str[i])
		i++;
	return (i);
}

char	*ft_get_next_line(int fd)
{
	static char	*current_read;
	char		*output;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	current_read = ft_line_allocation(fd, current_read);
	if (!current_read)
		return (NULL);
	output = ft_next_line(current_read);
	if (!output || output[0] == '\0')
		return (free(output), free(current_read), current_read = NULL, NULL);
	current_read = ft_rem_line(current_read);
	return (output);
}

// int	main(void)
// {
// 	char	*s;
// 	int		fd;
// 	int		i;

// 	i = 1;
// 	fd = open("borrowed.txt", O_RDONLY);
// 	if (fd == -1)
// 	{
// 		perror("Error opening file");
// 		return (1);
// 	}
// 	while ((s = ft_get_next_line(fd)) != NULL)
// 	{
// 		printf("line [%i] :: %s", i, s);
// 		i++;
// 		free(s);
// 	}
// 	close(fd);
// 	return (0);
// }
