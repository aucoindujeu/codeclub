CFLAGS=-Wall -g
CC=gcc

jeu:
	$(CC) $(CFLAGS) -o term-pacman term-pacman.c -lncurses 
	./term-pacman

play:
	./term-pacman

compile:
	$(CC) $(CFLAGS) -o term-pacman term-pacman.c -lncurses

test-ncurses:
	$(CC) $(CFLAGS) -o test-ncurses test-ncurses.c -lncurses
	./test-ncurses

cleanall:
	rm -f term-pacman
	rm -f test-ncurses

clean-tn:
	rm -f test-ncurses

clean-p:
	rm -f term-pacman
