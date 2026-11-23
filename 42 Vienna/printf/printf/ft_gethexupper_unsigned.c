/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_gethexupper_unsigned.c                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/28 14:46:25 by astoiber          #+#    #+#             */
/*   Updated: 2024/10/10 14:18:30 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

void	ft_gethexupper_unsigned(unsigned int ptr, size_t *count)
{
	ft_puthex_upper(ptr, count);
}
