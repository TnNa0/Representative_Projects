/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_gethexlower.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/28 14:46:25 by astoiber          #+#    #+#             */
/*   Updated: 2024/10/10 14:16:32 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

void	ft_gethexlower(void *ptr, size_t *count)
{
	char	*prefix;

	prefix = "0x";
	if (ptr == NULL)
	{
		ft_putstr_fd("(nil)", 1, count);
		return ;
	}
	ft_putstr_fd(prefix, 1, count);
	ft_puthex((unsigned long)ptr, count);
}
