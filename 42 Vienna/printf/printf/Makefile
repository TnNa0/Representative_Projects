# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: astoiber <astoiber@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 13:00:30 by astoiber          #+#    #+#              #
#    Updated: 2024/10/15 10:30:02 by astoiber         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

SRC = ft_printf.c ft_isprintf.c ft_puthex_upper.c ft_putchar_fd.c ft_puthex.c ft_gethexlower.c ft_gethexlower_unsigned.c ft_gethexupper_unsigned.c ft_putnbr_unsigned_fd.c ft_putstr_fd.c ft_putnbr_fd.c

OFILES = $(SRC:.c=.o)

CFLAGS = -Wall -Werror -Wextra

NAME = libftprintf.a

AR = ar -rcs

all: $(NAME)

$(NAME): $(OFILES)
	$(AR) $(NAME) $(OFILES)

%.o: %.c
	cc $(CFLAGS) -c $< -o $@

bonus: $(NAME)
	
clean:
	rm -f $(OFILES)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all bonus clean fclean re
