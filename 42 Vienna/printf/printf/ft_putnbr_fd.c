/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/10 14:35:54 by astoiber          #+#    #+#             */
/*   Updated: 2024/10/10 14:14:37 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

void	ft_putnbr_fd(int n, int fd, size_t *count)
{
	char	num;

	if (n == -2147483648)
	{
		write(fd, "-2147483648", 11);
		(*count) += 11;
		return ;
	}
	if (n < 0 && n > -2147483648)
	{
		ft_putchar_fd('-', 1, count);
		n *= -1;
	}
	if (n >= 10)
		ft_putnbr_fd(n / 10, fd, count);
	if (n >= 0)
	{
		num = (n % 10) + '0';
		ft_putchar_fd(num, 1, count);
	}
}
