/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/28 14:46:25 by astoiber          #+#    #+#             */
/*   Updated: 2024/10/10 14:16:48 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

void	ft_puthex(unsigned long nbr, size_t *count)
{
	char	hexnb;

	if (nbr >= 16)
		ft_puthex(nbr / 16, count);
	if (nbr % 16 > 9)
		hexnb = (nbr % 16 - 10) + 'a';
	else
		hexnb = (nbr % 16) + '0';
	ft_putchar_fd(hexnb, 1, count);
}
