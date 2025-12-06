CC = gcc
CFLAGS = -Wall -I/usr/local/include -g
LDFLAGS = -L/usr/local/lib -lwolfssl -lwolfssh


SRC = test.c server.c
OBJ = $(SRC:.c=.o)


all: server


server: $(OBJ)
	$(CC) -o server $(OBJ) $(LDFLAGS)


clean:
	rm -f *.o server