/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/10 14:30:58 by astoiber          #+#    #+#             */
/*   Updated: 2024/10/10 14:16:54 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

void	ft_putstr_fd(char *s, int fd, size_t *count)
{
	int	i;

	i = 0;
	if (!s)
	{
		ft_putstr_fd("(null)", 1, count);
		return ;
	}
	while (s[i])
	{
		write(fd, &s[i], 1);
		i++;
		(*count)++;
	}
}
