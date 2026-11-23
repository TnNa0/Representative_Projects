/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_puthex_upper.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/27 16:15:49 by astoiber          #+#    #+#             */
/*   Updated: 2024/10/10 14:18:38 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

void	ft_puthex_upper(unsigned long nbr, size_t *count)
{
	char	hexnb;

	if (nbr >= 16)
		ft_puthex_upper(nbr / 16, count);
	if (nbr % 16 > 9)
		hexnb = (nbr % 16 - 10) + 'A';
	else
		hexnb = (nbr % 16) + '0';
	ft_putchar_fd(hexnb, 1, count);
}
