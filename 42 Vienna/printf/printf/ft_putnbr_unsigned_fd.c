/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_unsigned_fd.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/28 14:38:16 by astoiber          #+#    #+#             */
/*   Updated: 2024/10/10 12:11:13 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

void	ft_putchar_unsigned_fd(unsigned char c, int fd, size_t *count)
{
	write(fd, &c, 1);
	(*count)++;
}

void	ft_putnbr_unsigned_fd(unsigned int n, int fd, size_t *count)
{
	char			num;

	if (n >= 10)
		ft_putnbr_unsigned_fd(n / 10, fd, count);
	num = (n % 10) + '0';
	ft_putchar_unsigned_fd(num, 1, count);
}
