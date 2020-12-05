CC = g++-9
CFLAGS = -pedantic-errors -Wall -Weffc++ -Wextra -Wsign-conversion 

run1: NAME = part1
run1: part1.cpp
	mkdir -p ./bin && \
	$(CC) $(CFLAGS) -o ./bin/$(NAME) $(NAME).cpp && \
	cat ../input.txt | ./bin/$(NAME)

