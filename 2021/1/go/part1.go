package main

import (
	"bufio"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	var (
		prev  = 0
		count = -1
	)

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		cur, err := strconv.Atoi(scanner.Text())
		check(err)

		if cur > prev {
			count++
		}

		prev = cur
	}

	println(count)
}
