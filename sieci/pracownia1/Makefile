
TARGET = traceroute

# Kompilator
CC = gcc

# Flagi kompilatora
CFLAGS = -Wall -Wextra -std=gnu99

# Pliki zrodlowe
SRCS = traceroute.c

# Pliki obiektowe (zamiana .c na .o)
OBJS = $(SRCS:.c=.o)

# Kompilacja programu
all: $(TARGET)

# Tworzenie pliku wykonywalnego z plikow obiektowych
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# Kompilacja plikow .c do plikow .o
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Czyszczenie plikow obiektowych
clean:
	rm -f $(OBJS)

# Czyszczenie plikow obiektowych i pliku wykonywalnego
distclean: clean
	rm -f $(TARGET)
