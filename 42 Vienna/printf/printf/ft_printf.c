/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/09/27 16:15:49 by astoiber          #+#    #+#             */
/*   Updated: 2024/10/15 14:55:58 by astoiber         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "printf.h"

static void	ft_putconstchar_fd(const char *c, int fd, size_t *count)
{
	write(fd, c, 1);
	(*count)++;
}

static void	ft_formatspecifier(va_list arg_ptr, const char *format,
		size_t *count)
{
	if (*format == 'c')
		ft_putchar_fd(va_arg(arg_ptr, int), 1, count);
	else if (*format == 's')
		ft_putstr_fd(va_arg(arg_ptr, char *), 1, count);
	else if (*format == 'p')
		ft_gethexlower(va_arg(arg_ptr, void *), count);
	else if (*format == 'd' || *format == 'i')
		ft_putnbr_fd(va_arg(arg_ptr, int), 1, count);
	else if (*format == 'u')
		ft_putnbr_unsigned_fd(va_arg(arg_ptr, unsigned int), 1, count);
	else if (*format == 'x')
		ft_gethexlower_unsigned(va_arg(arg_ptr, unsigned int), count);
	else if (*format == 'X')
		ft_gethexupper_unsigned(va_arg(arg_ptr, unsigned int), count);
	else if (*format == '%')
		ft_putchar_fd('%', 1, count);
}

int	ft_check_input(const char *format, size_t form_count, va_list arg_ptr)
{
	size_t	arg_count;

	arg_count = 0;
	while (*format)
	{
		if (*format == '%')
		{
			format++;
			if (*format == '\0' || !ft_isprintf(*format))
			{
				write(1, "##format missing## ", 19);
				return (0);
			}
			form_count++;
		}
		format++;
	}
	while (arg_count < form_count)
	{
		va_arg(arg_ptr, void*);
		arg_count++;
	}
	if (form_count != arg_count)
	{
		write (1, "##unequal format to argument## ", 31);
		return (0);
	}
	return (1);
}

int	ft_printf(const char *format, ...)
{
	va_list	arg_ptr;
	size_t	count;
	size_t	form_count;

	count = 0;
	form_count = 0;
	if (format == NULL || ft_check_input(format, form_count, arg_ptr) == 0)
		return (0);
	va_start(arg_ptr, format);
	{
		while (*format)
		{
			if (*format == '%')
			{
				format++;
				ft_formatspecifier(arg_ptr, format, &count);
			}
			else
				ft_putconstchar_fd(format, 1, &count);
			format++;
		}
	}
	va_end(arg_ptr);
	return (count);
}

#include <stdio.h>

int	main(void)
{
	int				i;
	char			c;
	char			*s;
	void			*p;
	int				d;
	unsigned int	u;
	unsigned int	x;
	unsigned int	X;
	int				pp;

	i = 0;
	c = 'z';
	s = "hello";
	p = NULL;
	d = 0;
	u = -429496795;
	x = -429496795;
	X = -429496795;
	pp = 0;
	printf("this is the control:\n");

	printf("i %i, c %c, s %s, p %p, d %d, u %u, x %x, X %X, %%", i, c, s, p,
		d, u, x, X);
	//Check if number of % = number of va_arg??!!

	printf("\n\n");
	pp = printf("%i: ", i);
	printf("return value of i: %i\n", pp);
	pp = printf("%c: ", c);
	printf("return value of c: %i\n", pp);
	pp = printf("%s: ", s);
	printf("return value of s: %i\n", pp);
	pp = printf("%p: ", p);
	printf("return value of p: %i\n", pp);
	pp = printf("%d: ", d);
	printf("return value of d: %i\n", pp);
	pp = printf("%u: ", u);
	printf("return value of u: %i\n", pp);
	pp = printf("%x: ", x);
	printf("return value of x: %i\n", pp);
	pp = printf("%X: ", X);
	printf("return value of X: %i\n", pp);
	pp = printf("%%: ");
	printf("return value of %%: %i\n", pp);
	pp = 0;
	printf("#########################\n");
	printf("now comes my code:\n\n");

	ft_printf("i %i%i, c %c, s %s, p %p, d %d, u %u, x %x, X %X, %%", i, c, s, p, d, u, x, X);

	printf("\n\n");
	pp = ft_printf("%i: ", i);
	ft_printf("return value of i: %i\n", pp);
	pp = ft_printf("%c: ", c);
	ft_printf("return value of c: %i\n", pp);
	pp = ft_printf("%s: ", s);
	ft_printf("return value of s: %i\n", pp);
	pp = ft_printf("%p: ", p);
	ft_printf("return value of p: %i\n", pp);
	pp = ft_printf("%d: ", d);
	ft_printf("return value of d: %i\n", pp);
	pp = ft_printf("%u: ", u);
	ft_printf("return value of u: %i\n", pp);
	pp = ft_printf("%x: ", x);
	ft_printf("return value of x: %i\n", pp);
	pp = ft_printf("%X: ", X);
	ft_printf("return value of X: %i\n", pp);
	pp = ft_printf("%%: ");
	ft_printf("return value of %%: %i\n", pp);
	return (0);
}
